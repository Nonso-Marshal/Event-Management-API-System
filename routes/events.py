from fastapi import APIRouter
from schemas.events import EventCreate, EventUpdate
from services.events import event_service

event_router = APIRouter()

@event_router.post("/", status_code=201)
def create_event(event_data: EventCreate):
    return event_service.create_event(event_data)

@event_router.get("/", status_code=200)
def get_all_events():
    return event_service.get_all_events()

@event_router.get("/{event_id}", status_code=200)
def get_event_by_id(event_id: int):
    return event_service.get_event_by_id(event_id)

@event_router.put("/{event_id}", status_code=200)
def update_event(event_id: int, event_update: EventUpdate):
    return event_service.update_event(event_id, event_update)

@event_router.delete("/{event_id}", status_code=200)
def delete_event(event_id: int):
    return event_service.delete_user(event_id)

@event_router.patch("/{event_id}", status_code=200)
def close_event_registration(event_id: int):
    return event_service.close_event(event_id)