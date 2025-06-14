from fastapi import HTTPException
from typing import List
from schemas.registrations import RegisterCreate
from database import registrations, users, events
from models import Registration as RegisterModel
from models import User


class Registration:


    @staticmethod
    def register_user_for_event(register_data: RegisterCreate):
        user = next((user for user in users if user.id == register_data.user_id), None)
        if not user:
            raise HTTPException(status_code=404, detail="User does not exist")
        
        if not user.is_active:
            raise HTTPException(status_code=403, detail="User is not active")
        
        
        event = next((event for event in events if event.id == register_data.event_id), None)
        if not event:
            raise HTTPException(status_code=404, detail="Event does not exist")
        
        if not event.is_open:
            raise HTTPException(status_code=403, detail="Event is closed for registration")


        for registrant in registrations:
            if registrant.user_id == register_data.user_id and registrant.event_id ==register_data.event_id:
                raise HTTPException(status_code=409, detail="User already registered for this event")


        registration_id = len(registrations) + 1
        registrant = RegisterModel(id=registration_id, **register_data.model_dump())
        registrations.append(registrant)
        return registrant        
    

    @staticmethod
    def mark_attendance(registrant_id: int):
        if registrant_id <= 0:
            raise HTTPException(status_code=400, detail="Invalid registration ID")



        for registrant in registrations:
            if registrant.id == registrant_id:
                registrant.attended = True
                return registrant

        raise HTTPException(status_code=404, detail="User not found in registrations")


    @staticmethod
    def get_all_registration():
        if not registrations:
            raise HTTPException(status_code=404, detail="Registration database is empty")

        return registrations
    
    @staticmethod
    def get_registration_by_user_id(user_id: int) -> List[RegisterModel]:
        if user_id <= 0:
            raise HTTPException(status_code=400, detail="Invalid User ID")
            
        unique_user = [registration for registration in registrations if registration.user_id == user_id]

        if not unique_user:
            raise HTTPException(status_code=404, detail="User not found in registrations")

        return unique_user



    @staticmethod
    def user_who_attended_atleast_one_event() -> List[User]:
        attendee_user_ids = set(registrant.user_id for registrant in registrations if registrant.attended)

        attendees = [user for user in users if user.id in attendee_user_ids]

        if not attendees:
            raise HTTPException(status_code=404, detail="No users found who attended any event")
        
        return attendees

registration_service = Registration()