# Django Application

This a Django blog application which allows users to read, create and delete blog posts. This application uses the Django framework to handle the backend logic, database interations and template rendering. 
The features of this app include:
1. User authentication - Sign up, Login, Logout
2. Create, Read and Delete operations on blog posts
3. Search blogs using author name

### User registration and login
The user is directed to the Sign up page as soon as the application is run, to create an account. The user is redirected to the login page, logs in, and is redirected to the home page. 

### Create a post
The authenticated user navigates to the "New Post" page.
Fills out the post creation form and submits it.
The post is saved to the database, and the user is redirected to the home page or the post detail page. 

### Viewing posts
Any user can visit the home page to see a list of all posts.
There is also search functionality - search based on author name.

### Deleting posts
A user can only delete the posts authored by him/her. 

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

