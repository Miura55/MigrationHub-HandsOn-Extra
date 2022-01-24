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
            is_added = False
            for unicorn in event['unicorns']:
                if unicorn not in cart['Item']['unicorns']:
                    cart['Item']['unicorns'].append(unicorn)
                    is_added = True
            if is_added:
                unishop_table.put_item(Item=cart['Item'])
                return "Added Unicorn to basket!"
            else:
                return "Unicorn is already exists in basket!"
        else:
            if len(event['unicorns']) == 0:
                return "No unicorns to add"
            # uuidでデータがなければ新規作成する
            unishop_table.put_item(Item=event)
            return "Added Unicorn to basket!"
    except ClientError as e:
        return e.response['Error']['Message']
