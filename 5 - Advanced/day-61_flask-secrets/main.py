from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField,SubmitField
from wtforms.validators import Email, Length
from flask_bootstrap import Bootstrap5

class MyForm(FlaskForm):
    email = StringField('Email', [Email()])
    pw = PasswordField('Password', [Length(min=8)])
    submit = SubmitField('Log In')


app = Flask(__name__)
app.secret_key = "some secret string"

bootstrap = Bootstrap5(app)

@app.route("/")
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = MyForm()
    print(form.validate_on_submit())
    if form.validate_on_submit():
        if form.email.data == "admin@email.com" and form.pw.data == "12345678":
            print(form.email.data)
            print(form.pw.data)
            return render_template('success.html')
        else:
            return render_template('denied.html')
    return render_template('login.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
