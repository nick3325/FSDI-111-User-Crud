
-- Creates a user database table:
CREATE TABLE user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name VARCHAR(45) NOT NULL,
    last_name VARCHAR(45) NOT NULL,
    hobbies TEXT,
    active BOOLEAN NOT NULL DEFAULT 1
);

CREATE TABLE vehicle (
    id INTEGER PRIMARY KEY AUTOINCREMENT
    color VARCHAR(45) NOT NULL,
    license_plate VARCHAR(45) NOT NULL,
    v_type INTEGER NOT NULL,
    user_id INTEGER NOT NULL,
    active BOOLEAN DEFAULT 1,
    FOREIGN KEY (v_type) REFERENCES vehicle_types(id)
    FOREIGN KEY (user_id) REFERENCES user(id)
)

CREATE TABLE vehicle_type(
    id INTEGER PRIMARY KEY AUTOINCREMENT
    description VARCHAR(64)
);
-- Creates a new record in the user table:
INSERT INTO user (
    first_name,
    last_name,
    hobbies
) VALUES (
    "Rafael",
    "GPL",
    "DIY stuff"
);

INSERT INTO user (
    first_name,
    last_name,
    hobbies
) VALUES (
    "Jane",
    "Doe",
    "Skiing"
);

INSERT INTO user (
    first_name,
    last_name,
    hobbies
) VALUES (
    "John",
    "Doe",
    "Painting"
);

INSERT INTO vehicle(description) VALUES ("motercycle")


INSERT INTO vehicle(
    color,
    license_plate,
    v_type,
    user_id
) VALUES
    "red",
    "HELLO1",
    2,
    1
);

SELECT user.last_name,
       user.first_name,
       user.hobbies,
       user.active,
       vehicle.license_plate,
       vehicle.color,
       vehicle_type.description
FROM user 
INNER JOIN vehicle ON user.id

SELECT user.last_name,
       user.first_name,
       user.hobbies, 
       user.active,
       vehicle.license_plate,
       vehicle.color
    FROM user
    INNER JOIN