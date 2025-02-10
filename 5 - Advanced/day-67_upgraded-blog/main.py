import datetime
import pprint

from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
from datetime import date

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)
ckeditor = CKEditor(app)

# CREATE DATABASE
class Base(DeclarativeBase):
    pass
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# CONFIGURE TABLE
class BlogPost(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    subtitle: Mapped[str] = mapped_column(String(250), nullable=False)
    date: Mapped[str] = mapped_column(String(250), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)


with app.app_context():
    db.create_all()

# NEW POST FORM
class PostForm(FlaskForm):
    title = StringField('The blog post title', validators=[DataRequired()])
    subtitle = StringField('The subtitle', validators=[DataRequired()])
    author = StringField("The author's name", validators=[DataRequired()])
    img_url = StringField("A URL for the background image", validators=[URL()])
    body = CKEditorField('Body for the blog post')
    submit = SubmitField('Submit')


@app.route('/')
def get_all_posts():
    result = db.session.execute(db.select(BlogPost))
    posts = result.scalars().all()
    return render_template("index.html", all_posts=posts)

@app.route('/post/<int:post_id>')
def show_post(post_id):
    result = db.session.execute(db.select(BlogPost).where(BlogPost.id == post_id))
    requested_post = result.scalar()
    pprint.pprint(requested_post)
    return render_template("post.html", post=requested_post)

# TODO: add_new_post() to create a new blog post
@app.route('/new-post', methods=['GET', 'POST'])
def create_new_post():
    form = PostForm()
    if form.validate_on_submit():
        new_post = BlogPost(
            title=form.data.get('title'),
            subtitle= form.data.get('subtitle'),
            date= datetime.date.today(),
            body= form.data.get('body'),
            author= form.data.get('author'),
            img_url= form.data.get('bg_img_url'),

        )
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for('get_all_posts'))
    else:
        return render_template("make-post.html", form=form, title="New Post")

# TODO: edit_post() to change an existing blog post
@app.route('/edit-post/<int:post_id>', methods=('GET',"POST"))
def update_post(post_id):
    blog = db.get_or_404(BlogPost, post_id)
    # form = PostForm(
    #     title=blog.title,
    #     subtitle = blog.subtitle,
    #     author = blog.author,
    #     bg_img_url = blog.img_url,
    #     body = blog.body
    # )

    form = PostForm(obj=blog)

    if form.validate_on_submit():

        blog.title=form.data.get('title')
        blog.subtitle= form.data.get('subtitle')
        blog.body= form.data.get('body')
        blog.author= form.data.get('author')
        blog.img_url= form.data.get('bg_img_url')

        db.session.commit()
        return redirect(url_for('get_all_posts'))
    else:
        return render_template("make-post.html", form=form, title="Edit Post")
    pass

# TODO: delete_post() to remove a blog post from the database
@app.route('/delete/<int:post_id>')
def delete_post(post_id):
    blog = db.get_or_404(BlogPost, post_id)
    db.session.delete(blog)
    db.session.commit()

    return redirect(url_for('get_all_posts'))

# Below is the code from previous lessons. No changes needed.
@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=5003)
