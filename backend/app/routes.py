from datetime import datetime
from app.database import user
from flask import (
    Flask,
    request
)

app = Flask(__name__)
VERSION = "1.0.0"
@app.get("/ping")
def ping():
    resp = {
        "status": "ok",
        "message": "success"
    }
    return resp

@app.get("/version")
def version():
    resp = {
        "status": "ok",
        "message": "success",
        "version": VERSION,
        "server_time": datetime.now().strftime("%F %H:%M:%S")
    }
    return resp 

@app.get("/users/<int:pk>")
def get_user_by_id(pk):
    target_user = user.select_by_id(pk)
    resp = {
        "status": "ok",
        "message": "success",
        "user": target_user
    }
    return resp

@app.get("/users/")
def get_all_users():
    user_list = user.scan()
    resp = {
        "status": "ok",
        "message": "success",
        "user": user_list
    }
    return resp

@app.post("/users/")
def create_user():
    user_data = request.json
    user.insert(user_data)
    return "", 204

@app.delete("/users/<int:pk>")
def deactivate_user(pk):
    user.deactivate(pk)
    return "", 204

@app.get("/vehicles/users/<int:user_id>")
def get_vehicle_byuser_id(user_id):
    vehicle_list = vehicles.select_by_user_id(user_id)
    resp = {
        "status": "ok",
        "message": "success",
        "vehicles": vehicle_list
        
    }
    return resp

@app.get("/reports/users/vehicles")
def get_users_and_vehicles_join():
    output = report.get_user_and_vehicles_join()
    resp = {
        "status": "ok",
        "message": "success",
        "vehicles": output
    }
    return resp

