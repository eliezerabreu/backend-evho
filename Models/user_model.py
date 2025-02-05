from pydantic import BaseModel, EmailStr
from typing import Optional

class User(BaseModel):
    user_id: str
    email: EmailStr
    hashed_password: str
    role: str  # "driver" | "rider"
    is_verified: bool = False
    location: Optional[dict] = None  # GeoJSON: { "type": "Point", "coordinates": [lng, lat] }