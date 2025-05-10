"""
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)

os.chdir(parent_dir)
"""

from flask import Flask
from flask import render_template
from flask import url_for

# app = Flask(__name__, static_folder='../static')
app = Flask(__name__)

@app.route("/")
def init(name=None):
    return render_template("blog/index.html", person=name)

@app.route("/")
def hyperlink_to_archived_posts(name=None):
    move_to = url_for("archived_posts", name=None)
    # render_template("new_blog_posts.html", person=name)
    return render_template("archives_button.html", click = move_to)

@app.route("/archive")
def archived_posts(name=None):
    # post = <blockquote class="twitter-tweet"><p lang="en" dir="ltr">Programming monkey discovers Python JSON parsing after having done her whole saving system manually and scattered out in a txt file 🤦‍♀️ <a href="https://t.co/wTAomfY2eU">pic.twitter.com/wTAomfY2eU</a></p>&mdash; SUPERNOOB20 (@SUPERNOOB_20) <a href="https://twitter.com/SUPERNOOB_20/status/1920927904885596524?ref_src=twsrc%5Etfw">May 9, 2025</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
    # return {% include 'post_template' %}
    # return post
    return render_template("list_of_archives.html", person=name)