# AllComHub – Dockerized Django App

This is a Dockerized version of a Django-based Platform. It uses the default SQLite database and is ready to run in a containerized environment.

---

## Docker Image

Docker Hub Image:  
➡️ [`zahid03/blog_app:v1`](https://hub.docker.com/r/zahid03/blog_app)

Pull the image:

```bash
docker pull zahid03/blog_app:v1
'''
Run:
'''bash
docker run -d -p 8000:8000 zahid03/blog_app:v1
Access the app at: http://localhost:8000
'''



# AllComHub

A Django website for a company where Home, Services Testimonials, FAQ, Blog, Contact section is present to represent the company.
## Installation
    
## Project SetUp

Clone the project

```bash
  git@github.com:Zahid031/AllComHUb.git
```

Go to the project directory

```bash
  cd AllComHUb
```

Install dependencies

```bash
  pip install -r requirements.txt

```

Start the server

```bash
  python manage.py runserver
```
Create Database
```bash
  python manage.py makemigrations
  python manage.py migrate
  python manage.py createsuperuser
  python manage.py runserver

```
After running the server you can go to http://127.0.0.1:8000/admin/
and customize the website as you want...
Here is the website running on pythonanywhere

```bash
    https://zahid03.pythonanywhere.com/
```
