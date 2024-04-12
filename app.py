import os

import uvicorn
from fastapi import FastAPI
from fastapi import HTTPException, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse, HTMLResponse
from fastapi.templating import Jinja2Templates

from starlette.responses import Response

import pandas as pd

from mobilePriceRangePrediction.utils.common import classify_prediction
from mobilePriceRangePrediction.constants.html_content import *
from mobilePriceRangePrediction.pipeline.prediction import PredictionPipeline
from mobilePriceRangePrediction.entity import PredictionRequest

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
async def index(request: Request):
    try:
        content = index_dict
        return templates.TemplateResponse("index.html",{"request":request, "content":content}) 
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")
    

@app.get("/form")
async def form(request: Request):
    try:
        content = form_dict
        return templates.TemplateResponse("form.html",{"request":request, "content":content}) 

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")

@app.get("/about")
async def about(request: Request):
    try:
        content = about_dict
        return templates.TemplateResponse("about.html",{"request":request, "content":content}) 
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")

@app.post("/predict")
async def predict(request: PredictionRequest):
    try:
        data = request.model_dump()
        df = pd.DataFrame([data])
        
        obj = PredictionPipeline()
        pred = obj.predict(df)
        result = classify_prediction(int(pred))

        return {"prediction": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction error: {e}")
    
@app.get("/train")
def training():
    try:
        os.system("python main.py")
        return Response("Training was successfull.")
    except Exception as e:
        return Response(f"Error occurred: {e}")

if __name__=="__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
