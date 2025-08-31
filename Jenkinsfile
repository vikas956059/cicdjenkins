pipeline {
  environment {
    dockerimagename = "vikas956059/python"
    dockerImage = ""
  }
  agent any

  stages {
    stage('Clone Repo') {
      steps {
        git branch: 'main', credentialsId: 'github', url: 'https://github.com/vikas956059/cicdjenkins.git'
      }
    }

    stage('Build') {
      steps {
        script {
          dockerImage = docker.build("${dockerimagename}:${BUILD_NUMBER}")
        }
      }
    }

    stage('Push Image') {
      environment {
        registryCredential = 'dockerhub'
      }
      steps {
        script {
          docker.withRegistry('https://registry.hub.docker.com', registryCredential) {
            dockerImage.push()
          }
        }
      }
    }

    stage('Deploy') {
      steps {
        withCredentials([file(credentialsId: 'kubernetes', variable: 'KUBECONFIG')]) {
          script {
           try {
          sh """
          echo "deployment update"
          kubectl --kubeconfig=$KUBECONFIG set image deployment/vikas vikas=${dockerimagename}:${BUILD_NUMBER} --record || \
          kubectl --kubeconfig=$KUBECONFIG rollout status deployment/vikas
          """
          }
          catch (err) {
           sh kubectl --kubeconfig=$KUBECONFIG rollout undo deployment/vikas
          }
        }
      }
     }
    }
  }
}

