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
                bat 'docker run --rm --network csvtopostgresql_default -v "%WORKSPACE%\\data:/data" csv-to-postgresql-app:latest'
            }
        }
    }
}