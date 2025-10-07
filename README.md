# 🌐 Mark Vault

![Built with Django](https://img.shields.io/badge/Built%20with-Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Frontend-Bootstrap%205-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white)
![SQLite3](https://img.shields.io/badge/Database-SQLite3-003B57?style=for-the-badge&logo=sqlite&logoColor=white)
![License: MIT](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge)

---

## 🔖 Overview

**Mark Vault** is a modern, responsive **Bookmark Management System** that helps you organize your favorite links, notes, and tags — all in one secure vault.

Developed using **Django**, **Bootstrap**, and **SQLite3**, it allows users to **save, edit, delete, and search** bookmarks quickly with an intuitive interface.

Save links instantly. Organize with tags. Find them fast — anytime, anywhere.

---

## ✨ Features

- 🔗 Add, edit, and delete bookmarks  
- 🏷️ Organize with tags and categories  
- 🗒️ Add notes for better context  
- 🔍 Search and filter bookmarks instantly  
- 📱 Fully responsive Bootstrap interface  
- ⚡ Lightweight and fast  
- 💾 Persistent storage using SQLite3  

---

## 🧰 Tech Stack

| Layer | Technologies |
|--------|---------------|
| **Frontend** | HTML5, CSS3, Bootstrap 5, JavaScript |
| **Backend** | Django (Python) |
| **Database** | SQLite3 |
| **Version Control** | Git & GitHub |

---

## 📂 Project Structure

mark-vault/
├── manage.py
├── db.sqlite3
├── .git/
├── markvault/ # Django project settings
│ ├── init.py
│ ├── asgi.py
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
├── bookmarks/ # Core Django app for bookmarks
│ ├── migrations/
│ ├── templates/
│ │ └── bookmarks/
│ │ ├── index.html
│ │ ├── add_bookmark.html
│ │ └── ...
│ ├── static/
│ │ ├── css/
│ │ ├── js/
│ │ └── images/
│ ├── models.py
│ ├── views.py
│ ├── urls.py
│ └── admin.py
└── README.md


---

## ⚙️ Installation & Setup

Follow these steps to set up the project locally:

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/mark-vault.git
cd mark-vault
```

### 2️⃣ Create a Virtual Environment
```bash
python -m venv env
# Activate
env\Scripts\activate        # Windows
source env/bin/activate     # macOS/Linux
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Apply Database Migrations
```bash
python manage.py migrate
```

### 5️⃣ Run the Server
```bash
python manage.py migrate
```

###6️⃣ Access the App
```bash
http://127.0.0.1:8000/
```

---
