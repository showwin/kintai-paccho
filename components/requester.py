import json
import os

import requests


class KOTException(Exception):
    pass


class KOTRequester:
    KOT_API_BASE_URL = "https://api.kingtime.jp/v1.0"
    KOT_TOKEN = os.environ.get("KOT_TOKEN")
    KOT_HTTPS_PROXY = os.environ.get("KOT_HTTPS_PROXY")

    def __init__(self):
        self.base_url = self.KOT_API_BASE_URL
        self.headers = {
            "Content-Type": "application/json; charset=utf-8",
            "Authorization": "Bearer {token}".format(token=self.KOT_TOKEN),
        }
        self.proxies = {
            "https": self.KOT_HTTPS_PROXY,
        } if self.KOT_HTTPS_PROXY else None

    def get(self, uri):
        url = self.base_url + uri
        resp = requests.get(url, headers=self.headers, proxies=self.proxies)
        resp_json = json.loads(resp.text)
        if "errors" in resp_json:
            raise KOTException(resp_json["errors"][0]["message"])
        return resp_json

    def post(self, uri, payload):
        url = self.base_url + uri
        resp = requests.post(url, headers=self.headers, data=payload, proxies=self.proxies)
        resp_json = json.loads(resp.text)
        if "errors" in resp_json:
            raise KOTException(resp_json["errors"][0]["message"])
        return resp_json

    def put(self, uri, payload):
        url = self.base_url + uri
        resp = requests.put(url, headers=self.headers, json=payload, proxies=self.proxies)
        resp_json = json.loads(resp.text)
        if "errors" in resp_json:
            raise KOTException(resp_json["errors"][0]["message"])
        return resp_json
