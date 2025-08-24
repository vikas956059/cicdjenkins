pipeline {
  enviroment {
   dockerimagename= "vikas956059/python"
   dockerImage = ""
   }
  agent any
   stages {
    stage('clone repo') {
       steps {
        git branch: 'main', credentialsId: 'github', url: 'https://github.com/vikas956059/cicdjenkins.git'
        }
      }
    stage('build') {
      steps{
       script{
       dockerImage= docker.build(dockerimagename)
         }
      }
     }
    stage('push image') {
      enviroment {
       registryCredentail = 'dockerhublogin'
       }
      steps{
        script{
           docker.withRegistry('https://registry.hub.docker.com',registryCredentail) {

           dockerImage.push("latest")
           }
         }
       }
    }       
   }    
  }   
