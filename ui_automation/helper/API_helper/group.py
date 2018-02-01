import json
import requests

from ui_automation.helper.API_helper.api_data import url_api_v2


def get_list_group(token):
    headers = token
    response = requests.request("GET", url_api_v2 + "teams", headers=headers)
    json_response = response.text
    s = json.loads(json_response, cls=None,
                   object_hook=None,
                   parse_float=None,
                   parse_int=None,
                   parse_constant=None,
                   object_pairs_hook=None)

    group_id = s['teams'][0]['id']
    return group_id


def delete_group(number, token):
    headers = token
    response = requests.request("DELETE", url_api_v2 + "teams/%d" % (number), headers=headers)
    return response.text


def delete_first_group(token):
    num = get_list_group(token)
    delete_group(num, token)











