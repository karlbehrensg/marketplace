from pydantic import BaseModel, EmailStr
from typing import Optional, List


class User(BaseModel):
    legal_id: str
    name: str
    last_name: str
    email: EmailStr


class Commerce(BaseModel):
    legal_id: str
    name: str
    retail_name: Optional[str]
    email: EmailStr
    users: List[User]


class RegistrationForm(Commerce):
    pass
