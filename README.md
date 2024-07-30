# Django Application

This a Django blog application which allows users to read, create and delete blog posts. This application uses the Django framework to handle the backend logic, database intercations and template rendering. 
The features of this app include:
1. User authentication - Sign up, Login, Logout
2. Create, Read and Delete operations on blog posts
3. Search blogs using author name

# Setup
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

## Install the requirements.txt
```
pip install -r requirements.txt
```

## Set Up the Database
### Apply databse migrations
```
python manage.py makemigrations
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

You can also specify IP address and port number (if required) using the following command
```
python manage.py runserver <ip-address>:<port number>
```

