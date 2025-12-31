# 🎓 Learning Management System – Student Module

The **Learning Management System (LMS)** is a web-based platform designed for students to access courses, assignments, quizzes, notifications, performance analytics, and more — all from one unified dashboard.

This repository contains the **Student Module (Frontend + Backend)** integrated using **HTML + Tailwind CSS + JavaScript + Django REST API**.

---

## 🚀 Features

| Module | Functionality |
|--------|--------------|
| 🔑 Authentication | Login with JWT Token authentication |
| 🏠 Dashboard | Personalized student dashboard |
| 📚 Courses | View enrolled courses & materials |
| 📝 Assignments | View / download / submit assignments |
| ❓ Quizzes | Attempt quizzes & view scores |
| 📊 Performance | GPA, progress charts & analytics |
| 🔔 Notifications | Alerts, deadlines & announcements |
| 💬 Discussion Forums | Student & Faculty community chat |
| 👤 Profile | User details & account security |

---

## 🛠️ Tech Stack

### 🔹 Frontend
- HTML5
- Tailwind CSS
- JavaScript (Fetch API)
- Chart.js (for graphs)

### 🔹 Backend
- Python 3
- Django / Django REST Framework
- Simple JWT Authentication
- SQLite Database (development)

---

## 📂 Project Structure

/lms
│
├── frontend/
│ ├── login.html
│ ├── dashboard.html
│ ├── courses.html
│ ├── assignment.html
│ ├── quizz.html
│ ├── performance.html
│ └── notification.html
│
└── backend/
├── lms_backend/
│ ├── settings.py
│ ├── urls.py
│ ├── wsgi.py
│ └── asgi.py
├── api/
│ ├── models.py
│ ├── views.py
│ ├── serializers.py
│ └── urls.py
├── students/
│ ├── models.py
│ ├── views.py
│ ├── serializers.py
│ └── urls.py
├── db.sqlite3
└── manage.py






---

## ⚙️ Setup Instructions

### 🔧 Backend Setup

```bash
cd lms-backend
python -m venv venv
venv\Scripts\activate  # Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver




### Server will start at:
http://127.0.0.1:8000/







###----------setup--------

# cd Project/lms/lms-backend
# python -m venv venv
# venv\Scripts\activate  # Windows
# pip install -r requirements.txt
# python manage.py migrate
# python manage.py createsuperuser
# python manage.py runserver# LMS-Student--Module
# LMS-Student--Module-Backend-
