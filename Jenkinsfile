pipeline {
    agent any

    environment {
        IMAGE_NAME = "prayag1/enterprise-devops-platform"
        IMAGE_TAG  = "${BUILD_NUMBER}"
        K8S_NAMESPACE = "default"
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                sh '''
                    docker build -t $IMAGE_NAME:$IMAGE_TAG .
                    docker tag $IMAGE_NAME:$IMAGE_TAG $IMAGE_NAME:latest
                '''
            }
        }

        stage('Docker Hub Login') {
            steps {
                withCredentials([
                    usernamePassword(
                        credentialsId: 'dockerhub',
                        usernameVariable: 'DOCKER_USER',
                        passwordVariable: 'DOCKER_PASS'
                    )
                ]) {
                    sh '''
                        echo "$DOCKER_PASS" | docker login \
                        -u "$DOCKER_USER" \
                        --password-stdin
                    '''
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                sh '''
                    docker push $IMAGE_NAME:$IMAGE_TAG
                    docker push $IMAGE_NAME:latest
                '''
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                withKubeConfig(
                    credentialsId: 'kubernetes-cluster'
                ) {
                    sh '''
                        kubectl apply -f kubernetes/deployment.yaml
                        kubectl apply -f kubernetes/service.yaml

                        kubectl set image deployment/enterprise-devops-platform \
                        enterprise-devops-platform=$IMAGE_NAME:$IMAGE_TAG \
                        -n $K8S_NAMESPACE

                        kubectl rollout status deployment/enterprise-devops-platform \
                        -n $K8S_NAMESPACE
                    '''
                }
            }
        }
    }

    post {
        success {
            echo 'Docker image built, pushed, and deployed to Kubernetes successfully!'
        }

        failure {
            echo 'Pipeline Failed!'
        }

        always {
            sh 'docker logout || true'
        }
    }
}
