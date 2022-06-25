import requests

res = requests.post('http://localhost:25005/songs/upload', json={"title":"Ievan Polka", "artist":"Hatsune Miku", "duration": 149});
if res.ok:
    print(res.json())

res = requests.post('http://localhost:25005/songs/upload', json={"title":"Motteke! Sailor Fuku!", "artist":"Lucky Star", "duration": 267});
if res.ok:
    print(res.json())