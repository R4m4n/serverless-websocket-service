# Serverless websocket service

This repository contains the complete code ready to deploy to create a websocket service using Lambda, API Gateway & DynamoDB.

To run this code first install all the dependencies using:

```
pip install -r requirements.txt
npm install
```

`serverless.yml` file contains the function delarations and DynamoDB table definitions. All the requirements are already handled in this file.

To deploy this service, first configure `aws` credentials using `aws-cli`.

You'll need to run `aws configure` to configure the keys and region.

Then to deploy this and create all the required resources just run:

`sls deploy`

And a URL containing `wss://` will be provided in the output which will be the websocket URL.

To send the message over websocket URL, you'll need to add `action` key. 

Example requesst payload for the websocket message is:

```
{
    "action": "onMessage",
    "name": "Raman"
}
```