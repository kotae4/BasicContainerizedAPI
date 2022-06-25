"""Provides some core test fixtures used by all tests"""
import pytest
from basicwebapi import create_app
from basicwebapi.db import get_db

@pytest.fixture
def app():

    # to-do:
    # use separate db for tests
    # for now i'll just make sure all the tests operate on a separate table
    app = create_app({
        'TESTING': True,
        'MARIADB_HOST': 'mariadb',
        'MARIADB_PORT': 3306,
        'MARIADB_DATABASE': 'basicwebapi-test',
        'MARIADB_USER': 'root',
        'MARIADB_PASS': 'toor',
    })
    """
    with app.app_context():
        db = get_db();
        db.execute("INSERT IGNORE INTO songs (title, artist, duration) VALUES ('Motteke! Sailor Fuku!', 'Lucky Star', 267)");
        db.connection.commit();
    """

    yield app


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def runner(app):
    return app.test_cli_runner()