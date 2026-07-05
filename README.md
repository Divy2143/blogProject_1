# blogProject

A Django blog project — setup guide, error log, and command reference.

---

## 📋 Errors, Fixes & Learnings (chronological)

1. **HTML without quotes in `HttpResponse`** → Python needs strings quoted; `HttpResponse("<h1>...</h1>")`. *Learning: Python treats bare text as code, not data — strings need quotes.*
2. **`include('posts/urls.py')` wrong** → should be `include('posts.urls')`. *Learning: Python imports use dot notation (module paths), not file paths.*
3. **Trailing commas after model fields** → turned `title = CharField(...)` into a tuple. *Learning: commas are for collections `[]{}()`, not statement separators — Python uses newlines for that.*
4. **New Django project = new empty database** → old superuser credentials don't carry over. *Learning: each project has its own isolated SQLite file; code and data are separate.*
5. **`Posts` model not showing in admin panel** → needed `admin.site.register(Posts)` in `admin.py`. *Learning: existing data ≠ automatically exposed in an interface; must explicitly register/wire it up.*
6. **`post/6/` → 404 Page Not Found** → URL pattern was `post/<int:post_id>` (no trailing slash) but link produced `post/6/` (with slash) — exact string mismatch. *Learning: Django URL matching is literal; trailing slash consistency matters.*

---

## Setup Guide

### PHASE 1 — One-Time Machine Setup *(do this only once per computer)*

**Install Python**
- Go to python.org and download the latest stable version
- During installation — check "Add Python to PATH"
- 💡 Without adding to PATH, terminal commands like `python` and `pip` won't work

**Install Git**
- Go to git-scm.com and download for Windows 64-bit
- Recommended settings during installation:
  - Default editor → Use Visual Studio Code
  - Initial branch name → Override → type: `main`
  - PATH environment → Git from command line and 3rd-party software
  - All other options → Keep defaults

**Connect Git to Your Identity** *(do this once)*
- 💡 This attaches your name and email to every commit you make.

### PHASE 2 — Per Project Setup *(do this for every new Django project)*

- Create and navigate to your project folder
- Create a virtual environment
- Activate the virtual environment — you'll see `(.venv)` appear at the start of your terminal line when active
- Install Django
- Create the Django project — 💡 the trailing `.` means "create project files here," avoiding an extra nested folder
- Verify Django works by visiting `http://127.0.0.1:8000`
- Create Django apps (features) — 💡 each "app" is a self-contained feature of your project, e.g. blog, store, wordcounter

### PHASE 3 — Git Initialisation *(do once per project, after creating the project)*

- Initialise Git — 💡 creates a hidden `.git` folder, Git's internal diary for your project
- Create a `.gitignore` file with this content:
  ```
  .venv/
  __pycache__/
  *.pyc
  db.sqlite3
  .env
  ```
  **What each line ignores:**
  - `.venv/` → your virtual environment — thousands of files anyone can recreate
  - `__pycache__/` → Python's auto-generated speed-boost files
  - `*.pyc` → compiled Python files — auto-generated, irrelevant to others
  - `db.sqlite3` → your local database — contains your data, not for sharing
  - `.env` → secret keys and passwords — NEVER goes to GitHub
- Stage all files — 💡 the `.` means "stage everything," but `.gitignore` protects listed files from being staged
- Make your first commit — 💡 `-m` lets you write the commit message directly in the command

### PHASE 4 — GitHub Connection *(do once per project)*

- Create a new repository on GitHub
  - Go to github.com → click + → New repository
  - Give it a name matching your project folder
  - Do NOT check "Add README" or "Add .gitignore" — you already have them
  - Click Create repository
- Connect local project to GitHub — 💡 "origin" is just a nickname for your GitHub repo, industry standard convention
- Push your code to GitHub — 💡 `-u` means "remember this connection," next time you just type `git push`

### PHASE 5 — Ongoing Development Workflow *(repeat forever as you build features)*

After every meaningful change or feature: stage → commit → push.

**When to commit:**
- After fixing a bug
- After completing a feature
- Before trying something risky or experimental
- Before closing your laptop for the day

> Remember: Git is local. GitHub is the cloud. You need both.
> commit often · push before you close your laptop · always `.gitignore` your secrets

---

## 💻 Terminal Commands (chronological)

```bash
# One-time machine setup
git config --global user.name "YourName"
git config --global user.email "your@email.com"

# Per-project setup
mkdir myProject
cd myProject
python -m venv .venv
.venv\Scripts\activate          # Windows
source .venv/bin/activate       # Mac / Linux
pip install django
django-admin startproject myProject .
python manage.py runserver
python manage.py startapp myapp

# File creation (Windows terminals)
touch file.py                   # Linux / Mac / Git Bash
New-Item file.py                # PowerShell
type nul > file.py              # Command Prompt (cmd)

# Git initialisation
git init
New-Item .gitignore             # Windows
touch .gitignore                # Mac / Linux
git add .
git commit -m "Initial project setup"

# GitHub connection
git remote add origin https://github.com/YourUsername/YourRepo.git
git push -u origin main

# Django database & admin setup
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

# Ongoing development workflow (repeat)
git status
git add .
git commit -m "Describe what you did"
git push
git log
git pull
```

### Quick Command Reference

| Command | What It Does |
|---|---|
| `git init` | Start tracking a folder with Git |
| `git add .` | Stage all changed files for commit |
| `git add filename` | Stage a specific file only |
| `git commit -m "msg"` | Save a snapshot with a label |
| `git status` | See what files have changed |
| `git log` | See history of all commits |
| `git push` | Send commits to GitHub |
| `git pull` | Get latest changes from GitHub |
| `git remote add origin <url>` | Connect local project to GitHub |
| `python manage.py makemigrations` | Generate migration files from model changes |
| `python manage.py migrate` | Build database tables from migrations |
| `python manage.py createsuperuser` | Create admin login credentials |
| `python manage.py runserver` | Start the local dev server |
| `python manage.py startapp <name>` | Create a new Django app |
