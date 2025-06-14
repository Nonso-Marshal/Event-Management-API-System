from fastapi import APIRouter
from typing import List
from schemas.registrations import RegisterCreate
from services.registration import registration_service
from models import Registration as Registermodel

registration_router = APIRouter()

@registration_router.post("/", status_code=201)
def register_user_for_event(register_data: RegisterCreate):
    return registration_service.register_user_for_event(register_data)


@registration_router.post("/{registrant_id}", status_code=200)
def mark_attendance(registrant_id: int):
    return registration_service.mark_attendance(registrant_id)

@registration_router.get("/", status_code=200)
def get_all_registration():
    return registration_service.get_all_registration()

@registration_router.get("/{user_id}", status_code=200)
def get_registrant_by_user_id(user_id: int):
    return registration_service.get_registration_by_user_id(user_id)

@registration_router.get("/user/{user_id}", status_code=200)
def user_who_attended_atleast_one_event():
    return registration_service.user_who_attended_atleast_one_event()