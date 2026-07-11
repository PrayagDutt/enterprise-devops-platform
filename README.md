markdown
<!-- ANIMATED HEADER -->
<div align="center">
  <img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&size=32&duration=3000&pause=500&color=36BCF7&center=true&vCenter=true&width=600&lines=Hello%2C+I'm+Prayag+Dutt;DevOps+Engineer;Cloud+Architect;Automation+Enthusiast" alt="Typing Animation" />
</div>

<!-- PROFILE BADGES -->
<div align="center">
  <a href="https://github.com/Prayag762"><img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white"/></a>
  <a href="https://linkedin.com/in/prayag-dutt"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white"/></a>
  <a href="mailto:prayag.dutt@email.com"><img src="https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white"/></a>
  <img src="https://komarev.com/ghpvc/?username=Prayag762&style=for-the-badge&color=blueviolet" alt="Profile Views" />
</div>

<!-- BANNER -->
<div align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&height=100&section=header&text=DevOps%20Engineer&fontSize=30&fontAlignY=40" width="100%" />
</div>

---

# 🚀 Enterprise DevOps Task Management Platform

### End-to-End CI/CD Pipeline | AWS | Terraform | Docker | Jenkins | Kubernetes | Ansible | Grafana

> A production-style cloud-native DevOps project demonstrating Infrastructure as Code (IaC), Continuous Integration & Continuous Deployment (CI/CD), containerization, Kubernetes orchestration, and AWS cloud deployment.

---

# 📖 Project Overview

The **Enterprise DevOps Task Management Platform** demonstrates a complete DevOps lifecycle from infrastructure provisioning to application deployment using modern DevOps tools and AWS cloud services.

The application is built using **Python Flask** with **Amazon RDS MySQL** as the backend database. Infrastructure is provisioned using **Terraform**, containerized using **Docker**, and deployed automatically through **Jenkins CI/CD**. Kubernetes deployment manifests are included to demonstrate container orchestration and production deployment readiness.

The project follows enterprise DevOps practices including Infrastructure as Code, automated deployments, containerization, and cloud-native architecture.

🏗 Architecture
                               Developer
                                   │
                                   │ Git Push
                                   ▼
                           GitHub Repository
                                   │
                                   ▼
                          Jenkins CI/CD Pipeline
        ┌─────────────────────────────────────────────────┐
        │                                                 │
        │ Checkout Source Code                           │
        │ Install Dependencies                           │
        │ Run Tests                                      │
        │ Build Docker Image                             │
        │ Push Image to Docker Hub                       │
        │ Deploy Latest Version                          │
        └─────────────────────────────────────────────────┘
                                   │
                                   ▼
                            Docker Hub Registry
                                   │
                                   ▼
                      Kubernetes Deployment (AWS EC2)
                 ┌───────────────────────────────────────┐
                 │                                       │
                 │ Replica Set                           │
                 │ Pod 1                                │
                 │ Pod 2                                │
                 │ Self-Healing                         │
                 │ Rolling Updates                      │
                 └───────────────────────────────────────┘
                                   │
                         Kubernetes Service
                                   │
                                   ▼
                     AWS Application Load Balancer
                                   │
                                   ▼
                           Flask Web Application
                                   │
                    ┌──────────────┴──────────────┐
                    ▼                             ▼
            Amazon RDS MySQL                 Amazon S3
          Application Database          Static Files / Storage

────────────────────────────────────────────────────────────────

Infrastructure Provisioning
Terraform
    │
    ├── VPC
    ├── Public Subnets
    ├── Private Subnets
    ├── Internet Gateway
    ├── NAT Gateway
    ├── Route Tables
    ├── Security Groups
    ├── EC2
    ├── RDS
    ├── S3
    ├── IAM
    └── Load Balancer

Server Configuration
Ansible
    │
    ├── Docker Installation
    ├── Jenkins Installation
    ├── Kubernetes Configuration
    ├── Package Installation
    └── Application Deployment

Monitoring
Grafana + Prometheus
🚀 Technology Stack
Category	Technology
Programming Language	Python
Framework	Flask
Database	MySQL, Amazon RDS
Containerization	Docker
Container Orchestration	Kubernetes
CI/CD	Jenkins
Infrastructure as Code	Terraform
Configuration Management	Ansible
Cloud Platform	AWS
Monitoring	Prometheus, Grafana
Image Registry	Docker Hub
Version Control	Git & GitHub
☁ AWS Services Used
Amazon EC2
Amazon RDS (MySQL)
Amazon VPC
Public & Private Subnets
Internet Gateway
NAT Gateway
Route Tables
Security Groups
Application Load Balancer
IAM
Amazon S3
⚙ DevOps Workflow
Developer

      │

Git Push

      │

GitHub

      │

Webhook

      │

Jenkins

      │

Build

      │

Docker Image

      │

Push

      ▼

Docker Hub

      │

Deploy

      ▼

Kubernetes

      │

Pods

      │

Service

      │

Load Balancer

      ▼

Flask Application

      │

Amazon RDS
📂 Repository Structure
enterprise-devops-platform/
│
├── Src/                     # Flask Application
├── terraform/               # Infrastructure as Code
├── ansible/                 # Configuration Management
├── k8s/                     # Kubernetes Manifests
├── Dockerfile
├── Jenkinsfile
├── README.md
└── .gitignore
✨ Key Features
✅ End-to-End CI/CD Pipeline using Jenkins
✅ Infrastructure Provisioning using Terraform
✅ Configuration Management using Ansible
✅ Dockerized Flask Application
✅ Docker Hub Image Repository
✅ Kubernetes Deployments
✅ Rolling Updates
✅ Self-Healing Pods
✅ Replica Management
✅ Amazon RDS Integration
✅ Amazon S3 Integration
✅ Application Load Balancer
✅ Public & Private Networking
✅ Secure Security Groups
✅ Infrastructure Automation
✅ Production-style DevOps Workflow
✅ Monitoring Ready with Prometheus & Grafana
🐳 Docker
Build Image
docker build -t prayag1/enterprise-devops-platform:latest .
Push Image
docker login
docker push prayag1/enterprise-devops-platform:latest
Run Container
docker run -d \
-p 5000:5000 \
--name devops-platform \
prayag1/enterprise-devops-platform:latest
☸ Kubernetes

Deploy Application

kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml

Check Pods

kubectl get pods

Check Services

kubectl get svc
🌍 Terraform

Initialize

terraform init

Plan

terraform plan

Apply

terraform apply
⚙ Ansible

Run Playbook

ansible-playbook playbook.yml
📊 Monitoring

The platform is designed to integrate with:

Prometheus
Grafana
Node Exporter
cAdvisor

These tools provide:

Infrastructure Monitoring
Container Monitoring
CPU & Memory Utilization
Application Health
Kubernetes Metrics
Alerting & Dashboards
📈 Future Enhancements
Kubernetes Ingress Controller
Horizontal Pod Autoscaler
Helm Charts
AWS EKS Deployment
ArgoCD GitOps
SonarQube Integration
Trivy Image Scanning
AWS CloudWatch Logs
Prometheus Alert Manager
👨‍💻 Author

Prayag Dutt

DevOps Engineer | AWS | Docker | Kubernetes | Terraform | Jenkins | Ansible | Python | Linux | CI/CD

---

