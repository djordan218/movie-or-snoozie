from flask import Flask, render_template
from forms import MovieSearchForm

# from models import db, connect_db, User
from key import API_KEY
import requests
import os

# CURR_USER_KEY = "curr_user"

app = Flask(__name__)

uri = os.getenv(
    "DATABASE_URL", "postgresql://postgres:password@127.0.0.1:5432/movie_or_snoozie"
)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "iamasecretkey123456")


####### HOMEPAGE & USER HANDLING #############
@app.route("/")
def homepage():
    """Show homepage"""
    form = MovieSearchForm()
    return render_template("index.html", form=form)


################# API REQUESTS ##########################


@app.route("/movie_search", methods=["GET", "POST"])
def load_movie():
    form = MovieSearchForm()
    API_URL = "http://www.omdbapi.com/?"
    search_term = form.movie.data
    res = requests.get(API_URL, params={"apikey": API_KEY, "s": search_term})
    movies = res.json()
    return render_template("index.html", form=form, movies=movies)
