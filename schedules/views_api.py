from schedules import app
from schedules.models import Division, Team

from flask import jsonify


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
