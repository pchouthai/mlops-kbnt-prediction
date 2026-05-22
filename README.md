Machine Learning Pipeline using GitHub Actions
Project Title
Flight Duration Prediction System using MLOps Pipeline with GitHub Actions
________________________________________
Project Overview
This project implements an end-to-end MLOps pipeline for flight duration prediction using GitHub Actions, Docker, Flask API, and Kubernetes deployment.
The system automates:
•	Data preprocessing
•	Model training
•	Continuous Integration (CI)
•	Continuous Delivery (CD)
•	Continuous Training (CT)
•	Kubernetes deployment
•	Monitoring workflows
The application predicts what will be the flight duration based on distance.
________________________________________
Architecture
The project architecture follows the MLOps lifecycle:
Dataset
↓
Preprocessing Pipeline
↓
Model Training & Evaluation
↓
Flask REST API
↓
Docker Containerization
↓
GitHub Actions CI/CD
↓
Kubernetes Deployment
↓
Continuous Monitoring & Retraining
________________________________________
Technologies Used
Technology	Purpose
Python	Machine Learning & API
Flask	REST API
Scikit-learn	ML Model
Pandas	Data Processing
Docker	Containerization
GitHub Actions	CI/CD Automation
Kubernetes	Deployment
GitHub Codespaces	Development Environment
________________________________________
Repository Structure
mlops-kbnt-prediction/
│
├── .github/workflows/
├── data/raw/
├── data/processed/
├── models/
├── src/
├── tests/
├── k8s/
├── Dockerfile
├── app.py
├── requirements.txt
└── README.md
________________________________________
Setup Steps
1. Clone Repository
git clone <repository-url>
cd mlops-kbnt-prediction
________________________________________
2. Create Virtual Environment
python -m venv venv
source venv/bin/activate
________________________________________
3. Install Dependencies
pip install -r requirements.txt
________________________________________
4. Run Preprocessing
python src/preprocess.py
________________________________________
5. Train Model
python src/train.py
________________________________________
6. Run Flask API
python app.py
________________________________________
Docker Setup
Build Docker Image
docker build -t kbnt-api .
________________________________________
Run Docker Container
docker run -p 5000:5000 kbnt-api
________________________________________
GitHub Actions Workflows
Workflow	Purpose
Preprocessing	Automates data preprocessing
Training	Automates model training
CI	Runs automated integration checks
Retraining	Performs continuous training
Kubernetes Deployment	Deploys application to Kubernetes
Kubernetes Monitor	Monitors Kubernetes deployment
________________________________________
Deployment
The application is deployed using:
•	Docker containers
•	Kubernetes cluster
•	GitHub Actions automation
Deployment process:
1.	GitHub Actions builds Docker image.
2.	Image is pushed to DockerHub.
3.	Kubernetes deployment workflow updates cluster.
4.	Flask API becomes accessible through Kubernetes service.
________________________________________
Branching Strategy
The project follows a simplified Git workflow:
Branch	Purpose
main	Production-ready code
feature/*	Feature development
Feature branches are merged into the main branch after validation through GitHub Actions workflows.
________________________________________
Conclusion
This project demonstrates a complete MLOps implementation using:
•	CI/CD pipelines
•	Docker containerization
•	Kubernetes deployment
•	Automated retraining workflows
The system automates the machine learning lifecycle from preprocessing to production deployment.
________________________________________
