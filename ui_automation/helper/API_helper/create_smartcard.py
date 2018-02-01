import json
from pprint import pprint

import requests

from helper.API_helper.api_data import url_api_v2, nik_token


def create_text_card(token):
    text_card = "EdCast is the Netflix of Knowledge"
    payload = json.loads(
        {"card":
            {"message": "%s"}}) % text_card
    headers = token
    response = requests.request("POST", url_api_v2 + "cards", data=payload, headers=headers)
    pprint(response.text)
