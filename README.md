# 🎓 Grade Tracker

A simple and responsive **Grade Tracker** web application built using **Django**. It allows users to add student marks, automatically calculate the average, assign grades, determine pass/fail status, and manage student records.

---

## 📸 Preview


https://github.com/user-attachments/assets/1ee414e9-f2b6-4231-95a3-2cf1ffcd633a



## ✨ Features

- ➕ Add student records
- 📊 Automatically calculate average marks
- 🏆 Automatically assign grades
- ✅ Display Pass/Fail status
- 📈 Dashboard cards
  - Total Students
  - Class Average
  - Pass Percentage
- 🗑 Delete student records
- 🎨 Modern and responsive UI

---

## 🛠 Tech Stack

- Python
- Django
- HTML5
- CSS3
- SQLite
- Font Awesome

---

## 📂 Project Structure

```
GradeTracker/
│
├── gradeapp/
│   ├── migrations/
│   ├── templates/
│   │   └── gradetemp/
│   │       └── index.html
│   ├── static/
│   │   └── css/
│   ├── models.py
│   ├── forms.py
│   ├── views.py
│   ├── urls.py
│   └── admin.py
│
├── gradetracker/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── db.sqlite3
├── manage.py
└── README.md
```

---

## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/yourusername/GradeTracker.git
```

### Navigate to the project

```bash
cd GradeTracker
```

### Create a virtual environment

```bash
python -m venv .venv
```

### Activate the virtual environment

**Windows**

```bash
.venv\Scripts\activate
```

**Linux/Mac**

```bash
source .venv/bin/activate
```

### Install dependencies

```bash
pip install django
```

### Apply migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### Run the development server

```bash
python manage.py runserver
```

Open your browser and visit

```
http://127.0.0.1:8000/
```

---

## 📊 Grade Calculation

Average is calculated as

```
Average = (Kannada + English + Hindi + Maths) / 4
```

---

## 🏅 Grade Criteria

| Average | Grade |
|----------|-------|
| 90 - 100 | A+ |
| 80 - 89 | A |
| 70 - 79 | B |
| 60 - 69 | C |
| 50 - 59 | D |
| Below 50 | F |

---

## ✅ Pass Criteria

A student is considered **Pass** if they score **35 or more** in every subject.

Otherwise, the student is marked as **Fail**.

---

## 📸 Dashboard

The application provides:

- Total Students
- Class Average
- Pass Percentage

These values update automatically whenever a student is added or deleted.

---

## 🚀 Future Improvements

- ✏️ Update/Edit student records
- 🔍 Search students
- 📄 Pagination
- 📥 Export to Excel/PDF
- 📊 Graphs using Chart.js
- 👤 User Authentication
- 🌙 Dark Mode
- 📱 Mobile Responsive Design

---

## 📷 Screenshots

<img width="1907" height="1078" alt="Screenshot 2026-07-02 190325" src="https://github.com/user-attachments/assets/1f15d50d-b10d-463e-ba11-bf616a4da18d" />


## 👨‍💻 Author

**Navaneetha**

- GitHub: https://github.com/Navaneetha-21
- LinkedIn: https://www.linkedin.com/in/navaneetha-77712a308/

---

## 📄 License

This project is created for learning and educational purposes.

Feel free to use and modify it.
