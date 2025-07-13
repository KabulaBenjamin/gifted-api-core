
# Gifted Ministers KE Core API

A production-ready backend API for Gifted Ministers Kenya, built with Flask, Supabase, JWT authentication, and Pydantic validation. This service powers user profiles, song and event management, and secures access with role-based controls.

---

## Features

- User authentication and profile management  
- CRUD operations for songs and events  
- JWT-based security with admin role restrictions  
- Request validation using Pydantic models  
- Comprehensive OpenAPI 3.0 documentation  
- Dockerized deployment with Gunicorn  
- Environment-driven configuration  

---

## Prerequisites

- Python 3.10 or higher  
- pip package manager  
- Git client  
- Supabase project (URL, anon key, service role key)  
- Docker & Docker Compose (optional, for containerization)  

---

## Getting Started

### Clone the Repository

```bash
git clone https://github.com/KabulaBenjamin/gifted-api-core.git
cd gifted-api-core
```

### Create and Activate a Virtual Environment

```bash
python -m venv venv
```

On Windows:

```bash
venv\Scripts\activate
```

On macOS/Linux:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment Variables

Create a file named `.env` in the project root with these values:

```ini
SUPABASE_URL=https://dempwwlkxthiykhxtmyt.supabase.co
SUPABASE_ANON_KEY=<your-public-anon-key>
SUPABASE_SERVICE_ROLE_KEY=<your-service-role-key>
JWT_SECRET=<your-jwt-secret>
FLASK_ENV=development
PORT=5000
```

---

## Running Locally

Start the Flask development server:

```bash
flask run
```

The healthcheck endpoint will respond at:  
http://localhost:5000/

---

## Docker Deployment

Build the Docker image:

```bash
docker build -t gifted-core .
```

Run the container, passing in your environment file:

```bash
docker run -p 5000:5000 --env-file .env gifted-core
```

Your API is now available at http://localhost:5000/.

---

## API Documentation

The API adheres to OpenAPI 3.0. You can explore the full specification in `openapi.yaml`.

### Interactive Docs with Swagger UI

If you embed Swagger UI, visit:

```
http://localhost:5000/docs
```

### Raw OpenAPI Spec

Download or view directly at:

```
http://localhost:5000/openapi.yaml
```

---

## Available Endpoints

### Users

- **GET** `/api/v1/users/me`  
  Fetch the authenticated user’s profile.

- **PATCH** `/api/v1/users/me`  
  Update the authenticated user’s profile fields.

### Songs

- **GET** `/api/v1/songs`  
  List all songs.

- **GET** `/api/v1/songs/{song_id}`  
  Retrieve a specific song.

- **POST** `/api/v1/songs` *(admin only)*  
  Create a new song.

- **PATCH** `/api/v1/songs/{song_id}` *(admin only)*  
  Update song details.

- **DELETE** `/api/v1/songs/{song_id}` *(admin only)*  
  Delete a song.

### Events

- **GET** `/api/v1/events`  
  List all events.

- **GET** `/api/v1/events/{event_id}`  
  Retrieve a specific event.

- **POST** `/api/v1/events` *(admin only)*  
  Create a new event.

- **PATCH** `/api/v1/events/{event_id}` *(admin only)*  
  Update event details.

- **DELETE** `/api/v1/events/{event_id}` *(admin only)*  
  Delete an event.

---

## Testing

Run the full test suite with:

```bash
pytest
```

Ensure you configure a test database or mock Supabase client for integration tests.

---

## Contributing

- Fork the repository and create a feature branch.  
- Implement your changes and add tests.  
- Submit a pull request with a descriptive title and summary.  

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
