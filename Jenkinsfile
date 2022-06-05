pipeline{
  agent any
  environment{
    docker_credentials=credentials('dockerhub')
  }
  stages{
    
    stage('Build'){
      steps{
        sh 'sudo docker build -t onesmus/rds .'
      }
    }
    stage('Test'){
      steps{
        echo "test"
      }
    }
    stage('Deploy'){
      steps{
        echo "Deploy"
      }
    }
  }
  
  
}
  
