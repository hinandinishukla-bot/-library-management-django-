📚 Library Management System (LMS)

“A library is not a luxury but one of the necessities of life.” — Henry Ward Beecher

The Library Management System (LMS) is a Django-based application designed to simplify the management of books, borrowing, and user interactions.
Built using Django 5.x, SQLite3, and HTML/CSS, the system now supports both Admin and User roles and integrates with the OpenLibrary API to fetch book details automatically.

🌟 Overview

The LMS provides two types of access:

👨‍💼 Admin

Has full control over book records, users, and borrowing operations.

👤 Users

Regular users can view books, borrow books, return books, and add reviews.

The system also connects to the OpenLibrary API, enabling automatic retrieval of book information such as:

Title

Author

Cover Image

ISBN details

This reduces manual data entry and makes book management faster and more accurate.

🔑 Core Features
🧾 Book Management (Admin)

Admins can:

Add new books (with OpenLibrary auto-fill)

Edit book information

Delete books

Manage book availability

Upload or fetch book covers

📦 Borrow & Return System
Admin Capabilities

Issue books to users

Set borrowing and due dates

View overdue books

Mark books as returned

User Capabilities

Request to borrow a book

Return borrowed books

Track borrowing history

📝 Reviews & Ratings (Users)

Users can:

Add reviews to books

Rate books (1–5 stars)

Edit or delete their own reviews

🔐 Authentication & Authorization

Django’s built-in authentication system

Role-based access:

Admin → full CRUD operations

User → controlled borrowing + review features

Secure session-based login

🤖 OpenLibrary API Integration

Using the external OpenLibrary API, admins can fetch book details by:

ISBN

Title

Author

This includes:

Metadata (title, author, publisher, publish year)

High-quality book covers

Unique identifiers

This removes the need for manual entry and speeds up book registration.

🏗️ Tech Stack
Component	Technology
Framework	Django 5.x
Database	SQLite3
Language	Python 3.11+
Frontend	HTML + CSS
External API	OpenLibrary API
Version Control	Git + GitHub
🎯 Final Result

A fully functional Admin + User Library Management System with:

Modern UI

Automated book data retrieval

Borrow/return workflows

Review system

Secure role-based access
