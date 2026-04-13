# 🧠 AI-Based Disease Prediction System Using Clinical Data

## 📌 Project Overview

This project is developed as part of the **CDAC DBDA (Diploma in Big Data Analytics)** course.
The goal is to design and implement a **machine learning-based system** that predicts the likelihood of a disease using patient clinical data.

The system uses **Python-based technologies**, combining:
- Machine Learning (Scikit-learn)
- Backend APIs (FastAPI)
- Frontend Interface (Streamlit)
- Database (SQLite)

It provides a **simple, scalable, and practical healthcare decision-support tool**.

---

## 🎯 Motivation & Purpose

Healthcare systems often require **early disease detection** to improve treatment outcomes. However:
- Manual diagnosis can be time-consuming
- Access to expert doctors is limited in many areas
- Patients may ignore early symptoms

This project aims to:
- Provide **quick preliminary disease prediction**
- Assist doctors with **data-driven insights**
- Enable users to **check risk levels easily**

---

## 🚀 What This Project Does

✔ Accepts clinical input data (e.g., glucose, BMI, age)  
✔ Uses a trained machine learning model  
✔ Predicts disease likelihood (currently Diabetes)  
✔ Displays results through an interactive UI  
✔ Provides a backend API for integration  
✔ Stores structure for future database logging  

---

## 🏗️ Project Architecture
User (Streamlit UI)

↓

Frontend (Streamlit)

↓

Backend API (FastAPI)

↓

ML Model (Scikit-learn)

↓

Database (SQLite - optional)

---

## 📂 Project Structure
ai-disease-prediction-system/

│

├── ml/ # Machine Learning logic

├── models/ # Saved trained models

├── backend/ # FastAPI backend

├── frontend/ # Streamlit UI

├── data/ # Dataset storage

├── database/ # SQL schema

├── tests/ # Basic testing

├── notebooks/ # EDA & experiments

└── reports/ # Documentation & PPT

---

## 🧠 Technologies Used

| Component | Technology |
|----------|------------|
| Language | Python |
| ML Model | Scikit-learn |
| Backend | FastAPI |
| Frontend | Streamlit |
| Database | SQLite |
| Environment | GitHub Codespaces |

---

## 📊 Machine Learning Approach

- Dataset: PIMA Diabetes Dataset  
- Preprocessing:
  - Data cleaning
  - Feature scaling
- Model:
  - Logistic Regression (baseline model)
- Output:
  - Binary classification (Disease / No Disease)

---

## ▶️ How to Run the Project (Codespaces)

### Step 1: Install dependencies
pip install -r requirements.txt

### Step 2: Train the model
python ml/train_model.py

### Step 3: Start backend
cd backend
python run.py

### Step 4: Start frontend
streamlit run frontend/streamlit_app.py --server.port 8501 --server.address 0.0.0.0

---

## 📌 Features Implemented

- ✔ Clean modular project structure  
- ✔ ML model training and prediction  
- ✔ REST API for predictions  
- ✔ Interactive UI for user input  
- ✔ Error handling and validation  
- ✔ GitHub Codespaces compatibility  

---

## 📈 What This Project Achieves

This project demonstrates:

- Practical use of **Machine Learning in Healthcare**
- End-to-end **full-stack AI system development**
- Integration of **ML + API + UI**
- Real-world application of **clinical data analysis**
- Ability to build scalable and modular systems

---

## ⚠️ Limitations (Current Version)

- Supports only one disease (Diabetes)
- Uses a basic ML model (can be improved)
- No authentication system
- Limited dataset size
- Not intended for real medical diagnosis

---

## 🌟 Future Enhancements

This project can be extended significantly:

### 🔹 Technical Improvements
- Add multiple disease prediction models
- Use advanced algorithms (Random Forest, XGBoost)
- Add model explainability (feature importance, SHAP)

### 🔹 System Enhancements
- User login & history tracking
- Cloud deployment (Render / AWS)
- REST API authentication
- Real-time database integration

### 🔹 AI Extensions
- Chatbot for symptom-based prediction
- NLP-based medical report analysis
- Integration with wearable health devices

---

## 👨‍💻 Author

**Yash Wardhan Pandey**  
B.Tech Computer Science Engineering  
CDAC DBDA Student  

---

## 📚 Academic Context

This project is developed as part of the **CDAC DBDA curriculum**, focusing on:
- Machine Learning applications
- Data processing pipelines
- Backend system design
- Real-world problem solving using data

---

## 📌 Disclaimer

This system is intended for **educational and demonstration purposes only**.  
It should **not be used for actual medical diagnosis or treatment decisions**.

---

## ⭐ Acknowledgements

- UCI Machine Learning Repository  
- Scikit-learn Documentation  
- CDAC DBDA Program Guidance  

---
