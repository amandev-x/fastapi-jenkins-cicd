pipeline {
    agent {label 'agent'}

    environment {
        DOCKERHUB_CREDS = credentials("docker")
        DOCKER_USERNAME = "amandabral9954"
        IMAGE_NAME = "fastapi-app"
        IMAGE_TAG = "${BUILD_NUMBER}"
        PYTHON_VERSION = "python3"
        VENV_DIR = "venv"
    }

    stages {
        stage("Checkout") {
            steps {
                checkout scm
            }
        }

        stage("Setting up environment") {
            steps {
                echo "Installing dependencies"
                sh '''
                  ${PYTHON_VERSION} -m venv ${VENV_DIR}
                  . ${VENV_DIR}/bin/activate
                  pip3 install -r requirements.txt
                '''
            }
        }

        stage("Run tests") {
            steps {
                echo "Running tests cases"
                sh '''
                . ${VENV_DIR}/bin/activate
                pytest tests/test.py -v
                '''
            }
        }

        stage("Building docker images 🐳") {
            steps {
                echo "Building docker images"
                script {
                    docker.build("${DOCKER_USERNAME}/${IMAGE_NAME}:${IMAGE_TAG}")
                }
            }
        }

        stage("Testing docker image") {
            steps {
                sh '''
                docker run -d --name test-container -p 8000:8000 ${DOCKER_USERNAME}/${IMAGE_NAME}:${IMAGE_TAG}
                sleep 5
                curl -f http://localhost:8000/health || exit 1
                docker rm -f test-container
                '''
            }
        }
    }

    post {
        success {
            echo '✅ Pipeline completed successfully!'
            echo "Application deployed: http://3.111.213.6:8000"
        }

        failure {
            echo '❌ Pipeline failed!'
        }

        always {
            echo "Cleaning up"
            sh 'rm -rf ${VENV_DIR}'
        }
    }
}