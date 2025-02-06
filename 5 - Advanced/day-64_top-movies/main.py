from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from movie_search import MovieSearch

MovieSearcher = MovieSearch()

class UpdateForm(FlaskForm):
    rating = StringField('Your Rating out of 10 (e.g. 7.5)', validators=[DataRequired()])
    review = StringField('Your Review', validators=[DataRequired()])
    submit = SubmitField('Submit')

class AddForm(FlaskForm):
    title = StringField("Name of the Movie", validators=[DataRequired()])
    submit = SubmitField('Submit')

# CREATE DB
class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movies.db"
Bootstrap5(app)

db.init_app(app)

# CREATE TABLE
class Movie(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(String, nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)
    ranking: Mapped[int] = mapped_column(Integer, nullable=False)
    review: Mapped[str] = mapped_column(String, nullable=False)
    img_url: Mapped[str] = mapped_column(String, nullable=False)

with app.app_context():
    db.create_all()

@app.route("/")
def home():
    movies = db.session.execute(db.select(Movie).order_by(Movie.rating)).scalars().all()

    for i in range(len(movies)):
        movies[i].ranking = len(movies) - i
    db.session.commit()

    return render_template("index.html", movies=movies)

@app.route("/edit/<int:id>", methods=['GET', 'POST'])
def edit(id):
    form = UpdateForm()
    if form.validate_on_submit():
        movie_to_update = db.get_or_404(Movie, id)
        movie_to_update.rating = form.rating.data
        movie_to_update.review = form.review.data
        db.session.commit()
        return redirect(url_for('home'))
    else:
        movie = db.get_or_404(Movie, id)
        title = movie.title
        return render_template('edit.html', form=form, title=title)

@app.route('/delete/<int:id>')
def delete(id):
    movie_to_delete = db.get_or_404(Movie, id)
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/add', methods=['GET', 'POST'])
def add():
    form = AddForm()
    if form.validate_on_submit():
        return redirect(url_for('select', title=form.title.data))
    else:
        return render_template('add.html', form=form)

@app.route('/select')
def select():
    if 'title' in request.args:
        searched_movies = MovieSearcher.title_search(request.args.get("title"))
        return render_template('select.html', searched_movies=searched_movies)
    elif 'selected_movie' in request.args:
        movie_id = (request.args.get("selected_movie"))
        selected_movie = MovieSearcher.id_search(movie_id)
        movie_to_add = Movie(
            title=selected_movie['title'],
            year=selected_movie['release_date'].split('-')[0],
            description=selected_movie['overview'],
            rating=7.3,
            ranking=9,
            review="",
            img_url=f"https://image.tmdb.org/t/p/w500{selected_movie['poster_path']}"
        )
        db.session.add(movie_to_add)
        db.session.commit()

        movie = db.session.execute(db.select(Movie).where(Movie.title == selected_movie['title'])).scalar()
        movie_id = movie.id
        return redirect(url_for('edit', id=movie_id))

if __name__ == '__main__':
    app.run(debug=True)


