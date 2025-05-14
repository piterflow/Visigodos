pipeline {
    agent any

    environment {
        GIT_USER = "piterflow"
        GIT_EMAIL = "andresrzcabel@gmail.com"
        BRANCH = "main"
        FILE_TO_TRACK = "app.py"
        REPO_URL = "https://github.com/piterflow/Visigodos.git"
    }

    stages {
        stage('Configurar Git') {
            steps {
                sh '''
                    git config user.name "$GIT_USER"
                    git config user.email "$GIT_EMAIL"
                '''
            }
        }

        stage('Detectar cambios en app.py') {
            steps {
                script {
                    def changed = sh(
                        script: "git status --porcelain | grep '${FILE_TO_TRACK}' || true",
                        returnStdout: true
                    ).trim()
                    
                    if (!changed) {
                        echo "No hay cambios en ${FILE_TO_TRACK}"
                        currentBuild.result = 'NOT_BUILT'
                        error("Sin cambios en ${FILE_TO_TRACK}")
                    } else {
                        echo "${FILE_TO_TRACK} ha cambiado"
                    }
                }
            }
        }

        stage('Commit y Push') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: '8e8c7f8b-d2b2-4d0e-9377-f27ffad3b960',
                    usernameVariable: 'USERNAME',
                    passwordVariable: 'PASSWORD'
                )]) {
                    sh '''
                        git add "${FILE_TO_TRACK}"
                        git commit -m "Auto-commit de ${FILE_TO_TRACK} desde Jenkins" || echo "Nada que commitear"
                        git push https://${USERNAME}:${PASSWORD}@github.com/piterflow/Visigodos.git HEAD:${BRANCH}
                    '''
                }
            }
        }
    }
}
