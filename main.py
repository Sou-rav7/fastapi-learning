from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# {
#     "name": "Mohit",
#     "age": 25,
#   "  password ":12345
# }
# for this we have to learn branch model 

class User (BaseModel):
    name : str
    age : int
    password : str

class UserResponse(BaseModel):
    name : str
    age : int

@app.get("/user",response_model=UserResponse)
def get_use():
    return{
        "name":"Sourav",
        "age": 23,
        "password":"12345"
    }