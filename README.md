📚 Library Management System (LMS)

“A library is not a luxury but one of the necessities of life.” — Henry Ward Beecher

The Library Management System is a simple Django project powered by SQLite3 and HTML/CSS, built for smooth handling of library records.
This system is Admin-only, meaning all operations are controlled strictly by the administrator.

🌟 Overview

In this system, only the Admin has access to manage books and borrowing operations.
Users do not interact with the system directly. Everything goes through the admin dashboard or admin-created pages.

✅ Admin Controlled System

Only the admin can:

Add, update, and delete books

Add borrow records (issue books to users)

Mark books as returned

View all transactions

🔑 Core Features
🧾 Book Management

Add new books

Edit existing books

Remove books

Borrow  Books



📦 Borrow & Return System

Admin issues books to users

Records borrowing date and due date

Admin marks overdue books


🔐 Authentication

Django Admin Login

Secure session-based access

🏗️ Tech Stack
Component	Technology
Framework	Django 5.x
Database	SQLite3
Language	Python 3.11+
Frontend	HTML + CSS
Version Control	Git + GitHub
