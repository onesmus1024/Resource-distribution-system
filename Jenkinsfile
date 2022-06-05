pipeline{
  agent any
  environment{
    docker_credentials=credentials('dockerhub')
  }
  stages{
    
    stage('build'){
      steps{
        sh 'sudo docker build -t onesmus/rds .'
      }
    }
  }
  
  
}
  
