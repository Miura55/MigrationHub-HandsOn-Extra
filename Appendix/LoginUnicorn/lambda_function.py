import os
import sys
import json
import boto3
from botocore.exceptions import ClientError

endpoint_url = os.getenv('DYNAMODB_ENDPOINT', None)
dynamodb = boto3.resource('dynamodb', endpoint_url=endpoint_url)
user_table = dynamodb.Table('unishop_user')


def lambda_handler(event, context):
    print("Received event: " + json.dumps(event, indent=2))
    try:
        user = user_table.get_item(Key={'email': event['email']})
        if user.get('Item'):
            return user['Item']
        sys.stderr.write("User not found")
        return None
    except ClientError as e:
        sys.stderr.write(e.response['Error']['Message'])
        return e.response['Error']['Message']
