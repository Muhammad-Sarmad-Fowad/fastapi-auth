from fastapi import FastAPI, Form, HTTPException
import json
import os
app=FastAPI()
USER_DB_FILE="user.json"

def load_user():
    if os.path.exists(USER_DB_FILE):
        with open(USER_DB_FILE, "r") as file:
            return json.load(file)
    return {}

def save_user(users):
    with open(USER_DB_FILE, "w") as file:
        json.dump(users, file)

@app.post("/signup")
def signup(username: str = Form(...), password: str = Form(...)):
    users=load_user()
    if username in users:
        raise HTTPException(status_code=400, detail="User already exists")
    users[username]=password
    save_user(users)
    return {"message": "Signup successful!"}

@app.post("/login")
def login(username: str = Form(...), password: str = Form(...)):
    users=load_user()
    if username not in users or users[username]!=password:
        raise HTTPException(status_code=401, detail="Wrong username or password")
    return {"message": "Login successful!"}
    
