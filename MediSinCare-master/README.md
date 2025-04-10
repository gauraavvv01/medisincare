# MediSinCare

## Overview
MediSinCare is a Flask-based web application that predicts diseases based on user symptoms using a logistic regression model and provide prevention recommendations. It integrates Firebase authentication and Firestore for user management and feedback collection.

## Features
- **User Authentication** (Login, Logout) via Firebase
- **Disease Prediction** using a trained Logistic Regression model
- **Personalized Recommendations** for diagnosed diseases
- **Feedback Collection** stored in Firestore
- **Multi-Page Navigation** including About Us, Diet, and Main sections

## Technologies Used
- **Flask** (Backend Framework)
- **Firebase Authentication & Firestore** (User management & database)
- **Joblib** (Machine Learning Model Serialization)
- **Scikit-learn** (Machine Learning - Logistic Regression)
- **Jinja2** (Templating Engine for Flask)

## Installation

### Prerequisites
Make sure you have the following installed:
- Python (>=3.7)
- pip (Python package manager)
- Git (optional)

### Steps
1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/Disease-Prediction.git
   cd Disease-Prediction
   ```

2. **Create a virtual environment (Optional but recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # For Linux/macOS
   venv\Scripts\activate    # For Windows
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   - Create a `.env` file in the project root and add the following:
     ```ini
     FLASK_SECRET_KEY=your_flask_secret_key
     FIREBASE_CREDENTIALS=your_firebase_credentials_json
     FIREBASE_API_KEY=your_firebase_api_key
     FIREBASE_AUTH_DOMAIN=your_firebase_auth_domain
     FIREBASE_PROJECT_ID=your_firebase_project_id
     FIREBASE_STORAGE_BUCKET=your_firebase_storage_bucket
     FIREBASE_MESSAGING_SENDER_ID=your_firebase_messaging_sender_id
     FIREBASE_APP_ID=your_firebase_app_id
     ```

5. **Run the application**
   ```bash
   python app.py
   ```
   The application will be available at `https://medisincare.onrender.com/`.

## API Endpoints

### 1. Firebase Config
**Endpoint:** `/firebase-config`  
**Method:** `GET`
**Response:**
```json
{
  "apiKey": "your_firebase_api_key",
  "authDomain": "your_firebase_auth_domain",
  "projectId": "your_firebase_project_id",
  "storageBucket": "your_firebase_storage_bucket",
  "messagingSenderId": "your_firebase_messaging_sender_id",
  "appId": "your_firebase_app_id"
}
```

### 2. Predict Disease
**Endpoint:** `/form`  
**Method:** `POST`
**Payload:**
```json
{
  "symptom1": 1,
  "symptom2": 0,
  "symptom3": 1
}
```
**Response:**
```json
{
  "disease": "Flu",
  "disease_recommendations": ["Drink warm fluids", "Rest well"]
}
```

### 3. Feedback Submission
**Endpoint:** `/feedback`  
**Method:** `POST`
**Payload:**
```json
{
  "name": "John Doe",
  "email": "john@example.com",
  "rating": "5",
  "recommend": "Yes",
  "comments": "Great experience!"
}
```

## Folder Structure
```
Disease-Prediction/
│── templates/
│   ├── login1.html
│   ├── ques_form.html
│   ├── hospital_main.html
│   ├── abt2.html
│   ├── diet.html
│   ├── feedback_form.html
│   ├── prediction.html
│── static/
│   │── css/
│   ├── images/
│   ├── js/
│── app.py  # Main Flask application
│── if_else_conditions.py  # Disease recommendation logic
│── symptoms.txt  # List of symptoms
│── logistic_model.joblib  # Trained ML model
│── requirements.txt  # Dependencies
│── .env  # Environment variables (not included in repo)
│── README.md  # Project documentation
```

## Contact
For questions or suggestions, feel free to reach out at mridulchawla20@example.com.

## License
This project is licensed under the MIT License.

