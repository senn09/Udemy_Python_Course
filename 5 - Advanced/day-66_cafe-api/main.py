import random
from struct import error

from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean

'''
Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)

# CREATE DB
class Base(DeclarativeBase):
    pass
# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)

    def to_dict(self):
        # gets all columns from the table and returns a dictionary
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


# HTTP GET - Read Record
@app.route("/random")
def get_random_cafe():
    # gets all the cafes from the db as a list
    result = db.session.execute(db.select(Cafe))
    all_cafe = result.scalars().all()
    random_cafe = random.choice(all_cafe)

    return jsonify(cafe=random_cafe.to_dict())

@app.route("/all")
def get_all_cafes():
    result = db.session.execute(db.select(Cafe))
    all_cafe = result.scalars().all()

    return jsonify(cafe={i:all_cafe[i].to_dict() for i in range(len(all_cafe))})

@app.route("/search")
def search():
    loc = request.args.get('loc')
    result = db.session.execute(db.select(Cafe).where(Cafe.location == loc))
    location_matched_cafes = result.scalars().all()

    if location_matched_cafes:
        return jsonify(cafe={i:location_matched_cafes[i].to_dict() for i in range(len(location_matched_cafes))})
    else:
        return jsonify(error="No where to be found"), 404

# HTTP POST - Create Record
@app.route("/add", methods=["POST"])
def post_new_cafe():
    new_cafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("loc"),
        has_sockets=bool(request.form.get("sockets")),
        has_toilet=bool(request.form.get("toilet")),
        has_wifi=bool(request.form.get("wifi")),
        can_take_calls=bool(request.form.get("calls")),
        seats=request.form.get("seats"),
        coffee_price=request.form.get("coffee_price"),
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"success": "Successfully added the new cafe."})

# HTTP PUT/PATCH - Update Record
@app.route("/update_price/<int:id>")
def update_coffe_price(id):
    cafe = db.session.get(Cafe, id)
    if cafe:
        new_price = request.args.get('new_price')
        cafe.coffee_price = new_price
        db.session.commit()
        return jsonify(sucess="done!"), 200
    else:
        return jsonify(error="no cafe found with that id"), 400



# HTTP DELETE - Delete Record
@app.route("/report-closed/<cafe_id>", methods=["Delete"])
def delete(cafe_id):
        if request.args.get("api-key") == "TopSecretAPIKey":
            cafe = db.session.get(Cafe, cafe_id)
            if cafe:
                db.session.delete(cafe)
                db.session.commit()

                return jsonify(success="done!"), 200
            else:
                return jsonify(error="no cafe found!"), 400
        else:
            return jsonify(error="invalid apikey!"), 400


if __name__ == '__main__':
    app.run(debug=True)
