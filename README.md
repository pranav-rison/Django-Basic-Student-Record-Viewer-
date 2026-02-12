# Django Student Record Viewer

A simple Django application that displays student records (Name, Grade, Department) stored in a database using Django ORM and templates.

This project is built for learning and practicing basic Django concepts such as models, views, templates, admin panel, and URL routing.

---

## 🚀 Features

- Student model with name, grade, and department
- Admin panel integration
- SQLite database (default Django DB)
- Dynamic data rendering using Django Template Language
- Simple table-style layout in HTML

---

## 🛠 Technologies Used

- Python
- Django
- SQLite
- HTML
- Django Template Language (DTL)

---

## 📁 Project Structure

```
django-student-app/
│
├── manage.py
├── minimini/              # Project settings
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
├── main/                  # Django app
│   ├── models.py
│   ├── views.py
│   ├── admin.py
│   ├── templates/
│   │   └── home.html
│   └── ...
```

---

## 🗄 Student Model

```python
from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    grade = models.CharField(max_length=1)
    department = models.CharField(max_length=15)

    def __str__(self):
        return self.name
```

---

## 👨‍💻 View Function

```python
from django.shortcuts import render
from .models import Student

def home(request):
    stud = Student.objects.all()
    return render(request, "home.html", {"student": stud})
```

---

## 🌐 URL Configuration

```python
from django.contrib import admin
from django.urls import path
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
]
```

---

## ▶️ How to Run the Project

### 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/django-student-app.git
cd django-student-app
```

### 2️⃣ Create Virtual Environment (Optional)

```bash
python -m venv venv
```

Activate it:

Windows:
```bash
venv\Scripts\activate
```

Mac/Linux:
```bash
source venv/bin/activate
```

### 3️⃣ Install Django

```bash
pip install django
```

### 4️⃣ Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5️⃣ Create Superuser

```bash
python manage.py createsuperuser
```

### 6️⃣ Run Server

```bash
python manage.py runserver
```

Open in browser:

Home Page:
```
http://127.0.0.1:8000/
```

Admin Panel:
```
http://127.0.0.1:8000/admin/
```

---

## 🎯 Learning Objectives

This project helps in understanding:

- Django Models
- Django Admin
- QuerySets
- Template Rendering
- URL Routing
- Basic MVC (MVT) Architecture in Django

---

## 🔮 Future Improvements

- Add CRUD operations (Create, Update, Delete)
- Add Bootstrap styling
- Add search functionality
- Add pagination
- Add frontend form to insert students

---

## 📜 License

This project is created for educational purposes.
