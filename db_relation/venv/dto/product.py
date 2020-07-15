from pydantic import BaseModel

class ProductDto(BaseModel):
    id: int
    name: str
    price: int
    description: str
    producer_id: int
    seller_id: int

    class Config:
        orm_mode = True


class ProductUpdateDTO(BaseModel):
    name: str
    price: int
    description: str


class ProductCreateDto(BaseModel):
    name: str
    price: int
    description: str
    producer_id: int

