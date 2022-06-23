import requests

res = requests.post('http://localhost:25005/songs/upload', json={"title":"Motteke! Sailor Fuku!", "artist":"Lucky Star", "duration": 267});
if res.ok:
    print(res.json())