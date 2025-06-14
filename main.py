from fastapi import FastAPI
from routes.users import user_router
from routes.speakers import speaker_router
from routes.events import event_router
from routes.registration import registration_router


app = FastAPI()


@app.get("/", status_code=200, tags=["Home"])
def home():
    return ("Welcome to my Event Management API System")
        
            
app.include_router(speaker_router, prefix="/Speakers", tags=["Speakers"])            
app.include_router(user_router, prefix="/users", tags=["Users"])
app.include_router(event_router, prefix="/events", tags=["Events"])
app.include_router(registration_router, prefix="/Registration", tags=["Registration"])
