from flask import Flask

"""
NOTES
 - getting the data from betting system
 - saving it in database
 - 
 
  - Team 
  - Amount
  - Name better
"""


app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

if __name__ == '__main__':
   app.run()