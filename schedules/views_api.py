from schedules import app, db
from schedules.models import Division, Team, Tournament

from flask import jsonify, request

import datetime


@app.route("/api/tournaments/<tournament_id>/divisions")
def divisions(tournament_id):
    """

    :param tournament_id:
    :type tournament_id:
    :return: JSON representation of divisions
    :rtype:
    """
    result = Division.query.all()
    divisions = []
    for r in result:
        division = dict()
        division['id'] = r.id
        division['group'] = r.group
        division['level'] = r.level
        division['age'] = r.age
        division['printable_id'] = r.printable_id
        division['updated'] = r.updated
        division['scoring'] = r.scoring
        divisions.append(division)
    return jsonify({'divisions': divisions})


@app.route("/api/tournaments/<tournament_id>/teams")
def teams(tournament_id):
    """
    List teams
    :return: JSON representation of teams
    :rtype: str
    """
    result = Team.query.all()
    teams = []
    for r in result:
        team = dict()
        team['id'] = r.id
        team['name'] = r.name
        team['division'] = r.division
        team['points'] = r.points
        team['goals'] = r.goals
        team['goals_against'] = r.goals_against
        team['goal_diff'] = r.goal_diff
        team['matches'] = r.matches
        teams.append(team)
    return jsonify({'teams': teams})


@app.route("/api/tournaments", methods=['GET', 'POST'])
def tournaments():
    if request.method == 'POST':
        t = Tournament(
            name=request.form['name'],
            start_date=datetime.datetime.strptime(request.form['start_date'], '%Y-%m-%d'),
            end_date=datetime.datetime.strptime(request.form['end_date'], '%Y-%m-%d')
        )
        db.session.add(t)
        db.session.commit()


    result = Tournament.query.all()
    ts = []
    for r in result:
        t = dict()
        t['id'] = r.id
        t['name'] = r.name
        t['start_date'] = r.start_date
        t['end_date'] = r.end_date
        ts.append(t)

    return jsonify({'tournaments': ts})
