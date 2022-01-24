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
            is_removed = False
            for unicorn in event['unicorns']:
                if unicorn in cart['Item']['unicorns']:
                    cart['Item']['unicorns'].remove(unicorn)
                    is_removed = True

            # 更新対象のアイテムが存在すれば更新する
            if is_removed:
                unishop_table.put_item(Item=cart['Item'])
                return "Unicorn was removed and basket was deleted!"
            else:
                return "Didn't find a unicorn to remove"
    except ClientError as e:
        return e.response['Error']['Message']

    return "Are you sure you asked to remove a Unicorn?"
