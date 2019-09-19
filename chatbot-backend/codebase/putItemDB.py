import boto3


def putItemDB(event, context):
    # this will create dynamodb resource object and here dynamodb is resource name
    client = boto3.resource('dynamodb')

    # this will search for dynamoDB table your table name may be different
    table = client.Table("CornellLocations111")

    return table.put_item(Item={'HallName': 'Bill Room ', 'Location': 'college town'})
