from pydantic import BaseModel, EmailStr
from typing import Optional


class CompanyCreate(BaseModel):
    name: str
    email: Optional[EmailStr] = None
    city: Optional[str] = None
    country: Optional[str] = None
    address: Optional[str] = None
    website: Optional[str] = None
    description: Optional[str] = None
    logo: Optional[str] = None


class CompanyResponse(BaseModel):
    id: int
    name: str
    email: Optional[EmailStr] = None
    city: Optional[str] = None
    country: Optional[str] = None
    address: Optional[str] = None
    website: Optional[str] = None
    description: Optional[str] = None
    logo: Optional[str] = None
    user_id: int

    class Config:
        from_attributes = True