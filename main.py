from typing import List
from fastapi import FastAPI, HTTPException
from typing import List
from models import User, Gender, Role
from uuid import uuid4, UUID

app = FastAPI()

# Our dummy database to store users of the application
db: List[User] = [
    User(
        id=UUID("d5b01056-cdb0-4c45-9074-28a85b96be0a"),
        first_name="John",
        last_name="Doe",
        user_email="johndoe@gmail.com",
        gender=Gender.male,
        country="Uganda",
        roles=[Role.admin, Role.user]
    ),

    User (
        id=UUID("1d7bbc41-034e-4df0-a3bd-e74966d7a8e0"),
        first_name="Yi",
        last_name="Ting",
        user_email="yiting@gmail.com",
        gender=Gender.female,
        country="Taiwan",
        roles=[Role.user]
    )
]

@app.get("/")
async def root():
    return {"Hello": "World!"}

# Get users from the database
@app.get("/api/v1/users")
async def fetch_users():
    return db

# Add new users to the database
@app.post("/api/v1/users")
async def add_user(user: User):
    db.append(user)
    return {"id": user.id}

# Delete a user from the database
@app.delete("/api/v1/users{user_id}") #Path variable
async def delete_user(user_id: UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return
    raise HTTPException (
        status_code=404,
        detail=f"user with id: {user_id} does not exist."
    )















