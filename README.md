🎓 Mentorship Platform

An easy-to-use student–mentor mentorship platform on which students can publish questions, communicate with mentors, and monitor academic outcomes. It has a modern front end interface, and a Flask backend API to process posts.

🚀 Features

🏠 Dashboard

View student queries recently received.

Upcoming mentoring events

Academic marketplace to buy and sell study materials.

📝 Post Queries

Students may include questions with:

Title

Course

Category

Priority

Description

👥 Mentor Meetings

Connect with mentors and faculty

Simulated meeting interface

💬 Chat System

Chat with mentors

Example responses (simulated)

👤 Student Profile

View course progress

Academic grade visualization

🛒 Academic Marketplace

Purchase or sell Study materials.

🏗️ Project Structure
mentorship-platform/
│
├── backend/
│   └── app.py          # Flask backend API
│
├── frontend/
│   ├── index.html      # Main UI
│   ├── styles.css      # Styling
│   └── scripts.js      # Frontend logic
│
├── database/
│   └── posts.db        # SQLite database (auto-created)
│
└── README.md
⚙️ Backend (Flask API)

It will be developed with Flask and SQLite for the backend.

It provides an API endpoint to create posts.

Example endpoint:

POST /api/posts

Payload:

{
  Maintaining the system.Help in operating systems.
  The course is Computer Science & Engineering,
  "category": "Assignment Help",
  "priority": "High",
  Need help in understanding scheduling algorithms.
}

Posts are stored in a SQLite database in the back-end using SQLAlchemy. 

app

💻 Frontend

The front end is a single page application (SPA) with:

HTML

CSS

Vanilla JavaScript

Features include:

Navigation sidebar

Dynamic content rendering

Query posting form

Chat simulation

Profile progress charts

When making a query, the frontend communicates with the Flask backend via the API. 

index

📦 Installation
1️⃣ Clone the Repository
git clone https://github.com/Himanshu-133/mentorship-platform.git
cd mentorship-platform
2️⃣ Install Backend Dependencies

Build virtual environment (Optional):

python -m venv venv

Activate it:

Mac/Linux

source venv/bin/activate

Windows

venv\Scripts\activate

Install packages:

pip install flask flask_sqlalchemy flask_cors
3️⃣ Run the Backend
python app.py

Server will start at:

http://127.0.0.1:5000
4️⃣ Run the Frontend

Simply open:

index.html

in your browser.

🗄️ Database

The project is implemented with SQLite.

The database file:

posts.db

is automatically created when the Flask app starts. 

app

🛠️ Technologies Used

Frontend

HTML5

CSS3

JavaScript

Backend

Flask

SQLAlchemy

Flask-CORS

Database

SQLite

📸 Future Improvements

Platform improvements that could be implemented:

User authentication (login/signup)

Live chat support with WebSockets.

Mentor booking system

File upload support

Notifications system

To add to a marketplace with payments.To add a marketplace with payments.

👨‍💻 Author

Created as a prototype for a student mentorship platform to meet the needs of the students of the platform to connect with mentors, ask questions and monitor their academic development.
