"""A basic WebAPI for experimenting with docker containers"""
import os

from flask import Flask

def create_app(test_config=None):
    """Factory function for creating the Flask application.<br>
    `test_config` arg is currently only used for unit tests. Leave default for normal usage."""
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY="ajoke",
        DATABASE=os.path.join(app.instance_path, "basicwebapi.sqlite"),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile("config.py", silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from . import db
    db.init_app(app);

    from . import math
    app.add_url_rule('/math', view_func=math.math);

    from . import songs
    app.add_url_rule('/songs', view_func=songs.songs);
    app.add_url_rule('/songs/upload', view_func=songs.post_song);
    app.add_url_rule('/songs/<int:id>/delete', view_func=songs.delete_song);
    app.add_url_rule('/songs/<int:id>', view_func=songs.get_song);

    return app