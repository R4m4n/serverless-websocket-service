from boto3.dynamodb.conditions import Key
import json
import boto3
import os

dynamodb = boto3.client('dynamodb')
# dynamodb = boto3.resource('dynamodb')

def handle(event, context):
    # table = dynamodb.Table('websocket-connections')
    print ('event =>>> ', event)

    message = event
    paginator = dynamodb.get_paginator('scan')

    apigatewaymanagementapi = boto3.client('apigatewaymanagementapi', 
    endpoint_url = "https://" + event["requestContext"]["domainName"] + "/" + event["requestContext"]["stage"])
    connectionIds = []
    # Retrieve all connectionIds from the database
    for page in paginator.paginate(TableName="websocket-connections"):
        connectionIds.extend(page['Items'])

    # connectionIds = [c['connectionId'] for c in connectionIds['Responses']['websocket-connections']]
    message = json.dumps(message)
    # Emit the recieved message to all the connected devices
    for connectionId in connectionIds:
        # try:
        print (connectionId)
        apigatewaymanagementapi.post_to_connection(
            Data=message,
            ConnectionId=connectionId['connectionId']['S']
        )
        # except:
        #     continue

    return {}