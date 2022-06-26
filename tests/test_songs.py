import pytest
from flask import g, session
from basicwebapi.db import get_db

def test_songs(client, app):
    # set up test data
    with app.app_context():
        db = get_db();
        db.execute(
            "INSERT IGNORE INTO songs (title, artist, duration) VALUES (?, ?, ?)",
            ("Motteke! Sailor Fuku!", "Lucky Star", 267,)
        );
        db.connection.commit();

    # now test it
    response = client.get('/songs');
    assert response.status_code == 200;
    respJSON = response.get_json();
    assert respJSON is not None;
    # TO-DO:
    # look up what happens when you index this kind of object
    # in C++ it might auto-create a new key:value pair for you
    # in python it might throw an exception in which case this test case will error out
    songs = respJSON['body'];
    assert songs is not None;
    found = False;
    for song in songs:
        if (song['title'] == 'Motteke! Sailor Fuku!'):
            found = True;
            break;
    assert found == True;

def test_post_song(client, app):
    # delete it if it already exists
    with app.app_context():
        db = get_db();
        db.execute(
            "DELETE IGNORE FROM songs WHERE title = ?",
            ("SLoWMoTIoN",)
        );
        db.connection.commit();

    # now test the upload
    assert client.get('/songs/upload').status_code == 405
    response = client.post(
        '/songs/upload', json={"title":"SLoWMoTIoN", "artist":"Hatsune Miku", "duration": 310}
    );
    assert response.status_code == 200;
    respJSON = response.get_json();
    assert respJSON is not None;
    assert respJSON['status'] == 200;

    with app.app_context():
        get_db().execute(
            "SELECT * FROM songs WHERE title = 'SLoWMoTIoN'",
        )
        assert get_db().fetchone() is not None

def test_get_song(client, app):
    # set up test data
    testID = -1;
    with app.app_context():
        db = get_db();
        db.execute(
            "INSERT IGNORE INTO songs (title, artist, duration) VALUES (?, ?, ?)",
            ("吹っ切れた", "Kasane Teto", 36000,)
        );
        db.connection.commit();
        db.execute(
            "SELECT * FROM songs WHERE title = '吹っ切れた'",
        );
        testID = db.fetchone()[0];

    # now test it
    assert testID != -1;
    response = client.get('/songs/{}'.format(testID));
    assert response.status_code == 200;
    respJSON = response.get_json();
    assert respJSON is not None;
    assert respJSON['status'] == 200;

    # now delete it
    with app.app_context():
        db = get_db();
        db.execute(
            "DELETE FROM songs WHERE id = ?",
            (testID,)
        );
        db.connection.commit();
    
    # and test that it'll return a 404 this time
    response = client.get('/songs/{}'.format(testID));
    assert response.status_code == 200;
    respJSON = response.get_json();
    assert respJSON is not None;
    assert respJSON['status'] == 404;

def test_delete_song(client, app):
    # prepare the data (insert a record and get its ID)
    testID = -1;
    with app.app_context():
        db = get_db();
        db.execute(
            "INSERT IGNORE INTO songs (title, artist, duration) VALUES (?, ?, ?)",
            ("Sai & Co", "KPP", 230,)
        );
        # it doesn't really matter if another insertion occurred in between these two commands, it's a test db afterall
        db.execute(
            "SELECT * FROM songs ORDER BY id DESC LIMIT 1",
        );
        lastRecord = db.fetchone();
        assert lastRecord is not None;
        testID = lastRecord[0];
        assert testID is not None;

    # now do the testing
    assert testID != -1;
    response = client.get('/songs/{}/delete'.format(testID));
    assert response.status_code == 200;
    respJSON = response.get_json();
    assert respJSON is not None;
    assert respJSON['status'] == 200;

    response = client.get('/songs/{}'.format(testID));
    assert response.status_code == 200;
    respJSON = response.get_json();
    assert respJSON is not None;
    assert respJSON['status'] == 404;

    # test that non-existent records still return 200
    response = client.get('/songs/{}/delete'.format(testID + 4814713));
    assert response.status_code == 200;
    respJSON = response.get_json();
    assert respJSON is not None;
    assert respJSON['status'] == 200;