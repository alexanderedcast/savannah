import json
import requests

from ui_automation.helper.API_helper.api_data import url_api_v2, nik_token


def follow_user(token, user_id, option):
    """

    :param token: you token
    :param user_id:
    :param option: follow or unfollow
    :return:
    """
    headers = token
    response = requests.request("POST", url_api_v2 + "users/{}/{}".format(user_id, option), headers=headers)
    return response.text


def followers(limit):
    querystring = {"limit": "{}".format(limit)}
    headers = nik_token
    response = requests.request("GET", url_api_v2 + "users/followers", headers=headers, params=querystring)
    json_response = response.text
    s = json.loads(json_response, cls=None,
                   object_hook=None,
                   parse_float=None,
                   parse_int=None,
                   parse_constant=None,
                   object_pairs_hook=None)
    return s["total"]


def following(limit):
    querystring = {"limit": "{}".format(limit)}
    headers = nik_token
    response = requests.request("GET", url_api_v2 + "users/following", headers=headers, params=querystring)
    json_response = response.text
    users = json.loads(json_response, cls=None,
                       object_hook=None,
                       parse_float=None,
                       parse_int=None,
                       parse_constant=None,
                       object_pairs_hook=None)
    user_following = []
    for i in range(0, len(users['users'])):
        user_following.append(users['users'][i]['name'])
    return user_following








