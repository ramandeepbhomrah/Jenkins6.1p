pipeline {
 agent any
 environment {
 DIRECTORY_PATH = "/path/user/raman"
 TESTING_ENVIRONMENT = "test-env"
 PRODUCTION_ENVIRONMENT = "ramandeep"
 }
 stages {
 stage('Build') {
 steps {
 echo "Utilizing Maven, fetch the source code from the directory path ${env.DIRECTORY_PATH}"
 echo "Compiling the code with artifacts"
 }
 }
 stage('Unit and Integration Tests') {
 steps {
 echo "unit tests"
 sleep(time: 10, unit: 'SECONDS')
 echo "integration tests"
 }
 }
 stage('Code Analysis') {
 steps {
 echo "end of integration, go to the next step"

 }
 }
 stage('Security Scan') {
 steps {
 echo "security scan l"
 }
 }
 stage('Deploy to Staging') {
 steps {
 echo "Installing the application on an AWS Elastic Beanstalk staging server"
 }
 }
 stage('Integration Tests on Staging') {
 steps {
 script {
 echo "Running integration tests on the staging environment"
 writeFile file: 'build.log', text: 'Build log contents...'
 }
 }
 post {
 success { 
 archiveArtifacts artifacts: 'build.log', allowEmptyArchive: true
 // Send notification email for successful pipeline
 emailext (
 subject: "Pipeline Status: SUCCESS",
 body:"The Jenkins pipeline has completed successfully. Please find the build log
attached.",
 to: "ramandeep0508@gmail.com",
attachmentsPattern: 'build.log' 
 )
 }
 }
 }
 stage('Deploy to Production') {
 steps {
 echo "Deploying code:
${env.PRODUCTION_ENVIRONMENT}"
 }
 }
 }
}
