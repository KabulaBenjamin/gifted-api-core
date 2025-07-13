
---

## 📦 Gifted Ministers KE Core API

![License](https://img.shields.io/badge/license-MIT-blue.svg)

A production-grade RESTful API built for **Gifted Ministers Kenya** using Flask, Supabase, and JWT authentication. This backend powers user profiles, songs, events, and provides secure, role-based access to administrative actions.

---

## 🧩 Features

- ✅ User authentication with Supabase JWT  
- ✅ Profile fetch and update (`/users/me`)  
- ✅ Admin-only song & event creation  
- ✅ Request validation via Pydantic models  
- ✅ Docker containerization for deployment  
- ✅ OpenAPI 3.0-compatible API docs  
- ✅ Scalable and testable project structure  

---

## 🚀 Technologies Used

| Category         | Tool                      |
|------------------|---------------------------|
| Framework        | Flask                     |
| Authentication   | Supabase + JWT            |
| Validation       | Pydantic                  |
| Deployment       | Docker + Gunicorn         |
| Documentation    | OpenAPI 3.0 / Swagger UI  |
| Testing          | Pytest                    |

---

## 🧰 Setup Instructions

### 🔑 Step 1: Clone and Initialize

```bash
git clone https://github.com/KabulaBenjamin/gifted-api-core.git
cd gifted-api-core
python -m venv venv
source venv/bin/activate  # Or use venv\Scripts\activate on Windows
```

### 📦 Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

### 🛠 Step 3: Configure `.env`

```ini
SUPABASE_URL=https://dempwwlkxthiykhxtmyt.supabase.co
SUPABASE_ANON_KEY=...
SUPABASE_SERVICE_ROLE_KEY=...
JWT_SECRET=...
FLASK_ENV=development
PORT=5000
```

---

## 🧪 Running Locally

```bash
flask run
```

Then visit: [http://localhost:5000](http://localhost:5000)

---

## 🐳 Docker Usage

```bash
docker build -t gifted-core .
docker run -p 5000:5000 --env-file .env gifted-core
```

---

## 📘 API Endpoints

### Users

| Method | Endpoint              | Description                  |
|--------|------------------------|------------------------------|
| GET    | `/api/v1/users/me`    | Get current user profile     |
| PATCH  | `/api/v1/users/me`    | Update current user info     |

### Songs

| Method | Endpoint                  | Description              |
|--------|---------------------------|--------------------------|
| GET    | `/api/v1/songs`           | List songs               |
| GET    | `/api/v1/songs/{id}`      | Get song details         |
| POST   | `/api/v1/songs` *(admin)* | Create a new song        |
| PATCH  | `/api/v1/songs/{id}` *(admin)* | Update a song      |
| DELETE | `/api/v1/songs/{id}` *(admin)* | Delete a song      |

### Events

| Method | Endpoint                    | Description                |
|--------|-----------------------------|----------------------------|
| GET    | `/api/v1/events`            | List events                |
| GET    | `/api/v1/events/{id}`       | Get event details          |
| POST   | `/api/v1/events` *(admin)*  | Create a new event         |
| PATCH  | `/api/v1/events/{id}` *(admin)* | Update an event      |
| DELETE | `/api/v1/events/{id}` *(admin)* | Delete an event      |

---

## 📝 Documentation

- OpenAPI spec: [`openapi.yaml`](./openapi.yaml)  
- Swagger UI: `http://localhost:5000/docs` *(optional setup required)*

---

## 🔬 Testing

```bash
pytest
```

Unit & integration tests should mock Supabase or use staging keys.

---

## 🤝 Contributing

1. Fork this repo  
2. Create your feature branch (`git checkout -b feature/awesome`)  
3. Commit your changes (`git commit -am 'feat: add awesome feature'`)  
4. Push and create a pull request

---

## 📄 License

This project is licensed under the [MIT License](./LICENSE).  
Feel free to use, remix, or contribute!

---


