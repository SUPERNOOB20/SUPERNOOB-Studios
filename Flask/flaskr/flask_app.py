"""
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)

os.chdir(parent_dir)
"""

# import os

from flask import Flask
from flask import render_template
from flask import url_for
# from flask import send_from_directory



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
    return render_template("portfolio.html", person=name)

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