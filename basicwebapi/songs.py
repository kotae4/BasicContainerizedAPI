from datetime import time
from flask import Flask
from flask import request
from typing import Optional

from basicwebapi.db import get_db

# marking private to prevent pdoc from seeing it
class _SongsResponseObject:
    status = -1;
    body = "Unknown Error";

    def __init__(self, _status = -1, _body = "Unknown Error"):
        self.status = _status;
        self.body = _body;

    def ToObject(self):
        return { "status": self.status, "body": self.body};

# this one is public because we **do** want pdoc to see it
class SongObject:
    """**Schema (JSON):** { "id":integer,<br>
    "title":string,<br>
    "artist":string,<br>
    "duration":integer,<br>
    "uploadDate":optional<timestamp> }<br>
    **Note:**<br>`duration` is expected to be the length of the song in seconds<br>`uploadDate` shouldn't be provided when uploading songs."""
    id : int = 0;
    title : str = "error";
    artist : str = "unknown";
    duration : int = 0;
    uploadDate : Optional[time] = 0;

    def __init__(self, _id, _title, _artist, _duration, _uploadDate):
        self.id = _id;
        self.title = _title;
        self.artist = _artist;
        self.duration = _duration;
        self.uploadDate = _uploadDate;
    
    # marking private to avoid pdoc from seeing it
    def _ToObject(self):
        return { "id": self.id, "title": self.title, "artist": self.artist, "duration": self.duration, 
        "uploadDate": self.uploadDate};

def songs():
    """**/songs**<br>
    **Response Schema (JSON):** { "status":integer, "body":list\\<`SongObject`> | string }<br>
    **Status codes:**<br>
    **400** - indiciates an error. The `body` field is a string containing the detailed error message.<br>
    **200** - indicates a success. The `body` field is a JSON collection of `SongObject` comprising the total collection.<br>
    """
    try:
        db = get_db();
        # TO-DO:
        # limit 100 and paginate
        songs = db.execute(
            'SELECT * FROM songs'
        ).fetchall();
        formattedSongList = [];
        for song in songs:
            # lol i really should read up how to model stuff properly
            # i think both flask and sqlite provide a modeling system
            fmtSong = SongObject(*tuple(song));
            formattedSongList.append(fmtSong._ToObject());
        
        return _SongsResponseObject(200, formattedSongList).ToObject();
    except Exception as e:
        return _SongsResponseObject(400, "Contact server administrator.").ToObject();

def post_song():
    """**/songs/upload**<br>
    **Request Schema (JSON) [POST]:** `SongObject`<br>
    **Response Schema (JSON):** { "status":integer, "body":string }<br>
    **Status codes:**<br>
    **400** - indiciates an error. The `body` field is a string containing the detailed error message.<br>
    **200** - indicates a success. The `body` field is a string containing the word "Success".<br>
    **Code Example:**<br>
    ```py
    import requests
    res = requests.post('http://<api-url>/songs/upload',
        json={"title":"Ievan Polka", "artist":"Hatsune Miku", "duration": 149});
    if res.ok:
        print(res.json())
    ```
    """
    try:
        db = get_db();
        songData = request.get_json();
        if (("title" in songData == False) or ("artist" in songData == False) or ("duration" in songData == False)):
            return _SongsResponseObject(400, "Invalid arguments. Expected 'title', 'artist', and 'duration' key:value pairs.").ToObject();

        db.execute("INSERT INTO songs (title, artist, duration) VALUES (?, ?, ?)", (songData["title"], songData["artist"], songData["duration"]));
        db.commit();
        
        return _SongsResponseObject(200, "Success").ToObject();
    except Exception as e:
        return _SongsResponseObject(400, "Contact server administrator.").ToObject();

post_song.methods = ['POST'];

def delete_song(id):
    """**/songs/{id}/delete**<br>
    **Response Schema (JSON):** { "status":integer, "body":string }<br>
    **Status codes:**<br>
    **400** - indiciates an error. The `body` field is a string containing the detailed error message.<br>
    **200** - indicates a success. The `body` field is a string containing the word "Success".<br>
    **Note:** This will return success even if no record existed. It is your responsibility to ensure the record exists before deleting it.<br>
    """
    try:
        db = get_db();
        db.execute("DELETE FROM songs WHERE id = ?", (id,));
        db.commit();
        
        return _SongsResponseObject(200, "Success").ToObject();
    except Exception as e:
        return _SongsResponseObject(400, "Contact server administrator.").ToObject();

def get_song(id):
    """**/songs/{id}**<br>
    **Response Schema (JSON):** { "status":integer, "body":`SongObject` | string }<br>
    **Status codes:**<br>
    **400** - indiciates an error. The `body` field is a string containing the detailed error message.<br>
    **404** - indicates that no song with that ID was found. The `body` field is a string containing the error message.<br>
    **200** - indicates a success. The `body` field is a SongObject.<br>
    """
    try:
        db = get_db();
        song = db.execute("SELECT * FROM songs WHERE id = ?", (id,)).fetchone();
        if (song is None):
            return _SongsResponseObject(404, "Song not found.").ToObject();

        fmtSong = SongObject(*tuple(song));
        return _SongsResponseObject(200, fmtSong._ToObject()).ToObject();
    except Exception as e:
        return _SongsResponseObject(400, "Contact server administrator.").ToObject();