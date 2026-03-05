from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow frontend access

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'  # or your DB URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Define your Post model
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    course = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(100), nullable=False)
    priority = db.Column(db.String(50), nullable=False)
    text = db.Column(db.Text, nullable=False)

# Create the database
with app.app_context():
    db.create_all()

# Your POST endpoint
@app.route('/api/posts', methods=['POST'])
def add_post():
    data = request.json
    new_post = Post(
        title=data['title'],
        course=data['course'],
        category=data['category'],
        priority=data['priority'],
        text=data['text']
    )
    db.session.add(new_post)
    db.session.commit()
    return jsonify({'message': 'Post created successfully!'}), 201

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
from flask_cors import CORS
CORS(app)
