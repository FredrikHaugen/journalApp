# InsightInk

---

## Description

My Journal App/InsightInk is a web-based journaling platform designed for individuals seeking a simple and intuitive space to document their thoughts, memories, and daily reflections. By leveraging the power of the Flask framework and SQLite3, I've created a robust platform that combines user-friendly features with a minimalistic design approach.

The core functionalities of the application include user registration, authentication, and the ability to create, view, and manage personal journal entries. Each journal entry is securely associated with an individual user account, ensuring data privacy and a personalized user experience.

The design of the application is intentionally minimalistic, reflecting my personal style preference. Opting for a stripped-back aesthetic allows users to focus entirely on the content, eliminating potential distractions.

Internally, I prioritized using existing packages to optimize my development workflow. I employed several Flask extensions, including flask_sqlalchemy for database operations, werkzeug.security for password management, flask_wtf for form handling, and flask_login for user session management. One notable challenge I embraced during the development process was reverting to using plain CSS for styling. Having worked extensively with ReactJS and Tailwind recently, diving back into pure CSS was both a nostalgic journey and an opportunity to re-familiarize myself with the foundational aspects of web design.

In today's fast-paced world, there's a growing need for digital spaces that promote introspection and mindfulness. My Journal App/InsightInk seeks to address this demand by offering a straightforward platform for users to chronicle their experiences, thoughts, and feelings. Whether used for daily reflections, capturing memories, or setting goals, this platform encourages users to engage in purposeful self-expression.

---

## Demo

[https://www.youtube.com/watch?v=ZPwi7rZd284]

---

## Features

- **User Authentication**: Secure login and registration system to protect your journals.
- **Rich Text Editor**: An intuitive editor to embellish your journal entries.
- **Responsive Design**: Optimal viewing experience across a wide range of devices, from desktop to mobile.
- **Private entries**: Well built for achieving optimal user privacy.

---

## Technologies Used

- **Backend**: Flask (Python web framework)
- **Frontend**: HTML, CSS, JavaScript
- **Database**: SQLite3

---

## How to Use

1. **Registration**: Start by registering an account on the platform using a valid email address.
2. **Login**: After registration, log in to access your personal journal dashboard.
3. **Create Entry**: Click on the "New Entry" button to start writing a new journal entry.
4. **Edit and Delete**: Access past entries from the "View Entries" and choose to edit or delete them as needed.

---

## Setup and Installation

For developers who wish to run the project locally:

1. **Clone the Repository**:

   git clone [https://github.com/FredrikHaugen/journalApp.git]

2. **Navigate to Project Directory**:

   cd journal_app

3. **Install Required Packages**:

   pip install -r requirements.txt

4. **Run the Application**:

   python app.py
