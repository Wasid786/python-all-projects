# 🚀 Django Project Setup (From Scratch)

This guide will help you set up and run a Django project step by step on Windows.

---

## 📁 Project Structure
```
mark02/
│
├── restful01/ # Django project
│ ├── manage.py
│ ├── restful01/ # Project config
│ ├── toys/ # App
│
├── toysenv/ # Virtual environment (ignored)
├── .gitignore
├── README.md

```

---

## ⚙️ Prerequisites

- Python 3.x installed
- Git installed

---

## 🧪 Step 1: Create Virtual Environment

```bash
python -m venv toysenv
```


## Step 2: Activate Virtual Environment

```bash
toysenv\Scripts\activate
```


## 📦 Step 3: Install Django

```bash
py -m pip install django

django-admin --version
```

## 🏗️ Step 4: Create Django Project

```bash
django-admin startproject restful01
cd restful01
```


## Step 5: Create App

```bash
py manage.py startapp toys
```


## Step 6: Register App


restful01/settings.py

INSTALLED_APPS = [
    ...
    'toys',
]
## Step 7: Run Migrations

```
py manage.py makemigrations
py manage.py migrate
```


## ▶️ Step 8: Run Server

```
py manage.py runserver
```
## Optional: Check Database Tables

```
python manage.py dbshell

.tables
```


## Environment Variables (Optional)
 - DEBUG=True
 - SECRET_KEY=your-secret-key

