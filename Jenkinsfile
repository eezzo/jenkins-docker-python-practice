pipeline {
  agent { docker { image 'python:3.8.5-buster' } }
  stages {
    stage('build') {
      steps {
        sh 'pip install -r requirements.txt'
      }
    }
    stage('test') {
      steps {
        sh 'python webrequest_test.py'
      }
    }
  }
}