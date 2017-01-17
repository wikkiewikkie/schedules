from schedules import db


class Division(db.Model):
    __tablename__ = "divisions"
    id = db.Column(db.Integer, primary_key=True)
    group = db.Column(db.String(20), nullable=False)
    level = db.Column(db.String(10))
    age = db.Column(db.String(12), nullable=False)
    printable_id = db.Column(db.Integer, db.ForeignKey('printables.id'))
    updated = db.Column(db.DateTime)
    scoring = db.Column(db.Boolean)

    finals = db.relationship('Final', backref='division')
    matches = db.relationship('Match', backref='division')
    teams = db.relationship('Team', backref='div')

    def __repr__(self):
        return '<Division {}>'.format(self.id)

    def groups(self):
        g = dict()
        for team in self.teams:
            group = team.id[2]
            if group not in g:
                g[group] = []
            g[group].append(team)
        return g


class Field(db.Model):
    __tablename__ = "fields"
    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String(48))
    tent = db.Column(db.Integer)


class Final(db.Model):
    __tablename__ = "finals"
    id = db.Column(db.Integer, primary_key=True)
    division_id = db.Column(db.Integer, db.ForeignKey('divisions.id'), nullable=False)
    date = db.Column(db.Date, nullable=False)
    time = db.Column(db.Time, nullable=False)
    description = db.Column(db.String(60))
    home = db.Column(db.String(80), nullable=False)
    home_actual = db.Column(db.String(4), db.ForeignKey('teams.id'))
    home_score = db.Column(db.Integer)
    away = db.Column(db.String(80), nullable=False)
    away_actual = db.Column(db.String(4), db.ForeignKey('teams.id'), nullable=False)
    away_score = db.Column(db.Integer)
    field = db.Column(db.Integer, nullable=False)


class Match(db.Model):
    __tablename__ = "matches"
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    time = db.Column(db.Time, nullable=False)
    division_id = db.Column(db.Integer, db.ForeignKey('divisions.id'), nullable=False)
    field = db.Column(db.Integer, nullable=False)
    home = db.Column(db.String(20), db.ForeignKey('teams.id'), nullable=False)
    away = db.Column(db.String(20), db.ForeignKey('teams.id'), nullable=False)
    home_score = db.Column(db.Integer)
    home_diff = db.Column(db.Integer)
    away_score = db.Column(db.Integer)
    away_diff = db.Column(db.Integer)
    updated = db.Column(db.DateTime)


class Printable(db.Model):
    __tablename__ = "printables"
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(80), nullable=False)
    url = db.Column(db.String(80), nullable=False)

    division = db.relationship('Division', backref='printable')

    def updated(self):
        return self.division[0].updated


class Team(db.Model):
    __tablename__ = "teams"
    id = db.Column(db.String(4), primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    division = db.Column(db.Integer, db.ForeignKey('divisions.id'), nullable=False)

    points = db.Column(db.Integer)
    goals = db.Column(db.Integer)
    goals_against = db.Column(db.Integer)
    goal_diff = db.Column(db.Integer)
    matches = db.Column(db.Integer)

    home_matches = db.relationship('Match', foreign_keys="Match.home", backref='home_team')
    away_matches = db.relationship('Match', foreign_keys="Match.away", backref='away_team')

    home_finals = db.relationship('Final', foreign_keys="Final.home_actual", backref='home_team')
    away_finals = db.relationship('Final', foreign_keys="Final.away_actual", backref='away_team')

    def __str__(self):
        return "{name} ({id})".format(name=self.name, id=self.id)

    @property
    def finals(self):
        return self.home_finals + self.away_finals

    @property
    def group(self):
        return self.id[2]

    @property
    def matches(self):
        return self.home_matches + self.away_matches

