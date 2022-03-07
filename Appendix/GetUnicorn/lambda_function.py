import os
import json
import boto3
from botocore.exceptions import ClientError

endpoint_url = os.getenv('DYNAMODB_ENDPOINT', None)
dynamodb = boto3.resource('dynamodb', endpoint_url=endpoint_url)
unishop_table = dynamodb.Table('unishop_unicorn')


def lambda_handler(event, context):
    print("Received event: " + json.dumps(event, indent=2))
    try:
        cart = unishop_table.scan()
        if cart.get('Items'):
            return cart['Items']
        return None
    except ClientError as e:
        return e.response['Error']['Message']
