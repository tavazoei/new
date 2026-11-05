from pydantic import BaseModel, ConfigDict, EmailStr, Field

# -------------------------
# Product Schemas
# -------------------------


class ProductCreate(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    price: int = Field(gt=0)


class ProductResponse(BaseModel):
    id: int
    name: str
    price: int

    model_config = ConfigDict(from_attributes=True)


# -------------------------
# Authentication Schemas
# -------------------------


class UserCreate(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8, max_length=128)


class UserResponse(BaseModel):
    id: int
    email: EmailStr
    role: str
    is_active: bool

    model_config = ConfigDict(from_attributes=True)


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"


class TokenData(BaseModel):
    email: str | None = None
