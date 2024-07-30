# Django Application setup

## Prerequisites

Before you begin, ensure you have the following installed:
1. Python (3.6 or later)
2. pip (Python package installer)

## Clone the repository
```
git clone https://github.com/yourusername/your-repository.git
cd your-repository
```
## Setup Virtual Environment
### Create and activate a virtual environment
1. On macOS/Linux
```
python3 -m venv venv
source venv/bin/activate
```
2. On windows
```
python -m venv venv
venv\Scripts\activate
```

## Set Up the Database
### Apply databse migrations
```
python manage.py migrate
```

### Create a superuser (optional but recommended for accessing the admin interface)
```
python manage.py createsuperuser
```

Follow the prompts to create the superuser account.

## Run the Development Server
```
python manage.py runserver
```

## Access the Application
Open your web browser and go to:

1. Home Page: http://127.0.0.1:8000/
2. Admin Interface: http://127.0.0.1:8000/admin (use the superuser credentials you created)

