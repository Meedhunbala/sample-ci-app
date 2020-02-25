node('docker') {
 
    stage 'Checkout'
        git 'https://github.com/Meedhunbala/sample-ci-app.git'
        
    stage 'Build UnitTest'
        sh "docker-compose build test-app"
  
    stage 'Integration Test'
        sh "docker-compose up --abort-on-container-exit --force-recreate test-app"
        sh "docker-compose down -v"
        
}
