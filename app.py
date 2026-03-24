from wikiService import load_wifi_event
from flask import Flask

app = Flask(__name__)


def execute():
    print("Calling execute")
    load_wifi_event()



execute()

