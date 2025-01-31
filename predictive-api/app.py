from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sklearn.tree import DecisionTreeClassifier
import numpy as np

app = FastAPI()

model = DecisionTreeClassifier()
X_train = np.array([[1], [2], [3], [4], [5]])
y_train = np.array([0,1,1,0,1])
model.fit(X_train, y_train)

class PredictionRequest(BaseModel):
    input_value: float

@app.get("/")
def root():
    return {"message": "Welcome to the Decision Tree Classifier API!"}

@app.post("/predict/")
def predict(request: PredictionRequest):
    try:
        input_array = np.array([[request.input_value]])
        prediction = model.predict(input_array)
        return {"input": request.input_value, "prediction": int(prediction[0])}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
