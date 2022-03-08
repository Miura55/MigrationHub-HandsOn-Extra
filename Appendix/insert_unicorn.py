import os
import boto3
from dotenv import load_dotenv
load_dotenv()

unicorns = [
    {
        "name": "UnicornFloat",
        "description": "Big Unicorn Float! Giant Glitter Unicorn Pool Floaty",
        "image": "UnicornFloat",
        "uuid": "e0316b68-2d05-46e7-ad64-7fa0aa53a191",
        "price": 100
    },
    {
        "name": "UnicornBeddings",
        "description": "Rainbow Unicorn Bedding Set - The Perfect Kids or Adults Unicorn Duvet Set",
        "image": "UnicornBeddings",
        "uuid": "13c981e5-5436-4780-863c-1d0adbfd1387",
        "price": 100
    },
    {
        "name": "UnicornHipHop",
        "description": "Rainbow Hip Hop Unicorn With Sunglasses Kids Tshirt",
        "image": "UnicornHipHo",
        "uuid": "ad89d5fc-eded-455f-997c-c9f3afcb1f41",
        "price": 100
    },
    {
        "name": "UnicornFluffy",
        "description": "Stylish Fluffy Unicorn Slippers",
        "image": "UnicornFluffy",
        "uuid": "6311207e-f590-4f9a-bec2-67affaf49280",
        "price": 100
    },
    {
        "name": "UnicornGlitter",
        "description": "Unicorn Glitter Backpack - Shop for Unique Unicorn Gifts for Girls!",
        "image": "UnicornGlitter",
        "uuid": "04aced37-0a04-4fbe-8d4d-6caae5e315a6",
        "price": 100
    },
    {
        "name": "UnicornBackpack",
        "description": "Top Rated Classy Unicorn Backpack - Kawaii School Bag",
        "image": "UnicornBackpack",
        "uuid": "be91e589-b705-4f7d-b147-ede42eae7d70",
        "price": 100
    },
    {
        "name": "UnicornPartyDress",
        "description": "Girls Unicorn Party Dress - Tutu Pastel Rainbow Princess Power!",
        "image": "UnicornPartyDress",
        "uuid": "4dda3b2e-fee3-4fec-b360-2cfdc482919b",
        "price": 100
    },
    {
        "name": "UnicornPink",
        "description": "Pretty Pink Baby Unicorn Summer Party Dress",
        "image": "UnicornPink",
        "uuid": "19622d63-65f1-41a9-9daf-5e8ed6c6c41b",
        "price": 100
    },
    {
        "name": "UnicornCool",
        "description": "Cool Dabbing Unicorn Mens Hip-hop Shirts",
        "image": "UnicornCool",
        "uuid": "357a8a27-28f9-495b-b7c6-e83f7f09a61e",
        "price": 100
    },
    {
        "name": "UnicornBlanket",
        "description": "Superfun Bestselling Unicorn Hooded Blanket",
        "image": "UnicornBlanket",
        "uuid": "90d726a2-9457-4857-8811-c38c36beceee",
        "price": 100
    }
]

dynamodb = boto3.resource(
    'dynamodb',
    region_name=os.getenv('REGION_NAME'),
    aws_access_key_id=os.getenv('ACCESS_KEY_ID'),
    aws_secret_access_key=os.getenv('ACCESS_KEY')
)
table = dynamodb.Table('unishop_unicorn')

with table.batch_writer() as batch:
    for unicorn in unicorns:
        batch.put_item(Item=unicorn)

print('Done')
