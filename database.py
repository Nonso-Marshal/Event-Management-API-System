from models import User, Event, Registration


users: list[User] = []
events: list[Event] = []
registrations: list[Registration] = []

speakers = [
    {"id": 1, 
    "Name": "Prof C.S Nwajide", 
    "Topic": "Geology Of Nigerian Sedimentary Basins"
    },

    {"id": 2, 
    "Name": "Mr Austin Avuru", 
    "Topic": "Extending the Frontiers of Deepwater Exploration"
    },

    {"id": 3, 
    "Name": "Mr Johnbosco Uche", 
    "Topic": "Application of Artificial Intelligence in Seismic Interpretation"
    },
]