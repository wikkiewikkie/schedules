from flask import render_template

from schedules import app
from schedules.models import Division, Field, Printable, Team


@app.route("/")
def index():
    return render_template("index.html",
                           divisions=Division.query.all(),
                           printables=Printable.query.all())


@app.route("/divisions/<number>")
def division(number):
    d = Division.query.get(number)
    return render_template("division.html", division=d)


@app.route("/fields/<number>")
def field(number):
    f = Field.query.get(number)
    return render_template("field.html", field=f)


@app.route("/printables/<number>")
def printable(number):
    return number


@app.route("/teams/<number>")
def team(number):
    t = Team.query.get(number)
    return render_template("team.html", team=t)