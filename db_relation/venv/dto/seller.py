from pydantic import BaseModel

class SellerDetailDto(BaseModel):
    id: int
    name: str
    description: str
    logo: str
    address: str

    class Config:
        orm_mode = True


class SellerUpdateDetailDto(BaseModel):
    id: int
    name: str
    description: str
    logo: str
    address: str


class SellerCreateDto(BaseModel):
    name: str
    description: str
    logo: str
    address: str
