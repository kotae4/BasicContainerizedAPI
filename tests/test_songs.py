import pytest
from flask import g, session
from basicwebapi.db import get_db

def test_songs(client, app):
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
        assert get_db().execute(
            "SELECT * FROM songs WHERE title = 'Ievan Polka'",
        ).fetchone() is not None

def test_delete_song(client, app):
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

@pytest.mark.parametrize(('path', 'statusCode'), (
    ('/songs/1', 200),
    ('/songs/935249', 404),
))
def test_get_song(client, app, path, statusCode):
    response = client.get(path);
    assert response.status_code == 200;
    respJSON = response.get_json();
    assert respJSON is not None;
    assert respJSON['status'] == statusCode;
