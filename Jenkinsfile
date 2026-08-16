pipeline {
    agent any

    stages {
        stage('Build Docker') {
            steps {
                bat 'docker-compose build'
            }
        }

        stage('Run Application') {
            steps {
                bat 'docker-compose up -d --no-recreate app'
            }
        }
    }
}