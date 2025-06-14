from fastapi import HTTPException
from schemas.events import EventCreate, EventUpdate
from database import events
from models import Event as EventModel

class EventService:

    @staticmethod
    def create_event(event_data: EventCreate):
        for event in events:
            if event.title == event_data.title:
                raise HTTPException(status_code=409, detail="Event already Exists")
        
        event_id = len(events) + 1
        event = EventModel(id=event_id, **event_data.model_dump())
        events.append(event)
        return event
    

    @staticmethod
    def get_event_by_id(event_id: int):
        for event in events:
            if event.id == event_id:
                return event
        
        for event in events:
            if event.id != event_id:
                raise HTTPException(status_code=400, detail="Event do not exist")


    @staticmethod
    def get_all_events():
        if not events:
            raise HTTPException(status_code=404, detail="Event database is empty")
        return events
    

    @staticmethod
    def update_event(event_id: int, event_update: EventUpdate):   
        event = next((event for event in events if event.id == event_id), None)
        if not event:
                raise HTTPException(status_code=404, detail="Event do not exist")
    
        if event_update.title is not None and event_update.title != event.title:
            if any(event.title == event_update.title for event in events if event.id != event_id):
                raise HTTPException(status_code=409, detail="Event title already exists")
        
        for event in events:
            if event.id == event_id:
                if event_update.title is not None:
                    event.title = event_update.title
                if event_update.date is not None:
                    event.date = event_update.date
                if event_update.location is not None:
                    event.location = event_update.location
                if event_update.is_open is not None:
                    event.is_open = event_update.is_open
                return event
            
    @staticmethod
    def delete_user(event_id: int):
        for event in events:
            if event.id == event_id:
                events.remove(event)
                return{"message" : "Event successfully deleted"}
            
        for event in events:
            if event.id != event_id:
                raise HTTPException(status_code=404, detail="Event do not exist")


    @staticmethod
    def close_event(event_id: int):
        for event in events:
            if not event:
                raise HTTPException(status_code=404, detail="Event do not exist")      


        for event in events:
            if event.is_open == False:
                raise HTTPException(status_code=400, detail="Event is already closed for registration")

        event.is_open = False
        return event


event_service = EventService()

