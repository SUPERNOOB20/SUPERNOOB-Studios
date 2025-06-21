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

"""
app.add_url_rule(
    "/favicon.ico",
    endpoint="favicon",
    redirect_to=url_for("static", filename="favicon.ico")
)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')
"""
                               
@app.route("/")
def init(name=None):
    return render_template("blog/index.html", person=name)

# @app.route("/archive")
# def hyperlink_to_archived_posts(name=None):
    # move_to = url_for("archived_posts", name=None)
    # return render_template("archives.html", click = move_to)

@app.route("/archive")
def archived_posts(name=None):
    return render_template("archives.html")

@app.route("/contact")
def links(name=None):
    return render_template("links.html")

@app.route("/posts")
def new_posts(name=None):
    # post = <blockquote class="twitter-tweet"><p lang="en" dir="ltr">Programming monkey discovers Python JSON parsing after having done her whole saving system manually and scattered out in a txt file 🤦‍♀️ <a href="https://t.co/wTAomfY2eU">pic.twitter.com/wTAomfY2eU</a></p>&mdash; SUPERNOOB20 (@SUPERNOOB_20) <a href="https://twitter.com/SUPERNOOB_20/status/1920927904885596524?ref_src=twsrc%5Etfw">May 9, 2025</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
    # return {% include 'post_template' %}
    # return post
    return render_template("new_posts_section.html", person=name)

@app.route("/lyric_composition")
def vocal_composition(name=None):
    return render_template("wind_god_girl.html")

@app.route("/vocal_covers")
def music(name=None):
    return render_template("music.html")

@app.route("/portfolio")
def portfolio(name=None):
    return render_template("portfolio.html", person=name)

@app.route("/translations")
def translations(name=None):
    return render_template("translations.html")

@app.route("/entrevista_a_juju_kenobi")
def juju_interview(name=None):
    return render_template("translations/eng_to_esp/juju_kenobi_interview.html")