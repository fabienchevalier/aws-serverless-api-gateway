import json


def lambda_handler(event, context):
    users = [
        {"id": 1, "name": "Jean Dupont"},
        {"id": 2, "name": "Marie Curie"}
    ]
    return {"statusCode": 200, "body": json.dumps(users)}
