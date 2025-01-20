from flask import Flask, render_template
import requests

app = Flask(__name__)

bin_url = "https://api.npoint.io/e3d97a55db81868c97b1"
bin_response = requests.get(url=bin_url)
bin_data = bin_response.json()


@app.route("/")
def home():
    return render_template("index.html", blogs=bin_data)


@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/post/<int:num>")
def post(num):
    return render_template("post.html", post_data=bin_data[num - 1])


if __name__ == "__main__":
    app.run(debug=True)
