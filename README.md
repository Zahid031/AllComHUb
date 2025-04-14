
# 🌐 AllComHub – Dockerized Django App

This is a Dockerized version of a Django-based platform called **AllComHub**.  
It uses the default **SQLite database** and is ready to run in a containerized environment.

---

## 🐳 Docker Image

Docker Hub Image:  
➡️ [`zahid03/blog_app:v1`](https://hub.docker.com/r/zahid03/blog_app)

### 📥 Pull the image

```bash
docker pull zahid03/blog_app:v1
```

### ▶️ Run the container

```bash
docker run -d -p 8001:8001 zahid03/blog_app:v1
```

Then visit: [http://localhost:8001](http://localhost:8001)

---

## 🛠️ AllComHub – Project Overview

A Django-based website for a company featuring:
- Home
- Services
- Testimonials
- FAQ
- Blog
- Contact

Live demo 👉 [https://zahid03.pythonanywhere.com/](https://zahid03.pythonanywhere.com/)

---

## ⚙️ Local Development Setup (Non-Docker)

### 1️⃣ Clone the repository

```bash
git clone git@github.com:Zahid031/AllComHUb.git
cd AllComHUb
```

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Create the database and apply migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 4️⃣ Create a superuser (admin)

```bash
python manage.py createsuperuser
```

### 5️⃣ Start the development server

```bash
python manage.py runserver
```

Visit: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/) to access the admin dashboard.



Create Database
```bash
  python manage.py makemigrations
  python manage.py migrate
  python manage.py createsuperuser
  python manage.py runserver

```
After running the server you can go to http://127.0.0.1:8000/admin/
and customize the website as you want...

Here is the live website running on pythonanywhere

```bash
    https://zahid03.pythonanywhere.com/
```


---


