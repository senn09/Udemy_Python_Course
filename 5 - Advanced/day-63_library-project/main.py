from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float

class Base(DeclarativeBase):
    pass

# initialise the db object
db = SQLAlchemy(model_class=Base)

# create the app
app = Flask(__name__)
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"
# initialize the app with the extension
db.init_app(app)

class Book(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[str] = mapped_column(Float, nullable=False)

    def __repr__(self):
        return f'<Book {self.title}>'

# Create the table
with app.app_context():
    db.create_all()

@app.route('/')
def home():
    all_books = []
    result = db.session.execute(db.select(Book).order_by(Book.title))
    all_books = result.scalars().all()
    return render_template('index.html', all_books=all_books)

@app.route("/add", methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        new_book = Book(title=request.form.get('Book Name'), author=request.form.get('Book Author'), rating=request.form.get('Rating'))
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for('home'))

    else:
        return render_template('add.html')

@app.route("/edit/<int:book_id>", methods=['GET', 'POST'])
def edit(book_id):
    book_to_update = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()

    if request.method == 'POST':
        book_to_update.rating = request.form.get('New Rating')
        db.session.commit()
        return redirect(url_for('home'))
    else:
        return render_template('edit.html', book=book_to_update)

@app.route("/delete")
def delete():
    book_id = request.args.get('book_id')

    book_to_delete = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for('home'))




if __name__ == "__main__":
    app.run(debug=True)

