                                **Enterprise DevOps Task Management Platform**                                      
																        
																				
												**Project Overview**

The Enterprise DevOps Task Management Platform is a cloud-native, production-ready web application developed to demonstrate a complete DevOps lifecycle using modern tools and AWS cloud services. The project automates application deployment, infrastructure provisioning, monitoring, and scaling through an end-to-end CI/CD pipeline.

The application is built using Python Flask with a MySQL database (Amazon RDS in production) and is fully containerized using Docker. Source code is maintained in GitHub, while Jenkins automates the build, test, Docker image creation, and deployment process. Docker images are stored in Docker Hub.

Infrastructure is provisioned using Terraform, enabling Infrastructure as Code (IaC) for AWS resources including VPCs, subnets, EC2 instances, Amazon RDS, Application Load Balancers, IAM roles, and Amazon S3.

Application configuration and software installation are automated using Ansible, while Kubernetes manages container orchestration, rolling deployments, auto-healing, and horizontal pod autoscaling.

The platform is deployed across two AWS regions connected through VPC Peering, providing high availability and disaster recovery capabilities.



## Enterprise DevOps Platform Architecture

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
classDef aws fill:#ede7f6,stroke:#5e35b1,stroke-width:2px,color:#311b92
classDef compute fill:#fce4ec,stroke:#c2185b,stroke-width


