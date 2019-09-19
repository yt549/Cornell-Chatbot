from __future__ import print_function  # Python 2/3 compatibility
import boto3
from boto3.session import Session


def createDBTable(event, context):
    aws = Session()
    ddb = aws.resource('dynamodb')
    hallsLocations_table = ddb.create_table(
        TableName='CornellLocations111',
        KeySchema=[
            {
                'AttributeName': 'HallName',
                'KeyType': 'String'  # Partition key
            },
            {
                'AttributeName': 'Location',
                'KeyType': 'String'  # Sort key
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'HallName',
                'AttributeType': 'S'
            },
            {
                'AttributeName': 'Location',
                'AttributeType': 'S'
            },
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 10,
            'WriteCapacityUnits': 10
        }
    )

    print("Table status:", hallsLocations_table.table_status)

    return hallsLocations_table
