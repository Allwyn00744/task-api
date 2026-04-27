# 🚀 AI-Powered Task Management API

## 📌 Overview

This project is a FastAPI-based backend system that allows users to manage tasks with authentication and integrates a Machine Learning model to automatically predict task priority based on the task title.

---

## 🤖 How the Model Works

The priority prediction model is built using a simple NLP pipeline:

* **Text Vectorization**: `CountVectorizer` converts task titles into numerical features.
* **Model**: `LogisticRegression` is used for classification.
* **Pipeline**: Combines vectorizer + classifier for streamlined processing.
* **Input**: Task title (text)
* **Output**: Priority label (`low`, `medium`, `high`)

---

## 🧠 How to Train the Model

### Step 1: Prepare dataset

Dataset format (`priority_dataset.csv`):

```
title,priority
Fix bug,high
Write documentation,low
Prepare report,medium
```

### Step 2: Run training script

```bash
python train_model.py
```

### Step 3: Output

* Trained model saved as: `priority_model.pkl`

---

## ⚙️ How to Run the API

### Step 1: Activate virtual environment

```bash
.venv\Scripts\activate
```

### Step 2: Install dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Start server

```bash
uvicorn main:app --reload
```

### Step 4: Open in browser

```
http://127.0.0.1:8000/docs
```

---

## 🔐 Authentication Flow

1. Register user → `/register`
2. Login → `/login`
3. Copy `access_token`
4. Use token in protected routes:

```
Authorization: Bearer <your_token>
```

---

## 📡 Example API Request/Response

### ➤ Create Task (Auto Priority Prediction)

**Request**

```json
POST /tasks
{
  "title": "Fix critical production bug"
}
```

**Headers**

```
Authorization: Bearer <your_token>
```

**Response**

```json
{
  "title": "Fix critical production bug",
  "priority": "high"
}
```

---

### ➤ Predict Priority (Standalone ML Endpoint)

**Request**

```json
POST /predict-priority
{
  "title": "Prepare meeting slides"
}
```

**Response**

```json
{
  "predicted_priority": "medium"
}
```

---

## 🗂️ Project Structure

```
routes/         → API endpoints
services/       → Business logic (DB + ML)
models.py       → Database models
schemas.py      → Request/response schemas
database.py     → DB connection
utils/          → JWT + hashing
train_model.py  → ML training
test_model.py   → ML testing
```

---

## 🔥 Features

* User Authentication (JWT)
* Task CRUD Operations
* Soft Delete Support
* User-specific tasks
* AI-based priority prediction
* Clean architecture (routes + services)

---

## 🧪 Testing

* Use Postman or Swagger (`/docs`)
* Run:

```bash
python test_model.py
```

---

## 🏁 Tech Stack

* FastAPI
* SQLAlchemy
* SQLite
* Scikit-learn
* JWT Authentication
* Passlib (bcrypt)

---

## 💡 Future Improvements

* Add confidence score for predictions
* Use TF-IDF / advanced models
* Deploy on cloud (Render / AWS)
* Add frontend dashboard

---

## 👨‍💻 Author

Allwyn Jeffo Raj
