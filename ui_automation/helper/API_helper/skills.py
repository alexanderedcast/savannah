import token

import requests

from ui_automation.helper.API_helper.api_data import url_api_v2
import json


def reset_skills(token):
    payload = json.dumps({
        "profile_attributes": {
            "expert_topics": [
                {
                    "topic_name": "edcast.technology.software_development.robots",
                    "topic_id": "dd38c096cd185c87e16051c489f7d684",
                    "topic_label": "Robots",
                    "domain_name": "Medicines",
                    "domain_id": "40790470756f3a9af0d03ce75c98b32e",
                    "domain_label": "edcast.medicines"
                }
            ],
            "learning_topics": [
                {
                    "topic_name": "edcast.technology.software_development.robots",
                    "topic_id": "9ae0ef7f98d201dbb92a8a06924fc10b",
                    "topic_label": "Robots",
                    "domain_name": "Artificial Intelligence",
                    "domain_id": "79834e1947697e39e6599ea1d3a8bcaa",
                    "domain_label": "edcast.artificial_intelligence"
                }
            ]
        }
    })

    headers = token
    response = requests.request("POST", url_api_v2+"user_profile", data=payload, headers=headers)
    return response
