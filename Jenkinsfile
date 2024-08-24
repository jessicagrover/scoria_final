pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "my-django-app"   // Customize the Docker image name
        GIT_REPO = "https://github.com/jessicagrover/scoria_final.git"
        PATH= "/usr/local/bin/docker:/bin/sh"
        
    }
  


      stages {
        stage('Checkout') {
            steps {
                git url: "${GIT_REPO}", branch: 'main'
            }
        }

        stage('Install Dependencies') {
            steps {
                // Upgrade pip and install dependencies from requirements.txt
                sh 'pip install --upgrade pip'
                sh 'pip install -r requirements.txt'
            }
        }
        // stage('Clean Docker') {
        //     steps {
        //         script {
        //             sh 'docker system prune -f'
        //         }
        //     }
        // }

        stage('Run Tests') {
            steps {
                // Run Django tests
                sh 'python manage.py test'
            }
        }

        
        stage('Check Docker') {
            steps {
                script {
                    sh 'docker --version'
                    sh 'docker ps'
                }
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
            // sh 'docker system prune -f'
                script {
                    // Clean up Docker images and containers
                    sh 'docker system prune -f'
                }
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
