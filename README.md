# Django REST API Project

A Django REST API project implementing a client-project management system with user authentication.

## Database Design

### Entity Relationship Diagram

```
User (Django's built-in User model)
├── id (PK)
├── username
├── first_name
├── last_name
└── email

Client
├── id (PK)
├── client_name
├── created_at
├── updated_at
└── created_by (FK -> User)

Project
├── id (PK)
├── project_name
├── client (FK -> Client)
├── created_at
├── created_by (FK -> User)
└── users (M2M -> User)
```

### Relationships
- User is Django's built-in model with additional fields like first_name and last_name used to display full names.
- Client is created by one User (via created_by) and can have many Project entries.
- Project is linked to a single Client and can involve multiple User entries via a many-to-many relationship.

## How to Run the Project

### Prerequisites
- Python 3.8 or higher
- Django 5.1+
- MySQL database

### Setup Steps

1. Clone the repository:
```bash
git clone <repository-url>
cd <project-directory>
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate
```

3. Configure the database:
- Create a MySQL database
- Update the database settings in `core/settings.py`

4. Install dependencies:
```bash
pip install -r requirements.txt
```

5. Apply migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

6. Create a superuser:
```bash
python manage.py createsuperuser
```

7. Start the development server:
```bash
python manage.py runserver
```

8. Access the application:

- API Base URL: http://127.0.0.1:8000/api/
- Django Admin Panel: http://127.0.0.1:8000/admin/

## API Endpoints

### Client Endpoints

1. List all clients
```
GET /api/clients/
```

2. Create a new client
```
POST /api/clients/
```

3. Get client details
```
GET /api/clients/:id/
```

4. Update client
```
PUT/PATCH /api/clients/:id/
```

5. Delete client
```
DELETE /api/clients/:id/
```

### Project Endpoints

1. List user's projects
```
GET /api/projects/
```

2. Create project for client
```
POST /api/clients/:id/projects/
```

## Authentication

The API uses Django's session-based authentication. You need to:
1. Log in through the Django admin interface (`/admin/`)
2. Use the obtained session for API requests

## Project Structure

```
├── api/
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   ├── models.py
│   └── __init__.py
├── core/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   ├── asgi.py
│   └── __init__.py
├── manage.py
├── requirements.txt
└── README.md

```
