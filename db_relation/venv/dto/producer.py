from pydantic import BaseModel

class ProducerDTO(BaseModel):
    name: str
    description: str
    logo: str

    class Config:
        orm_mode = True
