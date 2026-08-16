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
                bat 'docker-compose run --rm --no-deps app'
            }
        }
    }
}