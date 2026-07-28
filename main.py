from fastapi import FastAPI

app = FastAPI()


# Home Route 

@app.get("/")
def home():
    return {"message": "Hello World, FastAPI!"}


# about route
@app.get("/about")
def about():
    return {"messages":"This is About Page"}

# users Route

@app.get("/users")
def users():
    return {
        "users":["Mohit","Rohit","Sourav"]
    }