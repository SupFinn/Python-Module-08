> *This project has been created as part of the 42 curriculum by rhssayn.*

# 🌌 The Matrix
### *Welcome to the Real World of Data Engineering*
---

## 📌 Description
**The Matrix** is a foundational Python project focused on mastering **essential data engineering infrastructure skills**:
virtual environments, package management, environment configuration, and system dependency handling.

Set in the *Zion Resistance Network*, you'll create isolated training environments, manage program dependencies,
configure secure systems, and build data pipelines using production-grade tools.

---

## 🎯 Project Objectives
- 🏗️ Create and manage isolated Python virtual environments
- 📦 Master package management with pip and Poetry
- 🔐 Handle sensitive configuration with environment variables
- 🛡️ Keep secrets secure and out of version control
- 🔍 Detect environment state and adapt program behavior
- 🎯 Build resilient data pipelines with proper dependency handling

---

## 🧪 Exercises Overview

### 🏛️ Exercise 0 — Entering the Matrix
Detect whether you're in a virtual environment and display Python environment information.
Learn how to provide setup instructions for creating virtual environments.

**Key Concepts:** Virtual environments, `venv`, `sys`, `site`, environment detection

---

### 📦 Exercise 1 — Loading Programs
Build a data analysis tool with pip and Poetry dependency management.
Handle missing packages gracefully and demonstrate different dependency systems.

**Key Concepts:** pip, Poetry, `requirements.txt`, `pyproject.toml`, dependency resolution

---

### 🔐 Exercise 2 — Accessing the Mainframe
Create a secure configuration system using environment variables and `.env` files.
Build a data pipeline that loads configuration safely for development and production.

**Key Concepts:** Environment variables, `.env` files, `python-dotenv`, configuration management

---

## ⚙️ Rules & Constraints
- Python **3.10+**
- Python naming conventions (snake_case)
- Handle exceptions gracefully with **try-except blocks**
- Never commit real secrets to version control
- `.env` files must be in `.gitignore`
- Test in different environments (with/without venv)

---

## 📁 Project Structure
```
your-repo/
├── ex0/construct.py
├── ex1/
│   ├── loading.py
│   ├── requirements.txt
│   └── pyproject.toml
└── ex2/
    ├── oracle.py
    ├── .env.example
    └── .gitignore
```

---

## 🚀 Execution
```bash
python3 ex0/construct.py
python3 ex1/loading.py
python3 ex2/oracle.py
```

Or with virtual environment:
```bash
python3 -m venv matrix_env
source matrix_env/bin/activate

python3 ex0/construct.py
python3 ex1/loading.py
python3 ex2/oracle.py
```

---

## 🧠 Environment Layers

| Layer | Exercise | Purpose |
|-------|----------|---------|
| **Foundation** | Ex0 | Virtual environments and isolation |
| **Dependencies** | Ex1 | Managing packages and libraries |
| **Configuration** | Ex2 | Securing application settings |

---

## 🧪 Exercise Details

### Exercise 0: Entering the Matrix
Detect virtual environment status and display environment information.

**Objectives:**
- Detect if running inside a virtual environment
- Display Python environment information
- Show package installation paths
- Provide venv creation instructions

**Expected Output (outside venv):**
```
MATRIX STATUS: You're still plugged in
Virtual Environment: None detected
WARNING: You're in the global environment!

To enter the construct, run:
  python -m venv matrix_env
  source matrix_env/bin/activate
```

---

### Exercise 1: Loading Programs
Demonstrate package management with pip and Poetry.

**Objectives:**
- Show package management with pip
- Create reproducible dependency files
- Handle missing dependencies gracefully
- Compare pip vs Poetry workflows

**Expected Output:**
```
LOADING STATUS: Loading programs...
Checking dependencies:
[OK] pandas (2.1.0) - Data manipulation ready
[OK] requests (2.31.0) - Network access ready
[OK] matplotlib (3.7.2) - Visualization ready

Analysis complete!
```

---

### Exercise 2: Accessing the Mainframe
Load configuration from environment variables and `.env` files.

**Objectives:**
- Load configuration from environment variables
- Use `.env` files for development
- Support development and production modes
- Demonstrate secret management

**Configuration Variables:**
- `MATRIX_MODE` - "development" or "production"
- `DATABASE_URL` - Connection string
- `API_KEY` - Secret key for services
- `LOG_LEVEL` - Logging verbosity
- `ZION_ENDPOINT` - Network URL

**Expected Output:**
```
ORACLE STATUS: Reading the Matrix...
Configuration loaded:
Mode: development
Database: Connected to local instance
API Access: Authenticated

Environment security check:
[OK] No hardcoded secrets detected
[OK] .env file properly configured
```

---

## 📦 Authorized Imports

**Exercise 0:** sys, os, site, print()

**Exercise 1:** pandas, requests, matplotlib, numpy, sys, importlib

**Exercise 2:** os, sys, python-dotenv, file operations

---

## 🎓 Learning Outcomes

✅ Create and activate virtual environments  
✅ Understand dependency management  
✅ Use pip and freeze dependencies  
✅ Manage projects with Poetry  
✅ Load configuration from environment variables  
✅ Use `.env` files safely  
✅ Keep secrets out of version control  
✅ Build production-ready applications  

---

## 🔐 Security Best Practices

1. **Never commit `.env` files** — Add to `.gitignore`
2. **Use `.env.example`** — Show what variables are needed
3. **Environment variables override `.env`** — Production flexibility
4. **Use `python-dotenv`** — Don't parse manually
5. **Validate configuration** — Check required variables
6. **Log safely** — Never log secrets
7. **Rotate secrets** — Change keys regularly

---

## 👤 Author

*Created as part of the 42 curriculum — Real World Data Engineering*

If this project helped you, feel free to ⭐ the repository on GitHub!

**Virtual environments, package management, and secure configuration are the foundation of professional Python development.** 🔴✨