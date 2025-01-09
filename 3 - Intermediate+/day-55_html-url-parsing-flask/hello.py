from flask import Flask
app = Flask(__name__)

def bold_decorator(func):
    def wrapper():
        html = str(func())
        html_bolded = f"<b>{html}</b>"
        return html_bolded
    return wrapper

def underline_decorator(func):
    def wrapper():
        html = str(func())
        html_bolded = f"<u>{html}</u>"
        return html_bolded
    return wrapper

def emphasize_decorator(func):
    def wrapper():
        html = str(func())
        html_bolded = f"<em>{html}</em>"
        return html_bolded
    return wrapper


@app.route('/')
@bold_decorator
@underline_decorator
@emphasize_decorator
def hello_world():
    return 'Hello, World'

if __name__ == "__main__":
    app.run(debug=True)