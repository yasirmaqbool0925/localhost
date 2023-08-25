pipeline {
    agent any
    stages {
        stage('Clone the Repo') {
            // steps {
            //     script {
            //         git branch: 'main', url: 'https://github.com/yasirmaqbool0925/localhost.git'
            //     }
            // }
        // }
        stage('Open Localhost') {
            steps {
                script {
                    bat 'python script.py'
                }
            }
        }
    }
}
}