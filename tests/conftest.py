"""Provides some core test fixtures used by all tests"""
import pytest
from basicwebapi import create_app

@pytest.fixture
def app():
    app = create_app({
        'TESTING': True,
    })
    yield app


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def runner(app):
    return app.test_cli_runner()