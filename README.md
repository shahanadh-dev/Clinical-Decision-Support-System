# 🩺 Clinical Decision Support System

An AI-powered Clinical Decision Support System (CDSS) developed using Django and Machine Learning to assist healthcare professionals with respiratory disease risk assessment through an intuitive, mobile-friendly web interface.

---

## Overview

The Clinical Decision Support System is a healthcare-focused web application that combines machine learning with clinical data collection to generate preliminary respiratory risk assessments. The system enables healthcare professionals to input patient demographics, clinical parameters, and medical history through a responsive interface and receive predictive insights to support clinical decision-making.

---

## Features

- AI-powered respiratory risk assessment
- Mobile-friendly responsive web interface
- Patient demographic management
- Clinical parameter analysis
- Medical history integration
- Multiple Machine Learning models (SVM & KNN)
- Real-time prediction results
- Modular Django architecture

---

## Tech Stack

### Backend
- Python
- Django

### Machine Learning
- Scikit-learn
- Pandas
- NumPy

### Frontend
- HTML5
- Bootstrap 5
- CSS3

### Database
- SQLite

### Development
- Git
- VS Code

---

## System Workflow

Patient Information

↓

Clinical Parameters

↓

Medical History

↓

Data Preprocessing

↓

Machine Learning Model

↓

Clinical Risk Assessment

↓

Decision Support Report

---

## Project Structure

```
clinical-decision-support-system
│
├── dataset/
├── app/
│   ├── basics/
│   ├── GUI/
│   ├── manage.py
│   └── requirements.txt
│
├── docs/
└── README.md
```

---

## Machine Learning Pipeline

- Clinical Data Collection
- Data Preprocessing
- Feature Engineering
- Model Training
- Model Evaluation
- Respiratory Risk Prediction
- Clinical Decision Support

---

## Installation

```bash
git clone https://github.com/shahanadh-dev/clinical-decision-support-system.git
```

```bash
cd clinical-decision-support-system/app
```

```bash
pip install -r requirements.txt
```

```bash
python manage.py runserver
```

Open:

```
http://127.0.0.1:8000
```

---

## Screenshots

Include:

- Home Dashboard
- Patient Information Form
- Clinical Parameters Form
- Medical History Section
- Prediction Results
- Mobile Responsive Interface

---

## Future Improvements

- Multi-disease prediction
- Deep Learning models
- Explainable AI (SHAP/LIME)
- REST API integration
- Docker deployment
- Cloud deployment
- Electronic Health Record (EHR) integration
- Role-based authentication

---

## Disclaimer

This project was developed for educational and research purposes only. It is intended to demonstrate the application of Machine Learning in clinical decision support and should not be used as a substitute for professional medical diagnosis.
