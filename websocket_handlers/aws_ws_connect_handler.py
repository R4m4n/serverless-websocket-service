import json
import boto3
import os
# import jwt

dynamodb = boto3.client('dynamodb')

def handle(event, context):
    connectionId = event['requestContext']['connectionId']

    # Insert the connectionId of the connected device to the database
    dynamodb.put_item(TableName="websocket-connections", Item={
        'connectionId': {'S': connectionId}
    })

    return {}