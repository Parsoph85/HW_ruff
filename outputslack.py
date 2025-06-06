import requests
import json


def send_slack_message(payload, webhook):
    return requests.post(webhook, json.dumps(payload))
