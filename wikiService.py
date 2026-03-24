import requests
import sseclient
from constants import WIKI_URL
import json


def load_wifi_event():
    try:
        headers = {'Content-Type': 'text/event-stream; charset=utf-8',
                   'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                                'Chrome/146.0.0.0 Safari/537.36'}
        res = requests.get(WIKI_URL, headers=headers,stream=True)
        client = sseclient.SSEClient(res)
        print('SSE connection opened')
        for event in client.events():
            try:
                data = json.loads(event.data)
                if event.event != "edits from bots":
                    res_data = json.dumps(data)
                    print(f"Tiemstamp :- {data['timestamp']}")
                    print(f"user :- {data['user']}")
                    print(f"title :- {data['title']}")
                    print(f"comment :- {data['comment']}")
                    print(f"wiki :- {data['wiki']}")
            except Exception as e:
                print(f'Failed to parse SSE JSON: {e}')
                break
    except Exception as e:
        print(e)
