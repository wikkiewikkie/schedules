import datetime
import json
import pytest

from schedules import app, db


@pytest.fixture
def client():
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///test.db"
    with app.app_context():
        db.create_all()
    return app.test_client()


def test_api_divisions(client):
    pass


def test_api_teams(client):
    pass


def test_api_tournament(client):
    result = client.post("/api/tournaments", data=dict(name="Test",
                                                       start_date=datetime.date(2016, 1,1),
                                                       end_date=datetime.date(2016, 1, 2)))
    assert result.status == '200 OK'
    result = client.get("/api/tournaments")
    result = json.loads(result.data.decode())
    assert len(result['tournaments']) == 1


def test_index():
    pass
