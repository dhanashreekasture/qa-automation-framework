pipeline {
    agent any

    parameters {
        choice(
            name: 'ENV',
            choices: ['dev','qa','uat','prod'],
            description: 'Select Environment'
        )
    }

    stages {

        stage('Setup Python') {
            steps {
                sh '''
                python3 -m venv venv
                . venv/bin/activate
                pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                . venv/bin/activate
                mkdir -p reports/allure-results
                behave -D env=${ENV} -f allure_behave.formatter -o reports/allure-results
                '''
            }
        }

        stage('Allure Report') {
            steps {
                allure results: [[path: 'reports/allure-results']]
            }
        }
    }
}