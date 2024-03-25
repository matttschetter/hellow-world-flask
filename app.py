from flask import Flask, render_template


#This is setting up the flask app. Flask is a web framework that allows 
#you to create web applications and it acts like a server. This is the translator 
#between the front end and the back end.
app = Flask(__name__)


#@app.route. This is a route. A route is a way to navigate to a specific page on the website.
@app.route("/")
def hello():
    return render_template("index.html")
