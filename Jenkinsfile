pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "my-django-app"   // Customize the Docker image name
    }

    stages {
        stage('Checkout Code') {
            steps {
                // Clone the repository
                git branch: 'main', url: 'https://github.com/jessicagrover/scoria_final.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                // Upgrade pip and install dependencies from requirements.txt
                sh 'pip install --upgrade pip'
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                // Run Django tests
                sh 'python manage.py test'
            }
        }

        stage('Build Docker Image') {
            steps {
                // Build the Docker image
                script {
                    docker.build("${DOCKER_IMAGE}")
                }
            }
        }

        stage('Deploy') {
            steps {
                // Run the Docker container
                script {
                    docker.image("${DOCKER_IMAGE}").run('-d -p 8000:8000')
                }
            }
        }
    }

    post {
        always {
            // Cleanup Docker resources
            echo 'Cleaning up Docker resources...'
            sh 'docker system prune -f'
        }
        success {
            // Notification on success
            echo 'Deployment successful!'
        }
        failure {
            // Notification on failure
            echo 'Deployment failed!'
        }
    }
}
