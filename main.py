from fastapi import FastAPI, status , HTTPException


app = FastAPI()

# 200 → OK → Request successfully processed / data retrieved

# 201 → Created → New data/resource successfully created

# 400 → Bad Request → Client ki request invalid/incorrect hai

# 404 → Not Found → Requested resource/URL nahi mila

# 500 → Internal Server Error → Server ke andar unexpected error

@app.post("/create_user", status_code = status.HTTP_201_CREATED)
def create_user():
    return {
        "message" : "User Created"
    }


@app.get("/user")
def get_user():
    return{
        "status":"Success",
        "message":"User Fetched",
        "data":{
            "name":"Sourav",
            "age":24
        }
    }

@app.get("/users/{user_id}")
def get_user(user_id : int):
    if user_id != 1:
        raise HTTPException(
            status_code = 404,
            detail="User Not Found"
        )
    return{
        "id":1,
        "name":"Sourav"
    }