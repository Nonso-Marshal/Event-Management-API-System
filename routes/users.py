from fastapi import APIRouter
from schemas.users import UserCreate, UserUpdate
from services.users import user_service



user_router = APIRouter()


@user_router.post("/", status_code=201)
def create_user(user_data: UserCreate):
    return user_service.create_user(user_data)


@user_router.get("/", status_code=200)
def get_all_users():
    return user_service.get_all_users()


@user_router.get("/{user_id}", status_code=200)
def get_user_by_id(user_id: int):
    return user_service.get_user_by_id(user_id)

@user_router.put("/{user_id}", status_code=200)
def update_user(user_id: int, user_update: UserUpdate):
    return user_service.update_user(user_id, user_update)

@user_router.delete("/{user_id}", status_code=200)
def delete_user(user_id: int):
    return user_service.delete_user(user_id)

@user_router.patch("/{user_id}", status_code=200)
def deactivate_user(user_id: int):
    return user_service.deactivate_user(user_id)