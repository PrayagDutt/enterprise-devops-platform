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

## 📖 Project Overview

The **Enterprise DevOps Task Management Platform** demonstrates a complete DevOps lifecycle from infrastructure provisioning to application deployment using modern DevOps tools and AWS cloud services.

The application is built using **Python Flask** with **Amazon RDS MySQL** as the backend database. Infrastructure is provisioned using **Terraform**, containerized using **Docker**, and deployed automatically through **Jenkins CI/CD**. Kubernetes deployment manifests are included to demonstrate container orchestration and production deployment readiness.

The project follows enterprise DevOps practices including Infrastructure as Code, automated deployments, containerization, and cloud-native architecture.

---

## 🏗 Architecture Diagram

```mermaid
flowchart TB
    subgraph Dev["👨‍💻 Development"]
        Developer["Developer"]
    end

    subgraph CI["🔄 CI/CD Pipeline"]
        GitHub["📦 GitHub Repository"]
        Jenkins["⚙️ Jenkins CI/CD"]
        DockerBuild["🐳 Build Docker Image"]
        DockerPush["📤 Push to Docker Hub"]
    end

    subgraph K8s["☸ Kubernetes Cluster (AWS EC2)"]
        subgraph Control["Control Plane"]
            API["API Server"]
            Scheduler["Scheduler"]
        end
        
        subgraph Workers["Worker Nodes"]
            Pod1["Pod 1<br/>(App Instance)"]
            Pod2["Pod 2<br/>(App Instance)"]
            Pod3["Pod 3<br/>(App Instance)"]
        end
        
        Service["🔄 Kubernetes Service"]
    end

    subgraph AWS["☁️ AWS Cloud"]
        ALB["⚖️ Application<br/>Load Balancer"]
        
        subgraph Database["🗄️ Database"]
            RDS["Amazon RDS MySQL"]
        end
        
        subgraph Storage["📁 Storage"]
            S3["Amazon S3"]
        end
        
        subgraph IaC["🏗️ Infrastructure"]
            Terraform["Terraform"]
            Ansible["Ansible"]
        end
    end

    subgraph Monitoring["📊 Monitoring"]
        Prometheus["📈 Prometheus"]
        Grafana["📉 Grafana"]
    end

    Developer -->|Git Push| GitHub
    GitHub -->|Webhook Trigger| Jenkins
    Jenkins -->|Checkout Code| GitHub
    Jenkins -->|Build| DockerBuild
    DockerBuild -->|Push| DockerPush
    DockerPush -->|Deploy| K8s
    
    K8s -->|Expose| Service
    Service -->|Route Traffic| ALB
    ALB -->|User Access| Developer
    
    K8s -->|Store Data| RDS
    K8s -->|Store Files| S3
    
    Terraform -->|Provision| AWS
    Ansible -->|Configure| K8s
    
    K8s -->|Scrape Metrics| Prometheus
    Prometheus -->|Visualize| Grafana

    style Dev fill:#e3f2fd,stroke:#1565c0
    style CI fill:#f3e5f5,stroke:#6a1b9a
    style K8s fill:#e8f5e9,stroke:#2e7d32
    style Control fill:#fff3e0,stroke:#e65100
    style Workers fill:#fce4ec,stroke:#c62828
    style AWS fill:#e8f5e9,stroke:#2e7d32
    style Database fill:#fff8e1,stroke:#f57f17
    style Storage fill:#e0f7fa,stroke:#00695c
    style IaC fill:#f3e5f5,stroke:#7b1fa2
    style Monitoring fill:#e0f7fa,stroke:#00695c
