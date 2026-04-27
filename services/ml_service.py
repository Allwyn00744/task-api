import joblib

model=joblib.load("priority_model.pkl")

def predict_priority(title: str): 
    prediction = model.predict([title]) 
    return prediction[0] 