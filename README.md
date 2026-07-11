# Enterprise DevOps Task Management Platform

## Project Overview

The **Enterprise DevOps Task Management Platform** is a cloud-native, production-ready web application built to demonstrate a complete DevOps lifecycle using modern tools and AWS cloud services. The project automates application deployment, infrastructure provisioning, monitoring, and scaling through an end-to-end CI/CD pipeline.

The application is built using **Python Flask** with a **MySQL** database (**Amazon RDS** in production) and is fully containerized using **Docker**. Source code is maintained in **GitHub**, while **Jenkins** automates the build, test, Docker image creation, and deployment process. Docker images are stored in **Docker Hub**.

Infrastructure is provisioned using **Terraform**, enabling Infrastructure as Code (IaC) for AWS resources including VPCs, subnets, EC2 instances, Amazon RDS, Application Load Balancers, IAM roles, and Amazon S3.

Application configuration and software installation are automated using **Ansible**, while **Kubernetes** manages container orchestration, rolling deployments, auto-healing, and horizontal pod autoscaling.

The platform is deployed across **two AWS regions** connected through **VPC Peering**, providing high availability and disaster recovery capabilities.

---

## Architecture Diagram

```mermaid
flowchart LR

A(["👨‍💻 Developer"]) -->|Git Push| B["🐙 GitHub Repository"]
B -->|Webhook| C["⚙️ Jenkins CI/CD"]
C -->|Build Image| D["🐳 Docker Build"]
D -->|Push Image| E["📦 Docker Hub"]
C -->|Deploy Latest| F["🐳 Docker Container on EC2"]

subgraph AWS["☁️ AWS Cloud"]
    direction LR
    subgraph VPC["🔒 VPC"]
        direction LR
        subgraph Public["🌐 Public Subnet"]
            G["🖥️ Application EC2"]
        end
        subgraph Private["🔐 Private Subnet"]
            H[("🗄️ Amazon RDS - MySQL")]
        end
        M{{"🛡️ Security Groups"}}
    end
    I["🪣 S3 Bucket"]
end

F --> G
G --> H
G --> I
M -.-> G
M -.-> H
User(["🌍 Browser User"]) -->|HTTP :5000| G

classDef dev fill:#e1f5fe,stroke:#0288d1,stroke-width:2px,color:#01579b
classDef ci fill:#fff3e0,stroke:#f57c00,stroke-width:2px,color:#e65100
classDef docker fill:#e8f5e9,stroke:#388e3c,stroke-width:2px,color:#1b5e20
classDef compute fill:#fce4ec,stroke:#c2185b,stroke-width:2px,color:#880e4f
classDef storage fill:#fff9c4,stroke:#fbc02d,stroke-width:2px,color:#f57f17
classDef security fill:#ffebee,stroke:#d32f2f,stroke-width:2px,color:#b71c1c
classDef user fill:#e0f2f1,stroke:#00796b,stroke-width:2px,color:#004d40

class A dev
class B,C ci
class D,E,F docker
class G compute
class H,I storage
class M security
class User user
```

---

## Technology Stack

| Category | Tools |
|---|---|
| **Application** | Python, Flask |
| **Database** | MySQL, Amazon RDS |
| **Containerization** | Docker |
| **Orchestration** | Kubernetes (Deployments, Services, HPA) |
| **CI/CD** | Jenkins |
| **Infrastructure as Code** | Terraform |
| **Configuration Management** | Ansible |
| **Cloud Provider** | AWS (EC2, RDS, S3, VPC, ALB, IAM) |
| **Networking** | VPC Peering (multi-region), Public/Private Subnets |
| **Version Control** | Git, GitHub |

---

## Key Features

- ✅ **Infrastructure as Code** — full AWS environment provisioned via Terraform
- ✅ **CI/CD Pipeline** — automated build, test, and deploy with Jenkins
- ✅ **Containerization** — Dockerized Flask application, images pushed to Docker Hub
- ✅ **Configuration Management** — automated server setup and app config via Ansible
- ✅ **Container Orchestration** — Kubernetes-managed deployments with rolling updates, auto-healing, and horizontal pod autoscaling
- ✅ **High Availability** — multi-region AWS deployment connected via VPC Peering
- ✅ **Secure Networking** — public/private subnet separation with dedicated security groups
- ✅ **Managed Database** — Amazon RDS (MySQL) in a private subnet
- ✅ **Static Asset Storage** — Amazon S3

---

## How It Works

1. A developer pushes code to the **GitHub** repository.
2. A **webhook** triggers the **Jenkins** pipeline.
3. Jenkins checks out the code, runs tests, and builds a **Docker image**.
4. The image is pushed to **Docker Hub**.
5. Jenkins deploys the latest image to the **Application EC2 instance** inside AWS.
6. The Flask app connects to **Amazon RDS** for data and **Amazon S3** for static assets.
7. **Security Groups** control traffic between the application, database, and internet.
8. End users access the app over HTTP through the public subnet.

---

## Docker

### Build the image

```bash
docker build -t prayag1/enterprise-devops-platform:tagname .
```

### Push to Docker Hub

```bash
docker login
docker push prayag1/enterprise-devops-platform:tagname
```

### Run the container locally

```bash
docker run -d -p 5000:5000 --name devops-platform prayag1/enterprise-devops-platform:tagname
```

> Replace `tagname` with a version tag (e.g. `v1.0`, `latest`) each time you build and push a new image. Jenkins uses this same image in the CI/CD pipeline to deploy the latest build to EC2 / Kubernetes.

---

## Repository Structure

```
.
├── app/                # Flask application source code
├── terraform/          # Infrastructure as Code (AWS resources)
├── ansible/             # Configuration management playbooks
├── k8s/                 # Kubernetes manifests (Deployment, Service, HPA)
├── Jenkinsfile          # CI/CD pipeline definition
├── Dockerfile           # Container build definition
├── requirements.txt     # Python dependencies
└── README.md
```
