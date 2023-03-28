import requests
import json

def run(job_input):
    response = requests.get("https://lichess.org/api/player/top/200/blitz")
    response.raise_for_status()
    players = response.json()['users']
    id = 0
    for player in players:
        job_input.send_object_for_ingestion(payload = { 'user_id': id, 'username': player['username'] }, destination_table='players')
        id += 1