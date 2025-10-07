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

<img width="1886" height="857" alt="1" src="https://github.com/user-attachments/assets/f52d772d-ce8b-45f5-9efc-86bc50e57220" />

<img width="1893" height="862" alt="4" src="https://github.com/user-attachments/assets/d899c1a9-c97d-4765-a37b-62d37fdbc739" />

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

```
mark-vault/
├── manage.py
├── db.sqlite3
├── .git/
├── markvault/            # Django project settings
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── bookmarks/            # Core Django app for bookmarks
│   ├── migrations/
│   ├── templates/
│   │   └── bookmarks/
│   │       ├── index.html
│   │       ├── add_bookmark.html
│   │       └── ...
│   ├── static/
│   │   ├── css/
│   │   ├── js/
│   │   └── images/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── admin.py
└── README.md
```

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
python manage.py runserver
```

### 6️⃣ Access the App
Open your browser and go to:
```
http://127.0.0.1:8000/
```

---

## 🪄 Usage Guide

1. Launch the homepage to view your bookmarks.  
2. Add bookmarks with a title, URL, tags, and notes.  
3. Use the **search bar** to find bookmarks quickly.  
4. Edit or delete existing bookmarks as needed.  
5. Enjoy a smooth, mobile-friendly experience.

---

## 💡 Future Enhancements

- 🔐 User authentication (Login & Registration)
- 🌗 Dark mode
- ☁️ Cloud sync or backup
- 🧩 Chrome extension integration
- 📊 Analytics (Most visited links, usage trends)
- 📤 Import/export bookmarks (CSV/JSON)

---

## 🤝 Contributing

Contributions are welcome!  
Here’s how you can get started:

1. Fork this repository  
2. Create a feature branch  
   ```bash
   git checkout -b feature/new-feature
   ```
3. Commit your changes  
   ```bash
   git commit -m "Add new feature"
   ```
4. Push your branch  
   ```bash
   git push origin feature/new-feature
   ```
5. Open a Pull Request 🚀

---

## 🧾 License

This project is licensed under the **MIT License**.  
Feel free to use and modify it for your own purposes.

---

## 👨‍💻 Author

**Mark Vault**  
Created by [Clyde Charles Coelho]  
📧 Email: clydecc09.com  
🔗 GitHub: [colloid09](https://github.com/colloid09)

---

## 🌟 Support

If you found this project helpful, please ⭐ it on GitHub!  
> “Organize your web, one bookmark at a time.”
