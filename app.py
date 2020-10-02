from dataclasses import dataclass
from datetime import datetime
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
db = SQLAlchemy(app)


@dataclass
class User(db.Model):
  id: int
  email: str

  id = db.Column(db.Integer, primary_key=True, auto_increment=True)
  email = db.Column(db.String(200), unique=True)

db.create_all()

users = User(email="user1@gmail.com"), User(email="user2x@gmail.com")
db.session.add_all(users)
db.session.commit()


@app.route('/users/')
def users():
#   users = User(email="user1@gmail.com"), User(email="user2@gmail.com")
#   db.session.add_all(users)
#   db.session.commit()

  users = User.query.all()
  return jsonify(users)  


if __name__ == "__main__":
  app.run()