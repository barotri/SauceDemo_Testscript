pipeline {
    agent {
        docker {
            image 'mcr.microsoft.com/playwright/python:v1.51.0-noble'
            args '--user 1001'
        }
    }

    environment {
        PATH = "${HOME}/.local/bin:${env.PATH}"
    }

    options {
        timestamps()
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Set up Python & Install dependencies') {
            steps {
                sh '''
                    python -m pip install --upgrade pip
                    pip install -r requirements.txt
                    pip install pytest-playwright
                '''
            }
        }

        stage('Install Playwright Browsers') {
            steps {
                sh 'playwright install'
            }
        }

        stage('Run tests with pytest') {
            steps {
                sh 'pytest tests/ --html=reports/report.html --self-contained-html'
            }
        }

        stage('Archive HTML Report') {
            steps {
                archiveArtifacts artifacts: 'reports/*.html', allowEmptyArchive: true
            }
        }
    }

    post {
        always {
            junit 'tests/**/junit-*.xml' // nếu bạn dùng thêm pytest-junit
        }
        failure {
            echo 'Build failed. Check the test report.'
        }
    }
}
