# Event-Management-API-System

This system allows users to register for events, track attendance, and manage both event information and speaker details.


# Prerequisites

Before you begin, ensure you have the following installed:
Python 3.7+ (Download from python.org)
pip (Python package manager, included with Python)
Virtualenv (Optional, but recommended for isolating dependencies)



# Event-Management-API-System


      ├── main.py                         # Main FastAPI application file      
      ├── schemas/                        # Pydantic models for request/response validation for Events, User, Registrations
            └──users.py
            └──events.py
            └──registration.py
      ├── routes/                         # router for the entities: events, users, registration
              └──users.py
              └──events.py
              └──registration.py
      ├── services/                       # app logics/crud operations for the entities: events, users, registration
              └──users.py
              └──events.py
              └──registration.py
      ├── models.py                       # Data models (e.g., event models)
      ├── database.py                     # Database or in-memory data setup
      └── README.md   




# Getting Started

Follow these steps to set up and run the FastAPI application locally.




# 1. Clone the Repository

If you haven't already, clone the repository to your local machine:

      * git clone (https://github.com/Nonso-Marshal/Event-Management-API-System.git)
        
      * cd Event-Management-API-System



# 2. Set Up a Virtual Environment (Optional but Recommended)

Create and activate a virtual environment:

      bash
      Create a virtual environment
      * python -m venv venv
      
      Activate the virtual environment
      
      On Windows:
      
      * venv\Scripts\activate
      
      On macOS/Linux:
      
      * source venv/bin/activate
      

# 3. Run the FastAPI Application

Start the FastAPI server using Uvicorn, an ASGI server implementation:

      bash
      
      * uvicorn main:app --reload
      
      main:app: Refers to the FastAPI app instance in main.py


# 4. Access the API 

API Root: Visit http://127.0.0.1:8000 to see the default response.

Interactive API Docs: Open your browser and navigate to http://127.0.0.1:8000/docs to access the Swagger UI, where you can test API endpoints interactively.


# 5. Example API Endpoints

* GET /users: Retrieve all users.

* POST /users: Create a new user.

* GET /events: Retrieve all events.

* POST /registrations: Register a user for an event.

* Check the Swagger UI (/docs) for a complete list of endpoints and their schemas.


# 6. Stopping the Server

* To stop the server, press Ctrl+C in the terminal.










