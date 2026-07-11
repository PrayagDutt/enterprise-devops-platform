# 🚀 Enterprise DevOps Task Management Platform

### End-to-End CI/CD Pipeline | AWS | Terraform | Docker | Jenkins | Kubernetes | Ansible | Grafana

> A production-style cloud-native DevOps project demonstrating Infrastructure as Code (IaC), Continuous Integration & Continuous Deployment (CI/CD), containerization, Kubernetes orchestration, and AWS cloud deployment.

---

# 📖 Project Overview

The **Enterprise DevOps Task Management Platform** demonstrates a complete DevOps lifecycle from infrastructure provisioning to application deployment using modern DevOps tools and AWS cloud services.

The application is built using **Python Flask** with **Amazon RDS MySQL** as the backend database. Infrastructure is provisioned using **Terraform**, containerized using **Docker**, and deployed automatically through **Jenkins CI/CD**. Kubernetes deployment manifests are included to demonstrate container orchestration and production deployment readiness.

The project follows enterprise DevOps practices including Infrastructure as Code, automated deployments, containerization, and cloud-native architecture.

---

# 🏗 Architecture Diagram

```text
                                     ┌────────────────────┐
                                     │     Developer      │
                                     └─────────┬──────────┘
                                               │
                                         Git Push
                                               │
                                               ▼
                                 ┌────────────────────────┐
                                 │        GitHub          │
                                 │ Source Code Repository │
                                 └─────────┬──────────────┘
                                           │ Webhook
                                           ▼
                              ┌────────────────────────────┐
                              │        Jenkins CI/CD       │
                              │                            │
                              │ • Checkout Code           │
                              │ • Build Docker Image      │
                              │ • Push Docker Hub         │
                              │ • Deploy Application      │
                              └─────────┬──────────────────┘
                                        │
                                        ▼
                           ┌──────────────────────────┐
                           │       Docker Hub         │
                           │ Container Registry       │
                           └─────────┬────────────────┘
                                     │
                                     ▼
                      ┌──────────────────────────────────┐
                      │         AWS Infrastructure        │
                      │                                  │
                      │  VPC                             │
                      │  ├── Public Subnet              │
                      │  │      └── EC2 Application     │
                      │  │             │                │
                      │  │             ▼                │
                      │  │      Docker Container        │
                      │  │             │                │
                      │  ├── Private Subnet             │
                      │  │      └── Amazon RDS MySQL    │
                      │  │                             │
                      │  └── Amazon S3                 │
                      └──────────────────────────────────┘
                                     │
                                     ▼
                           End Users Access Application
```

---

# ☁ AWS Architecture

The complete AWS infrastructure is provisioned using **Terraform**.

### Resources Created

- Amazon VPC
- Public Subnets
- Private Subnets
- Internet Gateway
- NAT Gateway
- Route Tables
- Security Groups
- EC2 Instances
- Amazon RDS MySQL
- Amazon S3
- Application Load Balancer Components
- IAM Roles

---

# ⚙ Technology Stack

| Category | Technologies |
|----------|--------------|
| Programming | Python, Flask |
| Database | MySQL, Amazon RDS |
| Cloud Platform | AWS EC2, RDS, VPC, IAM, S3 |
| Infrastructure as Code | Terraform |
| Configuration Management | Ansible |
| CI/CD | Jenkins |
| Containerization | Docker |
| Container Orchestration | Kubernetes |
| Monitoring | Grafana, Prometheus |
| Version Control | Git, GitHub |
| Operating System | Ubuntu Linux |

---

# 📂 Repository Structure

```
enterprise-devops-platform
│
├── Src/
│   ├── app/
│   ├── migrations/
│   ├── requirements.txt
│   └── run.py
│
├── terraform/
│   ├── vpc.tf
│   ├── subnet.tf
│   ├── internet-gateway.tf
│   ├── nat-gateway.tf
│   ├── route-table.tf
│   ├── security-group.tf
│   ├── ec2.tf
│   ├── alb.tf
│   ├── target-group.tf
│   ├── rds.tf
│   ├── s3.tf
│   ├── variables.tf
│   ├── versions.tf
│   └── userdata.sh
│
├── k8s/
│   ├── deployment.yaml
│   └── service.yaml
│
├── Dockerfile
├── Jenkinsfile
├── README.md
└── .gitignore
```

---

# 🔄 CI/CD Pipeline Workflow

The CI/CD pipeline automates the complete application deployment.

### Pipeline Flow

1. Developer pushes code to GitHub.
2. Jenkins automatically triggers the pipeline.
3. Jenkins checks out the latest source code.
4. Docker image is built.
5. Image is pushed to Docker Hub.
6. Latest container is deployed on the application server.
7. Flask application connects to Amazon RDS.
8. Users access the application.

---

# 🐳 Docker

## Build Image

```bash
docker build -t prayag1/enterprise-devops-platform:latest .
```

## Login

```bash
docker login
```

## Push Image

```bash
docker push prayag1/enterprise-devops-platform:latest
```

## Run Container

```bash
docker run -d \
-p 5000:5000 \
--name devops-platform \
prayag1/enterprise-devops-platform:latest
```

---

# ☸ Kubernetes

The project includes Kubernetes manifests for deployment.

Current resources:

- Deployment
- Service

Deployment supports:

- Multiple Replicas
- Rolling Updates
- Self-Healing Pods
- High Availability

---

# 🏗 Infrastructure as Code

Infrastructure provisioning is fully automated using **Terraform**.

Terraform provisions:

- VPC
- Networking
- EC2
- Security Groups
- RDS
- S3
- IAM
- Load Balancer Components

Benefits:

- Repeatable deployments
- Version-controlled infrastructure
- Easy scalability
- Automated provisioning

---

# ⚙ Configuration Management

The project is designed to support **Ansible** for server configuration automation.

Typical automation tasks include:

- Package Installation
- Docker Installation
- Python Installation
- Jenkins Configuration
- Environment Configuration
- Application Deployment

---

# 📊 Monitoring

The platform is designed for integration with modern monitoring tools.

Monitoring Stack

- Grafana Dashboards
- Prometheus Metrics
- EC2 Monitoring
- Docker Monitoring
- Kubernetes Monitoring
- Infrastructure Health Monitoring

---

# 🔐 Security Features

- Private Amazon RDS
- Security Groups
- IAM Roles
- Private Networking
- Public/Private Subnet Separation
- Least Privilege Access

---

# 🌟 Key Features

- ✅ Infrastructure as Code using Terraform
- ✅ End-to-End CI/CD using Jenkins
- ✅ Dockerized Flask Application
- ✅ Amazon RDS MySQL Integration
- ✅ AWS Infrastructure Deployment
- ✅ Kubernetes Deployment Ready
- ✅ GitHub Source Control
- ✅ Docker Hub Integration
- ✅ Secure Networking
- ✅ Monitoring Ready with Grafana & Prometheus
- ✅ Configuration Automation Ready with Ansible

---

# 🚀 Future Enhancements

- Kubernetes Ingress Controller
- Horizontal Pod Autoscaler (HPA)
- Helm Charts
- ArgoCD GitOps
- Prometheus Monitoring
- Grafana Dashboards
- Ansible Playbooks
- SSL/TLS using AWS ACM
- Route53 DNS
- Blue-Green Deployment
- Canary Deployment

---

# 📈 Learning Outcomes

This project demonstrates practical experience with:

- AWS Cloud
- DevOps Practices
- Infrastructure as Code
- Continuous Integration
- Continuous Deployment
- Docker
- Kubernetes
- Terraform
- Jenkins
- GitHub
- Linux Administration
- Cloud Networking

---

# 👨‍💻 Author

**Prayag Dutt**

**GitHub**

https://github.com/Prayag762

**LinkedIn**

www.linkedin.com/in/prayag-dutt

---

# ⭐ If you found this project useful, don't forget to Star the repository.
