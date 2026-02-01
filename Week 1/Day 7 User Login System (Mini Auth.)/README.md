# 🔐 Secure Login System (Python)

A command-line user authentication system built using Python, featuring password validation, hashing, and login security.

This project simulates how real-world applications handle user registration and login processes.

---

## 🚀 Features

- User registration system
- Secure login authentication
- Password hashing using SHA-256
- Username validation (minimum length rule)
- Password complexity enforcement:
  - Must contain letters
  - Must contain numbers
  - Must contain symbols
- Hidden password input using `getpass`
- Login attempt limit (3 tries)
- Data stored persistently in a file

---

## 🔒 Security Measures

| Feature | Purpose |
|---------|--------|
| Password hashing | Protects passwords from being stored in plain text |
| Login attempt limit | Prevents brute-force login attempts |
| Password complexity rules | Encourages strong passwords |
| Hidden password input | Prevents password visibility during typing |

---

## 🛠️ Technologies Used

- Python  
- `hashlib` (for password hashing)  
- `getpass` (secure password input)  
- `re` (regex validation)  
- File handling  

---

## ▶️ How to Run

Make sure Python is installed, then run:

```bash
python login_system.py
# day7-login-system
