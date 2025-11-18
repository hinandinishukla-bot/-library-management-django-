📚 Library Management System (Admin)

“A library is not a luxury but one of the necessities of life.” — Henry Ward Beecher

This is the Admin interface of the Library Management System (LMS), built using Django 5.x. It allows admins to manage books, users, borrowing/returning workflows, and overall library operations efficiently. The system integrates with the OpenLibrary API to automatically fetch book metadata.

🌟 Admin Features
1. Book Management

Add Books: Add new books manually or fetch book details automatically using OpenLibrary API (by ISBN, title, or author).

Edit Books: Update title, author, publisher, publish year, number of copies, and cover image.

Delete Books: Remove outdated or damaged books.

Manage Copies: Track total and available copies for each book.

2. Borrow & Return Management

Issue Books: Assign books to users with borrow and due dates.

Track Returns: Mark books as returned and update availability.

Overdue Monitoring: Identify and manage overdue books.

3. User Management

View Users: See registered users and their borrowing activity.

Role Management: Assign roles (Admin/User).

Deactivate Users: Block or deactivate accounts if needed.

4. Dashboard Overview

Quick statistics of all books, borrowed books, overdue returns, and reviews.

Easy navigation for managing library operations.
