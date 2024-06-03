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
        stage('Integration Tests on Staging') {
         steps {
         script {
         echo "Running integration tests on the staging environment to ensure the application functions as expected in a production-like environment"
         // Create a custom message file
         writeFile file: 'build.log', text: 'Build log contents...'
         }
         }
         post {
         success {
         // Archive the build log file as an artifact
         archiveArtifacts artifacts: 'build.log', allowEmptyArchive: true
         // Send notification email for successful pipeline
         emailext (
         subject: "Pipeline Status: SUCCESS",
         body: "The Jenkins pipeline has completed successfully. Please find the build log
        attached.",
         to: "rsb132500000@gmail.com",
         attachmentsPattern: 'build.log' // Attach the build log file to the email
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
