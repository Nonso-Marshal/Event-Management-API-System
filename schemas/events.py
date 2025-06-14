from pydantic import BaseModel
from typing import Optional
from datetime import date

class EventBase(BaseModel):
    title : str
    location : str
    date : date
    

class EventCreate(EventBase):
    pass

class Events(EventBase):
    id : int
    is_open : bool = True


class EventUpdate(EventBase):
    title : Optional[str] = None
    location : Optional[str] = None
    date : Optional[date]
    is_open : Optional[bool] = True