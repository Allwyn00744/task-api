import joblib

model=joblib.load("priority_model.pkl")

#test samples
tests = [
    "Fix critical bug",
    "Write documentation",
    "Prepare presentation",
    "Server down issue"
]

for t in tests:
    result=model.predict([t])[0]
    print(f"{t} -> {result} ")