import sys
import os
from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from starlette.responses import Response
import uvicorn
from mobilePriceRangePrediction.pipeline.prediction import PredictionPipeline

app = FastAPI()

@app.get("/", tags=["authentication"])
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
async def predict_route(data):
    try:
        obj = PredictionPipeline()
        pred = obj.predict(data)
        return pred
    except Exception as e:
        raise e
    
if __name__=="__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
