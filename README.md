🎓 Mentorship Platform

A simple student–mentor mentorship platform that allows students to post queries, interact with mentors, and track academic progress. The platform includes a modern frontend interface and a Flask backend API for handling posts.

🚀 Features

🏠 Dashboard

View recent student queries

Upcoming mentoring events

Academic marketplace for study materials

📝 Post Queries

Students can submit questions with:

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

Simulated responses for demonstration

👤 Student Profile

View course progress

Academic grade visualization

🛒 Academic Marketplace

Buy or sell study materials

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

The backend is built using Flask and SQLite.

It provides an API endpoint to create posts.

Example endpoint:

POST /api/posts

Payload:

{
  "title": "Operating Systems Help",
  "course": "Computer Science & Engineering",
  "category": "Assignment Help",
  "priority": "High",
  "text": "Need help understanding scheduling algorithms."
}

The backend stores posts in a SQLite database using SQLAlchemy. 

app

💻 Frontend

The frontend is a single-page application (SPA) built using:

HTML

CSS

Vanilla JavaScript

Features include:

Navigation sidebar

Dynamic content rendering

Query posting form

Chat simulation

Profile progress charts

The frontend sends API requests to the Flask backend when submitting queries. 

index

📦 Installation
1️⃣ Clone the Repository
git clone https://github.com/yourusername/mentorship-platform.git
cd mentorship-platform
2️⃣ Install Backend Dependencies

Create a virtual environment (recommended):

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

The project uses SQLite.

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

Possible upgrades for the platform:

User authentication (login/signup)

Real-time chat using WebSockets

Mentor booking system

File upload support

Notifications system

Full marketplace with payments

👨‍💻 Author

Developed as a student mentorship platform prototype to help students connect with mentors, ask questions, and track academic progress.
