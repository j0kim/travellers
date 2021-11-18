from typing import List
from fastapi import FastAPI, HTTPException
from typing import List
from models import User, Gender
from uuid import uuid4, UUID

app = FastAPI()

# Our dummy database to store users of the application
traveller_db: List[User] = [

]

@app.get("/")
async def root():
    return {"Home": "Page!"}

# Get users from the database
@app.get("/api/v1/users")
async def fetch_users():
    return traveller_db

# Add new users to the database
@app.post("/api/v1/users")
async def add_user(user: User):
    traveller_db.append(user)
    return {"id": user.id}

# Delete a user from the database
@app.delete("/api/v1/users{user_id}")
async def delete_user(user_id: UUID):
    for user in traveller_db:
        if user.id == user_id:
            traveller_db.remove(user)
            return
    raise HTTPException (
        status_code=404,
        detail=f"user with id: {user_id} does not exist."
    )















