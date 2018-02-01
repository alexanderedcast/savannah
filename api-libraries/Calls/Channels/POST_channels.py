# create channel

import requests
import json

def create_channel(url, token, expected_code):

    header = {
        "X-API-TOKEN": token,
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    payload = json.dumps({
        "channel":{
            "label": "created for test",
            "description": "testing",
            "provider": "",
            "provider_image": "",
            "auto_follow": False,
            "is_private": False
        }
    })

    result = requests.post(url + "/api/v2/channels", data=payload, headers=header)
    status_code = result.status_code
    type = result.headers["Content-Type"][:16]

    # Status Code
    try:
        assert status_code == expected_code
    except AssertionError as e:
        print "Wrong status code:[" + str(status_code) + "] Expected code is:[" + str(expected_code) + "]"
        exit()

    # Accepted type
    try:
        assert type == "application/json"
    except AssertionError as e:
        print "Wrong response type:[" + type + "] Expected:[application/json]"
        exit()

    return result.content

admin_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJob3N0X25hbWUiOm51bGwsInVzZXJfaWQiOjY5OSwiY2xpZW50X3VzZXJfaWQiOm51" \
              "bGwsImlzX29yZ19hZG1pbiI6dHJ1ZSwiaXNfc3VwZXJhZG1pbiI6ZmFsc2UsIm9yZ2FuaXphdGlvbl9pZCI6MzEsInRpbWVzdGFtcCI6I" \
              "jIwMTctMTEtMTBUMjM6NTY6MjEuMzg3KzAwOjAwIiwiaXNfd2ViIjpudWxsfQ.8224xMBOGAAcGGyUp66eisXMJJ-Dc6JNfQZ78APH7C0"
response = create_channel("https://alex.edcasting.co", admin_token, 200)
