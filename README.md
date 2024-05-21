# Health Blog App

## Introduction

Welcome to the repository of our Health Blog App. This application serves as a platform for users to read and share informative articles about health and wellness. Built with Django and SQLite, and styled with Crispy Forms and Bootstrap 5, this app offers a responsive and intuitive user interface. It is deployed on Render for seamless access and performance.

## Features

- **User Authentication**: Sign up, log in, and manage your profile.
- **Article Management**: Create, read, update, and delete articles.
- **Comments**: Engage with the community through comments on articles.
- **Responsive Design**: Fully responsive web design using Bootstrap 5.

## Technologies

- **Django**: A high-level Python Web framework that encourages rapid development and clean, pragmatic design.
- **SQLite**: Used as a lightweight disk-based database to store user and blog data.
- **Crispy Forms**: Utilized to style Django forms with Bootstrap 5.
- **Bootstrap 5**: For modern, responsive designs.
- **Render**: Cloud service provider for deploying and running the application.

## Local Development

Follow these instructions to set up the Health Blog App for development on your local machine.

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Setup

1. **Clone the repository**

    ```
    git clone https://github.com/Rajanrj99/helthblog2.git
    cd helthblog2
    ```

2. **Create and activate a virtual environment (recommended)**

    ```
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    .\venv\Scripts\activate.bat
    ```

3. **Install dependencies**

    ```
    pip install -r requirements.txt
    ```

4. **Set up the database**

    Run migrations to set up your SQLite database.

    ```
    python manage.py migrate
    ```

5. **Run the development server**

    ```
    python manage.py runserver
    ```

    Visit `http://127.0.0.1:8000` in your browser to view the app.

## Deployment on Render

This application is deployed on Render. For deploying your own fork or version, follow these steps:

- Set up a new Web Service on Render and link to your repository.
- Use the following build command:
  
