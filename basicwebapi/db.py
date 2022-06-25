import mariadb;
import time;

from flask import current_app, g


def init_app(app):
    app.teardown_appcontext(close_db)

def get_db():
    if 'db' not in g:
        attempts = 0;
        # TO-DO:
        # figure out how to handle this race condition better
        # on first run, the mariadb container performs initialization that takes a few seconds
        # but this initialization is done separately from the container startup, so docker continues to basicwebapi container right away
        # but basicwebapi can't connect until that first-time initialization is done
        while (attempts < 12):
            try:
                attempts = attempts + 1;
                print("attempting db connection to '{}'".format(current_app.config['MARIADB_HOST']));
                conn = mariadb.connect(
                    host = current_app.config['MARIADB_HOST'],
                    port=current_app.config['MARIADB_PORT'],
                    user=current_app.config['MARIADB_USER'],
                    password=current_app.config['MARIADB_PASS'],
                    database=current_app.config['MARIADB_DATABASE']
                );
                if (conn is not None):
                    g.db = conn.cursor();
                    break;
            except mariadb.Error as e:
                print("Could not connect to database. Check connectivity and then check config values.");
                time.sleep(5);

    return g.db


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.connection.close();
        db.close();