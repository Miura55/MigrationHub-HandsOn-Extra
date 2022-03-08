import os
import sys
import uuid
import json
import boto3
from botocore.exceptions import ClientError

endpoint_url = os.getenv('DYNAMODB_ENDPOINT', None)
dynamodb = boto3.resource('dynamodb', endpoint_url=endpoint_url)
user_table = dynamodb.Table('unishop_user')


def lambda_handler(event, context):
    print("Received event: " + json.dumps(event, indent=2))

    try:
        email = event['email']
        _id = uuid.uuid4()
        user_table.put_item(
            Item={
                'email': email,
                'uuid': str(_id)
            }
        )
        return {
            'uuid': str(_id),
            'email': email
        }
    except ClientError as e:
        sys.stderr.write(e.response['Error']['Message'])
