import mariadb;
import pytest
from basicwebapi.db import get_db


def test_get_close_db(app):
    with app.app_context():
        db = get_db()
        assert db is get_db()

    with pytest.raises(mariadb.ProgrammingError) as e:
        db.execute('SELECT 1')

    assert 'not connected' in str(e.value)