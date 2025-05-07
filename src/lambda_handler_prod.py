import json


def lambda_handler(event, context):
    users = [{"id": 1, "name": "Prod User One"}, {"id": 2, "name": "Prod User Two"}]
    return {"statusCode": 200, "body": json.dumps(users)}
