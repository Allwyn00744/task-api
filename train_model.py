import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
import joblib

old=pd.read_csv("priority_dataset.csv")

try:
    new=pd.read_csv("retrain_dataset.csv")
    df=pd.concat([old,new],ignore_index=True)
except:
    df=old

# removes spaces
df.columns = df.columns.str.strip()

#inputs/outputs
X=df["title"].str.strip()
y=df["priority"].str.strip().str.lower()

# Build pipeline
model=Pipeline([
    ("vectorizer",CountVectorizer()),
    ("classifier",LogisticRegression(max_iter=1000))
]
)
#Train model
model.fit(X,y)

# Save model 
joblib.dump(model, "priority_model.pkl") 
print("Model trained successfully") 