import pytest
from flask import g, session
from basicwebapi.db import get_db

def test_songs(client):
    response = client.get('/songs');
    assert response.status_code == 200;
    respJSON = response.get_json();
    assert respJSON is not None;
    assert respJSON['body'][0]['title'] == 'Motteke! Sailor Fuku!';

def test_post_song(client, app):
    assert client.get('/songs/upload').status_code == 405
    response = client.post(
        '/songs/upload', json={"title":"Ievan Polka", "artist":"Hatsune Miku", "duration": 149}
    );
    assert response.status_code == 200;
    respJSON = response.get_json();
    assert respJSON is not None;
    assert respJSON['status'] == 200;

    with app.app_context():
        get_db().execute(
            "SELECT * FROM songs WHERE title = 'Ievan Polka'",
        )
        assert get_db().fetchone() is not None

@pytest.mark.parametrize(('path', 'statusCode'), (
    ('/songs/1', 200),
    ('/songs/935249', 404),
))
def test_get_song(client, path, statusCode):
    response = client.get(path);
    assert response.status_code == 200;
    respJSON = response.get_json();
    assert respJSON is not None;
    assert respJSON['status'] == statusCode;

def test_delete_song(client):
    response = client.get('/songs/1/delete');
    assert response.status_code == 200;
    respJSON = response.get_json();
    assert respJSON is not None;
    assert respJSON['status'] == 200;

    response = client.get('/songs/1');
    assert response.status_code == 200;
    respJSON = response.get_json();
    assert respJSON is not None;
    assert respJSON['status'] == 404;

    response = client.get('/songs/8115474/delete');
    assert response.status_code == 200;
    respJSON = response.get_json();
    assert respJSON is not None;
    assert respJSON['status'] == 200;