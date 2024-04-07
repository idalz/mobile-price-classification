import os

import uvicorn
from fastapi import FastAPI
from fastapi import HTTPException
from fastapi.responses import RedirectResponse

from starlette.responses import Response

import pandas as pd

from mobilePriceRangePrediction.utils.common import classify_prediction
from mobilePriceRangePrediction.pipeline.prediction import PredictionPipeline
from mobilePriceRangePrediction.entity import PredictionRequest

app = FastAPI()

@app.get("/")
async def index():
    return RedirectResponse(url="/docs")

@app.get("/train")
async def training():
    try:
        os.system("python main.py")
        return Response("Training was successfull.")
    except Exception as e:
        return Response(f"Error occurred: {e}")
    
@app.post("/predict")
async def predict_route(request: PredictionRequest):
    try:
        # Convert to dataframe
        data = request.model_dump()
        df = pd.DataFrame([data])
        #----------------------
        
        obj = PredictionPipeline()
        pred = obj.predict(df)
        result  = classify_prediction(int(pred))

        return {"prediction": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction error: {e}")

    
if __name__=="__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)

# run using uvicorn app:app --reload 
