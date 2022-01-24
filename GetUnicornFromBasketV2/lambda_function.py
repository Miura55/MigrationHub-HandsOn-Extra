import os
import json
import boto3
from botocore.exceptions import ClientError

endpoint_url = os.getenv('DYNAMODB_ENDPOINT', None)
dynamodb = boto3.resource('dynamodb', endpoint_url=endpoint_url)
unishop_table = dynamodb.Table('unishop')


def lambda_handler(event, context):
    print("Received event: " + json.dumps(event, indent=2))
    try:
        cart = unishop_table.get_item(Key={'uuid': event['uuid']})
        if cart.get('Item'):
            return cart['Item']
        return None
    except ClientError as e:
        return e.response['Error']['Message']
