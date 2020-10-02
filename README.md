# Flask_json
Demos how to jsonify a sqlalchemy object

From:  https://stackoverflow.com/questions/5022066/how-to-serialize-sqlalchemy-result-to-json

Outputs warnings in console but this does seem to work.  When I go to: localhost/users i get:


[
  {
    "email": "user1@gmail.com", 
    "id": 1
  }, 
  {
    "email": "user2@gmail.com", 
    "id": 2
  }
]