from flask import Flask, render_template,request,jsonify,session,redirect, url_for
import joblib
from if_else_conditions import recommendations
import firebase_admin
from firebase_admin import credentials, auth, firestore
import os
import json


app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY")

firebase_credentials = json.loads(os.getenv('FIREBASE_CREDENTIALS'))
cred = credentials.Certificate(firebase_credentials)
firebase_admin.initialize_app(cred)
db = firestore.client()

model=joblib.load("logistic_model.joblib")

with open('symptoms.txt', 'r') as file:
    selected_features = [line.strip() for line in file]

@app.route('/firebase-config', methods=['GET'])
def firebase_config():
    return jsonify({
        'apiKey': os.getenv('FIREBASE_API_KEY'),
        'authDomain': os.getenv('FIREBASE_AUTH_DOMAIN'),
        'projectId': os.getenv('FIREBASE_PROJECT_ID'),
        'storageBucket': os.getenv('FIREBASE_STORAGE_BUCKET'),
        'messagingSenderId': os.getenv('FIREBASE_MESSAGING_SENDER_ID'),
        'appId': os.getenv('FIREBASE_APP_ID')
    })

@app.route('/form',methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        symptoms = request.get_json()
        input_vector = [symptoms.get(feature, 0) for feature in selected_features]
        prediction = model.predict([input_vector])
        predicted_disease = prediction[0]
        recommendation=recommendations(predicted_disease)
        if all(value == 0 for value in input_vector):
            return jsonify({'disease': 'No Disease', 'disease_recommendations': []})
        else:
            return jsonify({'disease': predicted_disease, 'disease_recommendations': recommendation})
    return render_template('ques_form.html')

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        uid = request.json.get('uid')  
        if uid:
            session['uid'] = uid
            return jsonify({'message': 'Login successful'}), 200
        return jsonify({'error': 'Invalid UID'}), 400
    return render_template('login1.html')

@app.route('/logout')
def logout():
    session.pop('uid', None)
    return redirect(url_for('login'))

@app.route('/main')
def main():
    if 'uid' not in session:
        return redirect(url_for('login'))
    return render_template('hospital_main.html')

@app.route('/aboutus')
def aboutus():
    if 'uid' not in session:
        return redirect(url_for('login'))
    return render_template('abt2.html')

@app.route('/diet')
def diet():
    if 'uid' not in session:
        return redirect(url_for('login'))
    return render_template('diet.html')

@app.route('/feedback',methods=['GET', 'POST'])
def feedback():
    if 'uid' not in session:
        return redirect(url_for('login'))  # Ensure user is logged in

    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        rating = request.form.get('rating')
        recommend = request.form.get('recommend')
        comments = request.form.get('comments')
        
        user_id = session['uid']  # Get logged-in user's UID
        
        feedback_data = {
            "name": name,
            "email": email,
            "rating": rating,
            "recommend": recommend,
            "comments": comments
        }
        
        # Store feedback under the user's UID in Firestore
        db.collection("feedback").document(user_id).set(feedback_data)
        
        return redirect(url_for('main'))

    return render_template('feedback_form.html') 

@app.route('/predict',methods=['GET'])
def predict():
    if 'uid' not in session:
        return redirect(url_for('login'))
    disease = request.args.get('disease')
    if not disease:
        return redirect(url_for('form'))
    disease_recommendations = recommendations(disease)
    return render_template('prediction.html', disease=disease, disease_recommendations=disease_recommendations)    

if __name__ == '__main__':
    app.run(debug=True)
