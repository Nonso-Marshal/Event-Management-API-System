from fastapi import HTTPException
from schemas.users import UserCreate, UserUpdate
from database import users
from models import User as UserModel



class UserService:

    @staticmethod
    def create_user(user_data: UserCreate):
        for user in users:
            if user.email == user_data.email:
                raise HTTPException(status_code=409, detail="User with this Email already exist")


        user_id = len(users) + 1
        user = UserModel(id=user_id, **user_data.model_dump())
        users.append(user)
        return user
    
    
    @staticmethod
    def get_user_by_id(user_id: int):
        if user_id <= 0:
            raise HTTPException(status_code=400, detail="Invalid user ID")
        
        for user in users:
            if user.id == user_id:
                return user
        for user in users:
            if user.id != user_id:
                raise HTTPException(status_code=400, detail="User do not exist")


    

    @staticmethod
    def get_all_users():
        if not users:
            raise HTTPException(status_code=404, detail="User database is empty")
        return users
    
    @staticmethod
    def update_user(user_id : int, user_update: UserUpdate):
        if user_id <= 0:
            raise HTTPException(status_code=400, detail="Invalid user ID")
        
        user = next((user for user in users if user.id == user_id), None)
        if not user:
            raise HTTPException(status_code=404, detail="User not exist")
            
        if user_update.email is not None and user_update.email != user.email:
            if any(user.email == user_update.email for user in users if user.id != user_id):
                raise HTTPException(status_code=409, detail="User with this Email already exist")

        for user in users:
            if user.id == user_id:
                if user_update.name is not None:
                    user.name = user_update.name
                if user_update.email is not None:
                    user.email = user_update.email
                if user_update.is_active is not None:
                    user.is_active = user_update.is_active
                return user
    
    
    @staticmethod
    def delete_user(user_id : int):
        if user_id <= 0:
            raise HTTPException(status_code=400, detail="Invalid user ID")
    
        for user in users:
            if user.id == user_id:
                users.remove(user)
                return {"message" : "User successfully deleted"}
            
        for user in users:
            if user.id != user_id:
                raise HTTPException(status_code=404, detail="User do not exist")
            

    @staticmethod
    def deactivate_user(user_id: int):
        if user_id <= 0:
            raise HTTPException(status_code=400, detail="Invalid user ID")
    
        user = next((user for user in users if user.id == user_id), None)
        if not user:
            raise HTTPException(status_code=404, detail="User does not exist")
        
        for user in users:
            if user.is_active == False:
                raise HTTPException(status_code=400, detail="User is already inatcive")

        user.is_active = False
        return user
            
user_service = UserService()
    