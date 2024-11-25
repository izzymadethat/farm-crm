from pydantic import BaseModel

class ContactItem(BaseModel):
    name: str
    email: str
    phone: str
    
class ContactResponse(BaseModel):
    id: int
    name: str
    email: str
    phone: str
    
    class Config:
        orm_mode = True
      
    
    