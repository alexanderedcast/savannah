import json

import requests

from ui_automation.helper.API_helper.api_data import url_api_v2


def quantity_users_in_org(token, limit, option="users"):
    querystring = {"limit": "{}".format(limit)}
    headers = token
    response = requests.request("GET", url_api_v2 + option, headers=headers, params=querystring)
    json_response = response.text
    users = json.loads(json_response, cls=None,
                       object_hook=None,
                       parse_float=None,
                       parse_int=None,
                       parse_constant=None,
                       object_pairs_hook=None)
    all_users = []
    for i in range(0, len(users['users'])):
        all_users.append(users['users'][i]['name'])
    return all_users


def recommended_users(token, limit):
    headers = token
    response = requests.request("GET", url_api_v2 + "users/recommended_users.json?limit={}".format(limit),
                                headers=headers)
    json_response = response.text
    users = json.loads(json_response, cls=None,
                       object_hook=None,
                       parse_float=None,
                       parse_int=None,
                       parse_constant=None,
                       object_pairs_hook=None)
    recommended_users = []
    for i in range(0, len(users['users'])):
        recommended_users.append(users['users'][i]['name'])
    return recommended_users


def admin_in_org(token, limit):
    querystring = {"limit": "{}".format(limit)}
    headers = token
    response = requests.request("GET", url_api_v2 + "users", headers=headers, params=querystring)
    json_response = response.text
    roles = json.loads(json_response)

    list_admin = []
    for i in range(0, len(roles['users'])):
        for z in range(0, len(roles['users'][i]['roles'])):
            list_admin.append(roles['users'][i]['roles'][z])
    return list_admin.count('admin')


def leaderboard_user(token):
    querystring = {"limit": "10", "offset": "0", "period": "all_time", "order_attr": "smartbites_score"}
    headers = token
    response = requests.request("GET", url_api_v2 + "organizations/leaderboard", headers=headers, params=querystring)
    json_response = response.text
    users = json.loads(json_response, cls=None,
                       object_hook=None,
                       parse_float=None,
                       parse_int=None,
                       parse_constant=None,
                       object_pairs_hook=None)
    leaderboard_users = []
    for i in range(0, len(users['users'])):
        leaderboard_users.append(users['users'][i]['user']['name'])
    return leaderboard_users


def sme_users(token):
    querystring = {"limit": "10", "role": "sme"}
    headers = token
    response = requests.request("GET", url_api_v2 + "users", headers=headers, params=querystring)
    json_response = response.text
    users = json.loads(json_response, cls=None,
                       object_hook=None,
                       parse_float=None,
                       parse_int=None,
                       parse_constant=None,
                       object_pairs_hook=None)
    all_users = []
    for i in range(0, len(users['users'])):
        all_users.append(users['users'][i]['name'])
    return all_users
