# VII – Machine Learning and Operations Lab

## Laboratory Experiments

This repository contains the practical experiments performed as part of the **VII – Machine Learning and Operations Lab**.

The experiments provide hands-on experience with software version control, continuous integration and delivery, machine learning experiment tracking, model lifecycle management, containerization, and web application CI/CD.

---


## Course Overview

Machine Learning Operations (MLOps) combines machine learning development with software engineering and operational practices to make machine learning systems reliable, reproducible, maintainable, and deployable.

This laboratory focuses on the fundamental tools and workflows used in an MLOps environment.

The experiments progressively introduce the major stages of an MLOps and DevOps workflow:

```text
Version Control
       ↓
CI/CD Automation
       ↓
Experiment Tracking
       ↓
Model Registry
       ↓
Containerization
       ↓
Web Application CI/CD
```

---

## Overall Experiment Structure

| Experiment | Title | Primary Tool / Technology | Main Concept |
|---|---|---|---|
| Ex 1 | Exploring Git Commands Through Collaborative Coding | Git, GitHub | Version Control |
| Ex 2 | Implementing a CI/CD Pipeline with Jenkins | Jenkins, Maven, GitHub | Continuous Integration and Delivery |
| Ex 3 | Experiment Tracking Using MLflow | MLflow | Experiment Tracking |
| Ex 4 | MLflow Model Registry | MLflow | Model Versioning and Lifecycle Management |
| Ex 5 | Exploring Containerization and Application Deployment with Docker | Docker Desktop | Containerization |
| Ex 6 | Applying CI/CD Principles to Web Development Using Jenkins, Git, and Local HTTP Server | Jenkins, Git, GitHub, Python | Web Application CI/CD |

---

## Experiment 1 – Exploring Git Commands Through Collaborative Coding

### Objective

To explore and practice Git commands used for version control, repository management, branching, committing changes, and collaboration with GitHub.

### Key Concepts

- Git repository management
- Working directory
- Staging area
- Commits
- Branches
- Remote repositories
- GitHub
- Push and pull operations
- Version control workflow

### Outcome

The basic Git workflow was implemented and practiced by creating a repository, tracking changes, committing files, working with branches, connecting the repository with GitHub, and pushing changes to the remote repository.

---

## Experiment 2 – Implementing a CI/CD Pipeline with Jenkins

### Objective

To implement a Continuous Integration and Continuous Delivery (CI/CD) pipeline using Jenkins for automatically building and testing a Maven-based Java application.

### Key Concepts

- Jenkins
- Continuous Integration
- Continuous Delivery
- GitHub integration
- Maven
- Automated builds
- Automated testing
- Jenkins Pipeline

### Outcome

A Jenkins-based CI/CD pipeline was successfully configured and connected with a GitHub repository.

The Maven application was successfully built and tested through Jenkins, producing a successful build result.

---

## Experiment 3 – Experiment Tracking Using MLflow

### Objective

To understand and implement experiment tracking using MLflow by creating experiments, recording parameters and metrics, and viewing experiment results through the MLflow UI.

### Key Concepts

- MLflow
- Experiment tracking
- MLflow runs
- Parameters
- Metrics
- Artifacts
- MLflow UI
- Experiment comparison

### Outcome

MLflow was successfully installed and configured.

An experiment and run were created, parameters and metrics were recorded, and the experiment results were viewed through the MLflow UI.

---

## Experiment 4 – MLflow Model Registry

### Objective

To understand and implement MLflow Model Registry for registering, versioning, managing, and tracking machine learning models throughout their lifecycle.

### Key Concepts

- MLflow Model Registry
- Model registration
- Model versions
- Model metadata
- Model tags
- Model lifecycle management
- MLflow UI
- Model management using the MLflow SDK

### Outcome

A machine learning model was successfully registered using MLflow Model Registry.

Model versions and associated metadata were managed and viewed through the MLflow interface.

---

## Experiment 5 – Exploring Containerization and Application Deployment with Docker

### Objective

To understand and practice Docker containerization by installing and verifying Docker, managing Docker images and containers, deploying an Nginx web server, practicing Docker commands, creating Dockerfiles, building and running custom Docker images, working with Docker volumes and networking, and deploying a Python web application using Docker.

### Key Concepts

- Docker Desktop
- Docker Engine
- Docker Compose
- Docker images
- Docker containers
- Dockerfiles
- Docker volumes
- Docker networking
- Nginx
- Python application containerization
- Port mapping
- Docker image export and import

### Outcome

Docker was successfully installed and verified on Windows.

Docker images and containers were successfully managed using Docker commands.

Nginx was deployed and accessed through a browser.

Custom Docker images were created and executed.

Docker volumes and networking were explored.

A Python web application was successfully containerized and deployed.

Docker image export and import using `.tar` files were also demonstrated.

---

## Experiment 6 – Applying CI/CD Principles to Web Development Using Jenkins, Git, and Local HTTP Server

### Objective

To implement and demonstrate Continuous Integration and Continuous Deployment (CI/CD) principles for a web application using Git, GitHub, Jenkins, and a local Python HTTP server.

### Key Concepts

- Git
- GitHub
- Version Control
- Jenkins
- CI/CD
- Jenkins Pipeline
- HTML
- CSS
- JavaScript
- Python HTTP Server
- Automated validation
- Automated testing
- Automated deployment
- Application versioning

### Experiment Description

A static web application was developed using HTML, CSS, and JavaScript.

Git was used to maintain the source code under version control, while GitHub was used as the remote repository.

Jenkins was configured to obtain the application source code and execute a CI/CD pipeline.

The Jenkins pipeline consisted of the following stages:

```text
Checkout
   ↓
Validate
   ↓
Test
   ↓
Deploy
```

The application was deployed using Python's built-in HTTP server and verified through a web browser.

Two application versions were implemented.

Version 1 demonstrated the initial CI/CD workflow.

Version 2 demonstrated application modification, Git version control, committing changes, pushing the updated version to GitHub, and processing the updated source code through Jenkins.

### Outcome

The web application was successfully integrated with Git, GitHub, and Jenkins.

Jenkins successfully checked out the source code, validated the application files, tested the HTML, CSS, and JavaScript files, and deployed the application using a local Python HTTP server.

Version 2 was successfully created, committed, and pushed to GitHub.

The updated application was successfully integrated into the CI/CD workflow.

The application was successfully accessed through:

```text
http://localhost:8000
```

The Jenkins pipeline completed successfully with:

```text
Finished: SUCCESS
```

---

## Overall MLOps Workflow

The completed experiments demonstrate the following overall workflow:

```text
┌──────────────────────────────┐
│        Git / GitHub          │
│       Version Control        │
└──────────────┬───────────────┘
               │
               ↓
┌──────────────────────────────┐
│           Jenkins            │
│        CI/CD Pipeline        │
└──────────────┬───────────────┘
               │
               ↓
┌──────────────────────────────┐
│           MLflow             │
│      Experiment Tracking     │
└──────────────┬───────────────┘
               │
               ↓
┌──────────────────────────────┐
│     MLflow Model Registry    │
│   Model Version Management   │
└──────────────┬───────────────┘
               │
               ↓
┌──────────────────────────────┐
│           Docker             │
│       Containerization       │
└──────────────┬───────────────┘
               │
               ↓
┌──────────────────────────────┐
│      Web Application CI/CD   │
│   Jenkins + Git + HTTP      │
│           Server             │
└──────────────────────────────┘
```

---

## Technologies Covered

| Category | Technologies |
|---|---|
| Version Control | Git, GitHub |
| CI/CD | Jenkins |
| Build Automation | Apache Maven |
| Programming | Python, Java, HTML, CSS, JavaScript |
| Experiment Tracking | MLflow |
| Model Management | MLflow Model Registry |
| Containerization | Docker |
| Container Platform | Docker Desktop |
| Web Server | Python HTTP Server, Nginx |
| Development Environment | Visual Studio Code |
| Operating System | Windows, WSL |

---

## Learning Outcomes

After completing these experiments, the following practical skills were developed:

- Understanding Git-based version control.
- Managing source code using GitHub.
- Creating and managing branches.
- Performing commits, pushes, and pulls.
- Understanding Continuous Integration and Continuous Delivery.
- Configuring Jenkins for automated builds.
- Integrating GitHub with Jenkins.
- Building and testing Maven-based applications.
- Creating Jenkins Pipeline workflows.
- Tracking machine learning experiments using MLflow.
- Recording parameters and metrics.
- Managing machine learning models using MLflow Model Registry.
- Understanding model versioning and metadata.
- Installing and configuring Docker Desktop.
- Working with Docker images and containers.
- Creating and using Dockerfiles.
- Working with Docker volumes and networks.
- Containerizing Python applications.
- Deploying web applications using Docker.
- Understanding Git-based web application CI/CD.
- Validating and testing web application source files through Jenkins.
- Deploying a web application using a local HTTP server.
- Maintaining application versions using Git.
- Integrating updated application versions into a Jenkins pipeline.

---

## Repository Structure

The repository is organized according to the laboratory experiments.

| Directory | Description |
|---|---|
| `Ex 1` | Git and GitHub version control experiment |
| `Ex 2` | Jenkins CI/CD pipeline experiment |
| `Ex 3` | MLflow experiment tracking |
| `Ex 4` | MLflow Model Registry |
| `Ex 5` | Docker containerization and application deployment |
| `Ex 6` | Web application CI/CD using Jenkins, Git, and local HTTP server |

Each experiment contains its own README file describing the objective, software used, procedure, verification, output, result, and conclusion.

---

## Final Result

All six laboratory experiments were successfully completed.

The laboratory provided practical exposure to core tools and workflows used in MLOps and DevOps, beginning with source-code management and progressing through CI/CD automation, machine learning experiment tracking, model lifecycle management, containerization, and web application deployment.

The completed experiments establish a strong foundation for implementing more advanced MLOps and DevOps workflows involving containerized CI/CD, Kubernetes orchestration, cloud deployment, deployment strategies, monitoring, and application security testing.

---

## Author

**Kamalesh Suresh Kumar**
