from fastapi import FastAPI
from models.Profile import Profile
import  json

app = FastAPI(title="Learning apis")

"""
read a file 
"""
def load_json():
    with open('profile.json','r') as f:
        data = json.load(f)
        return data


@app.get("/")
def read_root():
    return {"message": "We are learing apis"}


@app.get("/profile/{profile_id}")
def get_profile(profile_id: str):
    """load all the data and then filter our profile"""
    data = load_json()
    if profile_id in data:
        return data[profile_id]

    return {'error':f"No Such record for {profile_id}"}







