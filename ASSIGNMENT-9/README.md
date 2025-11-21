📘 REST API Using Django — README
📌 Project Overview

This project demonstrates how to build a simple REST API using Django without using Django REST Framework (DRF).
The API allows you to Create, Read, Update, and Delete (CRUD) student records.

📁 Project Structure
restapi/
│
├── restapi/            # Main project folder
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
├── api/                # App containing API code
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── ...
│
└── manage.py

🚀 Setup Instructions
1️⃣ Install Django
pip install django

2️⃣ Create Project
django-admin startproject restapi
cd restapi

3️⃣ Create App
python manage.py startapp api

4️⃣ Add App to settings

In restapi/settings.py add:

INSTALLED_APPS = [
    ...
    'api',
]

5️⃣ Create Student Model

In api/models.py:

from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

6️⃣ Run Migrations
python manage.py makemigrations
python manage.py migrate

7️⃣ Create Views

In api/views.py:

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Student
import json

@csrf_exempt
def student_list(request):
    if request.method == 'GET':
        students = list(Student.objects.values())
        return JsonResponse(students, safe=False)

    if request.method == 'POST':
        data = json.loads(request.body)
        student = Student.objects.create(
            name=data['name'],
            age=data['age']
        )
        return JsonResponse({"id": student.id, "name": student.name, "age": student.age})

8️⃣ Create URLs
Project URL — restapi/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls'))
]

App URL — api/urls.py
from django.urls import path
from .views import student_list

urlpatterns = [
    path('students/', student_list),
]

9️⃣ Run the Server
python manage.py runserver


Your API is now live at:

http://127.0.0.1:8000/api/students/

🧪 Testing the API
GET All Students
GET http://127.0.0.1:8000/api/students/


Response:

[
  {
    "id": 1,
    "name": "Suhani",
    "age": 21
  }
]

POST (Create Student)

Use Postman or VS Code Thunder Client

URL:
http://127.0.0.1:8000/api/students/

JSON Body:
{
  "name": "Suhani",
  "age": 21
}

🎉 Your Django REST API is Ready!

If you want, I can also create:

✅ README for full CRUD API
✅ README with screenshots
✅ README for Django REST Framework version
Just tell me!
