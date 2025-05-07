import json


def lambda_handler(event, context):
    users = [{"id": 1, "name": "Dev User One"}, {"id": 2, "name": "Dev User Two"}]
    return {"statusCode": 200, "body": json.dumps(users)}
