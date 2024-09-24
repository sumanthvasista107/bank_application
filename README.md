Django Banking Application

This project is a web-based banking application built using Django. It allows users to securely manage their accounts, perform fund transfers, and handle multiple currencies with real-time exchange rates. The admin dashboard provides an overview of all users and their account details.
Features

    User Authentication:
        User registration and login (with 2FA)
        Admin user setup
        Password management (reset, change)
    Banking Features:
        User account management (opening, editing, viewing)
        Fund transfers between accounts
        Multi-currency support (using an exchange rate API)
    Admin Features:
        Dashboard with user and account details
        Account management for all users
        Ability to create new users (username, email, password)

Getting Started
Prerequisites

    Python 3.8+
    Django 4.x
    A currency exchange API (e.g., Open Exchange Rates or Fixer.io)

Installation

    Clone the repository:
    git clone https://github.com/yourusername/django-banking-app.git
    cd django-banking-app

Create a virtual environment and activate it:


_python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`_

Install dependencies:

pip install -r requirements.txt

Configure environment variables:

Create a .env file in the project root directory and add your configuration:

bash

SECRET_KEY=your_django_secret_key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL=your_database_url
EXCHANGE_API_KEY=your_exchange_api_key

Apply migrations:

bash

python manage.py migrate

Create a superuser (admin):

bash

python manage.py createsuperuser

Run the development server:

bash

python manage.py runserver

please use

http://127.0.0.1:8000/login/ to login to the system

superadmin username: admin
password: admin
