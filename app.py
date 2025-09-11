import uvicorn
from fastapi import FastAPI
from interaction_data import Attributes
import pandas as pd 
import numpy as np
import pickle

app = FastAPI()
pickle_in = open("nearest_neighbors_model.pkl", "rb")
nn = pickle.load(pickle_in)

@app.get('/')
def index():
    return {'message': 'Hello, World'}

@app.post('/rec-sys')
def recsys(data:Attributes):
    data = data.dict()
    student_id = data['student_id']
    video_title = data['video_title']
    video_link = data['video_link']
    video_description = data['video_description']
    video_tags = data['video_tags']
    interaction_type = data['interaction_type']

    recommendation = nn.recommend_videos(video_title, num_recommendations=5)

if __name__ == '__main__':
    uvicorn.run(app, host=' ', port=)