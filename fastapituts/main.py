from fastapi import FastAPI, Path, HTTPException, Query
from models.Profile import Profile
import json

app = FastAPI(title="Learning apis")

"""
read a file 
"""


def load_json():
    with open('profile.json', 'r') as f:
        data = json.load(f)
        return data


@app.get("/")
def read_root():
    return {"message": "We are learing apis"}


# this is an example of path param
@app.get("/profile/{profile_id}")
def get_profile(profile_id: str = Path(..., description="Id of the Profile you want to fetch", example="P001")):
    """load all the data and then filter our profile"""
    data = load_json()
    if profile_id in data:
        return data[profile_id]
    raise HTTPException(status_code=404, detail="Profile Id not found")


# an example of query param ?key=value for exampe https://www.gn.com/profile?username=rohit -- mostly for sorting or filterinh
@app.get("/sort")
def get_query_param(sort_by: str = Query(..., description="Sorty by any value u want"),
                    order: str = Query('asc', description="The values will be sorted in ascending order")):
    valid_values = ['name', 'age']
    if sort_by not in valid_values:
        raise HTTPException(status_code=400, detail=f'Invalid field value select from ${valid_values}')

    if order not in ['asc', 'dsc']:
        raise HTTPException(status_code=400, detail=f'Invalid field value select fromas c or dsc')

    data = load_json()  # load the key value map -- iterate abd sort tdate data fron the map
    sort_order = True if order == 'asc' else False
    sorted_data = sorted(data.values(), key=lambda x: x.get(sort_by, 0), reverse=sort_order)
    return sorted_data
