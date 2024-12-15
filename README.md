# Taskify API

Taskify is a simple task management application built with Flask, SQLAlchemy, and JWT authentication. It allows users to create, update, delete, and view tasks, with JWT-based login and email notifications.

## Key Features:
- User registration
- Login using username and password
- Add new tasks
- View tasks
- Update task status
- Delete tasks
- JWT-based authentication

## Technologies Used:
- **Flask**: Python web framework for building the application.
- **SQLAlchemy**: ORM for interacting with the database.
- **Flask-JWT-Extended**: JWT authentication support.
- **Flask-Mail**: Email notification functionality.
- **Flasgger**: API documentation using Swagger UI.

## Getting Started

### Prerequisites:
- Python 3.8 or higher
- PostgreSQL or any database supported by SQLAlchemy

### Installation Steps:
1. Clone the repository:
   ```bash
   git clone https://github.com/SaaaRoO/Taskify.git
   
2. Navigate to the project folder:
   cd Taskify

3. Create a virtual environment:
   python -m venv venv

4. Activate the virtual environment:
   **On Windows:
   venv\Scripts\activate

5. Install the required dependencies:
   pip install -r requirements.txt

   
6.  Update the email configuration in config.py:

**Make sure to set MAIL_USERNAME and MAIL_PASSWORD with your email account credentials.

7. Run the application:
   python app/app.py
8. Access the Swagger API documentation at:
   http://127.0.0.1:5000/swagger
