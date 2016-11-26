from flask import Flask, render_template
from flask_pymongo import PyMongo
from pymongo import MongoClient

app = Flask(__name__)
mongo = PyMongo(app)


@app.route("/")
def index():
    return render_template("index.html")


@app.route('/homepage')
def home_page():
    online_users = mongo.db.neb.find({'neb_id': 1})
    return render_template('homepage.html',
        online_users=online_users)


@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)