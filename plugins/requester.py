import json
import os

import requests


class KOTException(Exception):
    pass


class KOTRequester():
    KOT_API_BASE_URL = 'https://api.kingtime.jp/v1.0'
    KOT_TOKEN = os.environ.get('KOT_TOKEN')

    def __init__(self):
        self.base_url = self.KOT_API_BASE_URL
        self.headers = {
            'Content-Type': 'application/json; charset=utf-8',
            'Authorization': 'Bearer {token}'.format(token=self.KOT_TOKEN)
        }

    def get(self, uri):
        url = self.base_url + uri
        resp = requests.get(url, headers=self.headers)
        resp_json = json.loads(resp.text)
        if 'errors' in resp_json:
            raise KOTException(resp_json['errors'][0]['message'])
        return resp_json

    def post(self, uri, payload):
        url = self.base_url + uri
        resp = requests.post(url, headers=self.headers, data=payload)
        resp_json = json.loads(resp.text)
        if 'errors' in resp_json:
            raise KOTException(resp_json['errors'][0]['message'])
        return resp_json
