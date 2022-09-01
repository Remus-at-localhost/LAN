import json
import requests

def retrive():
    headers = {
        'authorization': 'OTA3NTgwMjE2MjcxMDU2ODk3.G2YLqz.php5ypT1nQtaWA8RH4eWLdONGNIjOacce0-yn4'
    }
    r = requests.get(
        f'https://discord.com/api/v9/channels/996713086885044267/messages',headers=headers)
    jobj= json.loads(r.text)
    for value in jobj:
        print(value, '\n')

retrive()
