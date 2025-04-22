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
 

    steps {
 

        sh '''
 

            python3 -m pip install --upgrade pip
 

            pip3 install -r requirements.txt
 

            pip3 install pytest-playwright
 

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
 
                script {
 
                    try {
 
                        sh 'pytest tests/ --html=reports/report.html --self-contained-html'
 
                    } catch (Exception e) {
 
                        currentBuild.result = 'FAILURE'
 
                        throw e
 
                    }
 
                }
 
            }
 
        }
 

 
        stage('Archive HTML Report') {
 
            steps {
 
                archiveArtifacts artifacts: 'reports/*.html', allowEmptyArchive: true
 
            }
 
        }
 
    }
 
}
