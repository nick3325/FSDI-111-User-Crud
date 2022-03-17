
from app.database import get_db

def get_users_and_vehicle_join():
    stmt = """
    SELECT user.last_name,
    user.first_name,
    user.hobbies,
    user.active,
    vehicle.license_plate,
    vehicle.color,
    vehicle_type.description
    FROM user 
    INNER JOIN vehicle ON user.id = vehicle.user_id
    INNER JOIN vehicle_type ON vehicle.v_type = vehicle_type.id
"""
cursor = get_db().execute(stmt, ())
results = cursor.fetchall()
cursor.close()
out = []
for results in results:
    res_dict = {}
    res_dict = {
        "user.last_name": result[0],
        "user.first_name": result[1],
        "user.hobbies": result[2],
        "user.active": True if
        "vehicle.license_plate":
        "vehicle.color":
        "vehicle_type.description":
    }
    
