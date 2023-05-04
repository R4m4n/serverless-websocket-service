
import json
import boto3
import os

dynamodb = boto3.client('dynamodb')

def handle(event, context):
    connectionId = event['requestContext']['connectionId']

    # Delete connectionId from the database
    dynamodb.delete_item(TableName="websocket-connections", Key={'connectionId': {'S': connectionId}})

    return {}