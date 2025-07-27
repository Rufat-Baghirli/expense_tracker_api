# 💸 Expense Tracker API

This is a Django REST Framework based Expense Tracker API. It allows users to track expenses, manage categories, set budget goals, and export data.

## 🚀 Features

- JWT authentication (login/register)
- Create, update, delete transactions
- Monthly statistics
- PDF/CSV export
- Category and goal management
- Audit logging & rate limiting

## 🛠 Tech Stack

- Python 3.10+
- Django
- Django REST Framework
- SQLite (can be changed)
- JWT (Simple JWT)

## 📦 Installation

```bash
git clone https://github.com/Rufat-Baghirli/expense_tracker_api.git
cd expense_tracker_api
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
