from flask import Flask
from flask import render_template
from flask import url_for

# from osrparse import Replay

# from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column



"""
app.config["SQLALCHEMY_DATABASE_URI"] = ""mysql+mysqldb://{SUPERNOOB20}:{password}@{hostname}/{dans_leaderboard}""

class Base(DeclarativeBase):
  pass

db = SQLAlchemy(app, model_class=Base)

class User(db.Model):
    id: Mapped[int] = mapped_column(db.Integer, primary_key=True)
    username: Mapped[str] = mapped_column(db.String, unique=True, nullable=False)

with app.app_context():
    db.create_all()

    db.session.add(User(username="example"))
    db.session.commit()

    users = db.session.execute(db.select(User)).scalars()



CREATE DATABASE [IF NOT EXISTS] test_database
[CHARACTER SET charset_name]
[COLLATE collation_name];
"""




# app = Flask(__name__, static_folder='../static')
app = Flask(__name__)



                               
@app.route("/")
def init(name=None):
    return render_template("blog/index.html", person=name)

@app.route("/archive")
def archived_posts(name=None):
    return render_template("archives.html")

@app.route("/contact")
def links(name=None):
    return render_template("links.html")

@app.route("/posts")
def posts(name=None):
    return render_template("posts.html", person=name)

@app.route("/new_posts")
def new_posts(name=None):
    return render_template("new_posts_section.html", person=name)

@app.route("/dans")
def dans(name=None):
    return render_template("dans.html")

@app.route("/dans_FAQ")
def dans_FAQ(name=None):
    return render_template("dans_FAQ.html")

@app.route("/zako")
def zako(name=None):
    return render_template("blog/dans/zako.html")

@app.route("/alpha")
def alpha(name=None):
    return render_template("blog/dans/alpha.html")

@app.route("/beta")
def beta(name=None):
    return render_template("blog/dans/beta.html")

@app.route("/gamma")
def gamma(name=None):
    return render_template("blog/dans/gamma.html")

@app.route("/delta")
def delta(name=None):
    return render_template("blog/dans/delta.html")

@app.route("/epsilon")
def epsilon(name=None):
    return render_template("blog/dans/epsilon.html")

@app.route("/kami")
def kami(name=None):
    return render_template("blog/dans/kami.html")

@app.route("/lyric_composition")
def vocal_composition(name=None):
    return render_template("wind_god_girl.html")

@app.route("/vocal_covers")
def music(name=None):
    return render_template("music.html")

@app.route("/research")
def writings(name=None):
    return render_template("writings.html")





@app.route("/portfolio")
def portfolio(name=None):
    # return render_template("portfolio.html", person=name)
    return render_template("blog/portfolio_navigator.html", person=name)

@app.route("/portfolio/thumbnails")
def portfolio_thumbnails(name=None):
    # return render_template("portfolio.html", person=name)
    return render_template("blog/illustrations/thumbnails.html", person=name)

@app.route("/portfolio/vector_illustrations")
def portfolio_vector(name=None):
    # return render_template("portfolio.html", person=name)
    return render_template("blog/illustrations/vector.html", person=name)

@app.route("/portfolio/raster_illustrations")
def portfolio_raster(name=None):
    # return render_template("portfolio.html", person=name)
    return render_template("blog/illustrations/raster.html", person=name)




@app.route("/translations")
def translations(name=None):
    return render_template("translations.html")

@app.route("/siervos")
def song_siervos(name=None):
    return render_template("translations/esp_to_eng/songs/siervos.html")

@app.route("/entrevista_a_juju_kenobi")
def juju_interview(name=None):
    return render_template("translations/eng_to_esp/juju_kenobi_interview.html")

@app.route("/misc")
def credits(name=None):     # url_for('credits') will come here...! :3
    return render_template("credits.html")