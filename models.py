from typing import Optional, List
from uuid import UUID, uuid4
from pydantic import BaseModel
from enum import Enum

class Gender(str, Enum):
    male = "male"
    female = "female"

class User (BaseModel):
    id: Optional[UUID] = uuid4()
    first_name: str
    last_name: str
    user_name: str
    user_email: str
    user_pass: str
    user_country: str


