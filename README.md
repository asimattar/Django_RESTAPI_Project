# Django REST API Project

A Django REST API project implementing a client-project management system with user authentication.

## Database Design

### Entity Relationship Diagram

```
User (Django's built-in User model)
├── id (PK)
└── username

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
- A Client belongs to one User (created_by)
- A Client can have many Projects
- A Project belongs to one Client
- A Project can have many Users
- A User can be assigned to many Projects

## How to Run the Project

### Prerequisites
- Python 3.8 or higher
- MySQL database

### Setup Steps

1. Clone the repository:
```bash
git clone <repository-url>
cd <project-directory>
```

2. Install dependencies:
```bash
npm run setup
```

3. Configure the database:
- Create a MySQL database
- Update the database settings in `core/settings.py`

4. Run migrations:
```bash
npm run makemigrations
npm run migrate
```

5. Create a superuser:
```bash
python3 manage.py createsuperuser
```

6. Start the development server:
```bash
npm start
```

The server will start at `http://localhost:3000`

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
│   ├── models/
│   │   ├── __init__.py
│   │   ├── client.py
│   │   └── project.py
│   ├── serializers/
│   │   ├── __init__.py
│   │   ├── client.py
│   │   ├── project.py
│   │   └── user.py
│   ├── views/
│   │   ├── __init__.py
│   │   ├── client.py
│   │   └── project.py
│   ├── urls.py
│   └── __init__.py
├── core/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── manage.py
├── requirements.txt
└── package.json
```
