from flask import Flask, render_template
import random
from datetime import datetime
import requests
app = Flask(__name__)

@app.route("/")
def home():
    age_url = "https://api.agify.io/"
    gender_url = "https://api.genderize.io/"
    param = {
        "name": "steve"
    }
    rand_num = random.randint(1, 10)
    year = datetime.now().year

    age_result = requests.get(url=age_url, params=param).json()
    age = age_result["age"]

    gender_result = requests.get(url=gender_url, params=param).json()
    gender = gender_result["gender"]


    return render_template("index.html", num=rand_num, year=year, name="steve", age=age, gender=gender)

@app.route("/<name>")
def guess(name):
    age_url = "https://api.agify.io/"
    gender_url = "https://api.genderize.io/"
    param = {
        "name": name
    }
    rand_num = random.randint(1, 10)
    year = datetime.now().year

    age_result = requests.get(url=age_url, params=param).json()
    age = age_result["age"]

    gender_result = requests.get(url=gender_url, params=param).json()
    gender = gender_result["gender"]


    return render_template("index.html", num=rand_num, year=year, name=name, age=age, gender=gender)

@app.route("/blog/<num>")
def get_blog(num):
    print(num)
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)

if __name__ == "__main__":
    app.run(debug=True)