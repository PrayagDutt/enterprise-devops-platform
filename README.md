<!-- Header Banner -->
<img src="https://capsule-render.vercel.app/api?type=waving&color=0EA5E9&height=150&section=header&text=Hello!%20I'm%20Prayag%20Dutt&fontSize=40&fontAlignY=35&animation=twinkling&fontColor=ffffff" width="100%" />
<div align="center">
<!-- Typing Animation -->
<a href="https://linkedin.com/in/prayag-dutt">
  <img src="https://readme-typing-svg.herokuapp.com?font=Inter&weight=600&size=24&duration=3000&pause=1000&color=0EA5E9&center=true&vCenter=true&width=600&lines=DevOps+Engineer;Cloud+Architect;;Automation+Enthusiast" alt="Typing Animation" />
</a>
<br>
<!-- Social Badges (Using their official brand colors for better recognition) -->
<a href="https://github.com/Prayag762">
  <img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub"/>
</a>
<a href="https://linkedin.com/in/prayag-dutt">
  <img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn"/>
</a>
<a href="mailto:prayag.dutt@email.com">
  <img src="https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white" alt="Email"/>
</a>
<br><br>
<!-- Profile Views -->
<img src="https://komarev.com/ghpvc/?username=Prayag762&style=flat-square&color=0EA5E9&label=Profile%20Views" alt="Profile Views" />
</div>
---
# 🚀 Enterprise DevOps Task Management Platform

### End-to-End CI/CD Pipeline | AWS | Terraform | Docker | Jenkins | Kubernetes | Ansible | Grafana

> A production-style cloud-native DevOps project demonstrating Infrastructure as Code (IaC), Continuous Integration & Continuous Deployment (CI/CD), containerization, Kubernetes orchestration, and AWS cloud deployment.

---

## 📖 Project Overview

The **Enterprise DevOps Task Management Platform** demonstrates a complete DevOps lifecycle from infrastructure provisioning to application deployment using modern DevOps tools and AWS cloud services.

The application is built using **Python Flask** with **Amazon RDS MySQL** as the backend database. Infrastructure is provisioned using **Terraform**, containerized using **Docker**, and deployed automatically through **Jenkins CI/CD**. Kubernetes deployment manifests are included to demonstrate container orchestration and production deployment readiness.

The project follows enterprise DevOps practices including Infrastructure as Code, automated deployments, containerization, and cloud-native architecture.

## 🏗 Architecture Diagram

```mermaid
flowchart TB
    %% TOP - Developer (Code Provider)
    Developer["👨‍💻 Developer"]
    
    %% USERS Column (Bottom)
    Users["👥 End Users"]
    
    %% CI/CD Pipeline
    subgraph CI["CI/CD Pipeline"]
        GitHub["📦 GitHub Repository"]
        Jenkins["⚙️ Jenkins CI/CD"]
        DockerBuild["🐳 Build Docker Image"]
        DockerPush["📤 Push to Docker Hub"]
    end
    
    %% Kubernetes on EC2
    subgraph K8s["Kubernetes Cluster (AWS EC2)"]
        subgraph Workers["Worker Nodes (EC2 Instances)"]
            Pod1["📦 Pod 1"]
            Pod2["📦 Pod 2"]
            Pod3["📦 Pod 3"]
        end
        subgraph Control["Control Plane"]
            API["⚙️ API Server"]
            Scheduler["📅 Scheduler"]
        end
        Service["🔄 Kubernetes Service"]
    end
    
    %% AWS Cloud
    subgraph AWS["AWS Cloud"]
        ALB["⚖️ Application Load Balancer"]
        subgraph Database["Database"]
            RDS["🗄️ Amazon RDS MySQL"]
        end
        subgraph Storage["Storage"]
            S3["📁 Amazon S3"]
        end
        subgraph IaC["Infrastructure"]
            Terraform["🏗️ Terraform"]
            Ansible["⚙️ Ansible"]
        end
    end
    
    %% Monitoring
    subgraph Monitoring["Monitoring"]
        Prometheus["📈 Prometheus"]
        Grafana["📉 Grafana"]
    end

    %% MAIN FLOW - Developer to Deployment
    Developer -->|"1. Writes & Pushes Code"| GitHub
    GitHub -->|"2. Webhook Trigger"| Jenkins
    Jenkins -->|"3. Checkout Code"| GitHub
    Jenkins -->|"4. Build Docker Image"| DockerBuild
    DockerBuild -->|"5. Push to Registry"| DockerPush
    DockerPush -->|"6. Deploy to K8s"| API
    
    %% Kubernetes Internal Flow
    Control -->|"7. Schedule Pods on EC2"| Workers
    Workers -->|"8. Expose Application"| Service
    Service -->|"9. Route Traffic"| ALB
    ALB -->|"10. User Access via Browser"| Users
    
    %% Data & Infrastructure
    Workers -->|"11. Store Persistent Data"| RDS
    Workers -->|"12. Store Static Files"| S3
    Terraform -->|"13. Provision Infrastructure"| ALB
    Ansible -->|"14. Configure Cluster"| API
    
    %% Monitoring
    Workers -->|"15. Scrape Metrics"| Prometheus
    Prometheus -->|"16. Visualize Dashboards"| Grafana

    %% Developer Style - RED
    style Developer fill:#ff4444,stroke:#cc0000,stroke-width:4px,color:#ffffff,font-size:18px,font-weight:bold
    
    %% Users Style - BLUE
    style Users fill:#4A90D9,stroke:#2C5F8A,stroke-width:4px,color:#ffffff,font-size:18px,font-weight:bold
    
    %% Subgraph Styles
    style CI fill:#f3e5f5,stroke:#6a1b9a,stroke-width:2px
    style K8s fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px
    style Control fill:#fff3e0,stroke:#e65100,stroke-width:2px
    style Workers fill:#fce4ec,stroke:#c62828,stroke-width:2px
    style AWS fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px
    style Monitoring fill:#f3e5f5,stroke:#6a1b9a,stroke-width:2px
    style IaC fill:#e8eaf6,stroke:#283593,stroke-width:2px
    style Database fill:#e0f7fa,stroke:#00695c,stroke-width:2px
    style Storage fill:#fff8e1,stroke:#f57f17,stroke-width:2px

    %% Pure Black Arrows
    linkStyle default stroke:black,stroke-width:3px,color:black

```
🔄 CI/CD Pipeline Workflow

### 🔄 CI/CD Pipeline Workflow

```mermaid
flowchart LR
    A[Developer] -->|Git Push| B[GitHub]
    B -->|Webhook| C[Jenkins]
    C --> D[Checkout Source Code]
    D --> E[Install Dependencies]
    E --> F[Run Tests]
    F --> G[Build Docker Image]
    G --> H[Push to Docker Hub]
    H --> I[Deploy Latest Version]
    I --> J[Kubernetes Cluster]
    J --> K[Application Live]
    
    classDef default fill:#0ea5e9,stroke:#0284c7,stroke-width:2px,color:#ffffff;

```

## ☁ AWS Architecture

The complete AWS infrastructure is provisioned using Terraform.

### 🏗️ Infrastructure Components

Resources Created
✅ Amazon VPC
✅ Public Subnets
✅ Private Subnets
✅ Internet Gateway
✅ NAT Gateway
✅ Route Tables
✅ Security Groups
✅ EC2 Instances
✅ Amazon RDS MySQL
✅ Amazon S3
✅ Application Load Balancer
✅ IAM Roles
**Resources Created:**
- ✅ Amazon VPC
- ✅ Public Subnets
- ✅ Private Subnets
- ✅ Internet Gateway
- ✅ NAT Gateway
- ✅ Route Tables
- ✅ Security Groups
- ✅ EC2 Instances
- ✅ Amazon RDS MySQL
- ✅ Amazon S3
- ✅ Application Load Balancer
- ✅ IAM Roles
## ⚙ Technology Stack
| Category | Technologies |
|---|---|
| Database | MySQL, Amazon RDS |
| Containerization | Docker |
| Container Orchestration | Kubernetes |
| CI/CD | Jenkins |
| Infrastructure as Code | Terraform |
| Configuration Management | Ansible |
| Cloud Platform | AWS |
| Monitoring | Prometheus, Grafana |
| Image Registry | Docker Hub |
| Version Control | Git & GitHub |
## ☁️ AWS Services Used
- Amazon EC2
- Amazon RDS (MySQL)
- Amazon VPC
- Public & Private Subnets
- Internet Gateway
- NAT Gateway
- Route Tables
- Security Groups
- Application Load Balancer
- IAM
- Amazon S3
- ☁️ Amazon EC2
- ☁️ Amazon RDS (MySQL)
- ☁️ Amazon VPC
- ☁️ Public & Private Subnets
- ☁️ Internet Gateway
- ☁️ NAT Gateway
- ☁️ Route Tables
- ☁️ Security Groups
- ☁️ Application Load Balancer
- ☁️ IAM
- ☁️ Amazon S3
## 📂 Repository Structure
```text
enterprise-devops-platform/
│
├── Src/                          # Flask Application
│   ├── app/
│   ├── migrations/
│   ├── requirements.txt
│   └── run.py
│
├── terraform/                    # Infrastructure as Code
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
├── ansible/                      # Configuration Management
│   ├── playbook.yml
│   └── inventory/
│
├── k8s/                          # Kubernetes Manifests
│   ├── deployment.yaml
│   └── service.yaml
│
├── Dockerfile
├── Jenkinsfile
├── README.md
└── .gitignore
```
## ✨ Key Features
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
- ✅ End-to-End CI/CD Pipeline using Jenkins
- ✅ Infrastructure Provisioning using Terraform
- ✅ Configuration Management using Ansible
- ✅ Dockerized Flask Application
- ✅ Docker Hub Image Repository
- ✅ Kubernetes Deployments
- ✅ Rolling Updates
- ✅ Self-Healing Pods
- ✅ Replica Management
- ✅ Amazon RDS Integration
- ✅ Amazon S3 Integration
- ✅ Application Load Balancer
- ✅ Public & Private Networking
- ✅ Secure Security Groups
- ✅ Infrastructure Automation
- ✅ Production-style DevOps Workflow
- ✅ Monitoring Ready with Prometheus & Grafana
## 🐳 Docker
### Build Image
```bash
docker build -t prayag1/enterprise-devops-platform:latest .
```
### Login to Docker Hub
```bash
docker login
```
### Push Image
```bash
docker push prayag1/enterprise-devops-platform:latest
```
### Run Container
```bash
docker run -d \
  -p 5000:5000 \
  --name devops-platform \
  prayag1/enterprise-devops-platform:latest
```
## ☸ Kubernetes
### Deploy Application
```bash
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
```
### Check Pods
```bash
kubectl get pods
```
### Check Services
```bash
kubectl get svc
```
### Scale Application
```bash
kubectl scale deployment enterprise-devops-platform --replicas=5
```
### Rolling Update
```bash
kubectl set image deployment/enterprise-devops-platform \
  enterprise-devops-platform=prayag1/enterprise-devops-platform:latest
```
## 🌍 Terraform
### Initialize
```bash
cd terraform
terraform init
```
### Plan
```bash
terraform plan
```
### Apply
```bash
terraform apply -auto-approve
```
### Destroy
```bash
terraform destroy
```
## ⚙ Ansible
### Run Playbook
```bash
ansible-playbook -i inventory/production playbook.yml
```
### Check Syntax
```bash
ansible-playbook playbook.yml --syntax-check
```
### Dry Run
```bash
ansible-playbook playbook.yml --check
```
## 📊 Monitoring
The platform is designed to integrate with modern monitoring tools.
### Monitoring Stack
- Prometheus - Metrics Collection
- Grafana - Dashboards & Visualization
- Node Exporter - Node Metrics
- cAdvisor - Container Metrics
- 📈 **Prometheus** - Metrics Collection
- 📉 **Grafana** - Dashboards & Visualization
- 🖥️ **Node Exporter** - Node Metrics
- 🐳 **cAdvisor** - Container Metrics
### Monitoring Capabilities
- Infrastructure Monitoring
- Container Monitoring
- CPU & Memory Utilization
- Application Health
- Kubernetes Metrics
- Alerting & Dashboards
- 🔍 Infrastructure Monitoring
- 📦 Container Monitoring
- ⚡ CPU & Memory Utilization
- 🏥 Application Health
- ☸️ Kubernetes Metrics
- 🔔 Alerting & Dashboards
## 🔐 Security Features
🔒 Private Amazon RDS
🔒 Security Groups
🔒 IAM Roles
🔒 Private Networking
🔒 Public/Private Subnet Separation
🔒 Least Privilege Access
🔒 Security Group Rules
🔒 Network Isolation
- 🔒 Private Amazon RDS
- 🔒 Security Groups
- 🔒 IAM Roles
- 🔒 Private Networking
- 🔒 Public/Private Subnet Separation
- 🔒 Least Privilege Access
- 🔒 Security Group Rules
- 🔒 Network Isolation
## 📈 Future Enhancements
- Kubernetes Ingress Controller
- Horizontal Pod Autoscaler (HPA)
- Helm Charts
- AWS EKS Deployment
- ArgoCD GitOps
- SonarQube Integration
- Trivy Image Scanning
- AWS CloudWatch Logs
- Prometheus Alert Manager
- SSL/TLS using AWS ACM
- Route53 DNS
- Blue-Green Deployment
- Canary Deployment
- 🚀 Kubernetes Ingress Controller
- 🔄 Horizontal Pod Autoscaler (HPA)
- 📦 Helm Charts
- ☁️ AWS EKS Deployment
- 🔄 ArgoCD GitOps
- 🔍 SonarQube Integration
- 🛡️ Trivy Image Scanning
- 📝 AWS CloudWatch Logs
- 🔔 Prometheus Alert Manager
- 🔐 SSL/TLS using AWS ACM
- 🌐 Route53 DNS
- 🔵🟢 Blue-Green Deployment
- 🐤 Canary Deployment
## 🎯 Learning Outcomes
This project demonstrates practical experience with:
☁️ AWS Cloud
🔄 DevOps Practices
🏗️ Infrastructure as Code
🔄 Continuous Integration
🚀 Continuous Deployment
🐳 Docker
☸ Kubernetes
🌍 Terraform
⚙️ Jenkins
🐙 GitHub
🐧 Linux Administration
🌐 Cloud Networking
📊 Monitoring & Observability
🔐 Security Best Practices
- ☁️ AWS Cloud
- 🔄 DevOps Practices
- 🏗️ Infrastructure as Code
- 🔄 Continuous Integration
- 🚀 Continuous Deployment
- 🐳 Docker
- ☸ Kubernetes
- 🌍 Terraform
- ⚙️ Jenkins
- 🐙 GitHub
- 🐧 Linux Administration
- 🌐 Cloud Networking
- 📊 Monitoring & Observability
- 🔐 Security Best Practices
---
## 👨💻 Author

**Prayag Dutt**

## 🤝 Let's Connect!

<div align="center">
  <p style="color: #8b949e; max-width: 550px; margin: 0 auto 25px;">
    Always open to collaborations, DevOps discussions, or just a friendly chat. 
    Let's build something amazing together! 🚀
  </p>

  <div style="display: flex; justify-content: center; gap: 15px; flex-wrap: wrap;">
    <a href="https://github.com/Prayag762"><img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white"/></a>
    <a href="https://linkedin.com/in/prayag-dutt"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white"/></a>
    <a href="mailto:prayag.dutt@email.com"><img src="https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white"/></a>
  </div>

  <br />

  <div style="padding: 15px 20px; background: rgba(54, 188, 247, 0.05); border-radius: 10px; border-left: 3px solid #36BCF7;">
    <p style="margin: 0; color: #c9d1d9;">
      ⭐ <strong style="color: #36BCF7;">Star this repo</strong> if you found it valuable — it helps others discover this project!
    </p>
  </div>

  <br />

  <p style="color: #8b949e; font-size: 0.85rem;">
    Made with ☕ and ❤️ using DevOps
  </p>
</div>

---

<div align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&height=100&section=footer" width="100%" />
</div>

<div align="center">
  <b style="background: linear-gradient(135deg, #667eea, #764ba2); -webkit-background-clip: text; -webkit-text-fill-color: transparent; font-size: 1.1rem;">
    ⭐ If this project helped you, don't forget to star the repository! ⭐
  </b>
</div>
