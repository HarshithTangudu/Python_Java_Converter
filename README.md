```markdown
# Python → Java Code Converter 🐍➡️☕

**Full Stack Web Application | Flask + Bootstrap + MySQL + REST API + CRUD**

[![Status](https://img.shields.io/badge/Status-40%25_Complete-%2336A2EB?style=flat-square&logo=github)](https://github.com/HarshithTangudu/python-java-converter)
[![Flask](https://img.shields.io/badge/Flask-3.0-000?style=flat-square&logo=flask)](https://flask.palletsprojects.com)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-7952B3?style=flat-square&logo=bootstrap)](https://getbootstrap.com)
[![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=flat-square&logo=mysql)](https://mysql.com)
[![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)](LICENSE)

## 🎯 Project Overview

A responsive web application that converts Python code snippets to equivalent Java code. Built to demonstrate **Python Full Stack skills** for developer roles.

**Converts:**
- `def function()` → `public static void function()`
- `print("Hello")` → `System.out.println("Hello")`
- Basic variable declarations and structure

## ✨ Features (Current Status)

| Feature | Status | Description |
|---------|--------|-------------|
| Responsive Bootstrap UI | ✅ Complete | Mobile-first design with Bootstrap 5 |
| Python → Java Converter | ✅ Working | Basic syntax conversion engine |
| REST API Endpoint | ✅ Ready | `POST /api/convert` for programmatic use |
| MySQL Database Schema | ✅ Prepared | `conversions` table ready |
| CRUD Operations | ⏳ Planned | Create/Read/Update/Delete conversions |
| Railway Deployment | ⏳ Tomorrow | Production deployment |

## 🛠 Tech Stack

```
Backend:     Flask 3.0, Gunicorn
Frontend:    Bootstrap 5.3, Custom CSS/JS
Database:    MySQL 8.0 (PostgreSQL compatible)
Deployment:  Railway.app
Tools:       Git, GitHub Actions
```

## 📱 Live Demo

**Local Development:** `http://127.0.0.1:5000/`  
**Production:** Deploying on Railway tomorrow 🚀

### Quick Demo
```
Input (Python):
def greet(name):
    print(f"Hello {name}!")

Output (Java):
public static void greet(name){
    System.out.println("Hello " + name + "!");
}
```

## 🏗 Project Structure

```
python-java-converter/
│
├── app.py                    # Flask app + converter logic
├── requirements.txt          # Python dependencies
├── Procfile                  # Railway deployment
├── runtime.txt              # Python version
├── database.sql             # MySQL schema
│
├── templates/               # HTML templates
│   ├── base.html           # Bootstrap layout
│   ├── index.html          # Converter form
│   ├── list.html           # Conversions list (CRUD)
│   └── result.html         # Results page
│
├── static/
│   ├── css/style.css       # Custom styles
│   └── js/converter.js     # Client-side logic
│
└── README.md               # This file!
```

## 🚀 Quick Start (Local)

```
# Clone & Install
git clone https://github.com/HarshithTangudu/python-java-converter.git
cd python-java-converter
pip install -r requirements.txt

# Run
python app.py
# Open: http://127.0.0.1:5000/
```

## 🗄 Database Setup

```
-- database.sql
CREATE DATABASE converter_db;
USE converter_db;

CREATE TABLE conversions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    py_code TEXT NOT NULL,
    java_code TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

## 🔌 REST API

```
curl -X POST http://127.0.0.1:5000/api/convert \
  -H "Content-Type: application/json" \
  -d '{"code": "def hello(): print(\"Hi\")"}'
```

**Response:**
```
{
  "java": "public static void hello(): System.out.println(\"Hi\")"
}
```

## 📈 Development Roadmap

```
graph TD
    A[40% Complete<br/>Flask + Templates] --> B[MySQL CRUD]
    B --> C[Full REST API]
    C --> D[Railway Deploy]
    D --> E[Syntax Highlighting]
    E --> F[100% Production Ready]
```

## 💼 Why Built?

**Target Job:** Python Full Stack Developer Internship  
**Skills Demonstrated:**
- Flask web framework
- Bootstrap responsive UI
- MySQL database operations
- REST API development
- Web app deployment
- CRUD operations

## 🤝 Contributing

1. Fork the repo
2. Create feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add some AmazingFeature'`)
4. Push (`git push origin feature/AmazingFeature`)
5. Open Pull Request

## 📄 License

This project is [MIT](LICENSE) licensed.

## 👨‍💻 Author

**Harshith Tangudu**  
BTech Computer Science (Data Science) | Final Year  
Hyderabad, India  

[![GitHub](https://img.shields.io/badge/GitHub-HarshithTangudu-black?style=flat-square&logo=github)](https://github.com/HarshithTangudu)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-HarshithTangudu-0077B5?style=flat-square&logo=linkedin)](https://linkedin.com/in/harshithtangudu)

---

*Built December 2025 | For Python Full Stack Developer Applications*
```

