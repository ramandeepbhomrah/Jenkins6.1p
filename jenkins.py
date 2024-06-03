pipeline {
    agent any
    environment {
        REPO_URL = "https://github.com/ramandeepbhomrah/Jenkins6.1p.git"
        REPO_PATH = "/path/user/raman"
        DEV_ENV = "development-env"
        PROD_ENV = "production-env"
    }
    stages {
        stage('Clone Repository') {
            steps {
                echo "Cloning the repository from the path: ${env.REPO_PATH}"
                git url: "${env.REPO_URL}", branch: 'main', credentialsId: '4eba3e14-63ea-4039-8ca7-8f0a45bd4a57'
            }
        }
        stage('Compile') {
            steps {
                echo "Compiling the application using Gradle"
               
            }
        }
        stage('Test') {
            steps {
                echo "Executing unit tests"
               
            }
        }
       
        stage('Dependency Check') {
            steps {
                echo "Checking for known vulnerabilities using OWASP Dependency-Check"
                // Example: Running Dependency-Check
                
            }
        }
        stage('Deploy to Development') {
            steps {
                echo "Deploying the application to the development environment"
                // Example: Deploy to development environment
               
            }
        }
        stage('Integration Tests in Dev') {
            steps {
                echo "Running integration tests in the development environment"
               
            }
            post {
                success {
                    echo 'Integration tests passed'
                    archiveArtifacts artifacts: '**/target/*.jar', allowEmptyArchive: false
                    emailext(
                        subject: "Build Successful",
                        body: "The build and integration tests have passed. Artifacts are archived.",
                        to: "rsb132500000@gmail.com"
                    )
                }
                failure {
                    echo 'Integration tests failed'
                    emailext(
                        subject: "Build Failed",
                        body: "The build or integration tests failed. Please check the Jenkins logs.",
                        to: "rsb132500000@gmail.com"
                    )
                }
            }
        }
        stage('Deploy to Production') {
            steps {
                echo "Deploying the application to the production environment: ${env.PROD_ENV}"
                // Example: Deploy to production environment
                
            }
        }
    }
}
