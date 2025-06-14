from pydantic import BaseModel
from datetime import date

class RegistrationBase(BaseModel):
    user_id : int
    event_id : int
    registration_date : date
    

class RegisterCreate(RegistrationBase):
    pass

class RegisterUpdate(RegistrationBase):
    attended : bool = False

class Register(RegistrationBase):
    id : int

