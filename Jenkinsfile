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
    stage('push'){
      steps{
        sh 'sudo docker push onesmus1024/rds  '
      }
    }
    stage('Deploy'){
      steps{
        echo "sudo docker push onesmus1024/rds  "
      }
    }
  }
  
  
}
  
