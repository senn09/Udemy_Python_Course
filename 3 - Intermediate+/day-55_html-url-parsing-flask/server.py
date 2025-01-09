from flask import Flask
app = Flask(__name__)

def h1_decorator(func):
    def wrapper():
        html = func()
        html_h1 = f"<h1>{html}</h1>"
        return html_h1
    return wrapper

@app.route('/')
@h1_decorator
def home():
    return ("<p>Guess a number between 0 and 9</p>"
            "<img src= 'https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif' width=500>")


actual = 5
@app.route('/<int:guess>')
def check(guess):
    if guess > actual:
        return ("<p>guess lower!</p>"
                "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'>")
    elif guess < actual:
        return ("<p>guess higher!</p>"
                "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'>")
    else:
        return ("<p>guess correct!</p>"
                "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'>")

if __name__ == "__main__":
    app.run(debug=True)