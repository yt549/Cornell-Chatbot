from __future__ import print_function # Python 2/3 compatibility
import boto3
import json
import decimal

# Helper class to convert a DynamoDB item to JSON.
class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            if abs(o) % 1 > 0:
                return float(o)
            else:
                return int(o)
        return super(DecimalEncoder, self).default(o)

dynamodb = boto3.resource('dynamodb', region_name='us-east-1' )
                            # ,aws_access_key_id='AKIAJB4O4YMRGCSBNN2A',
                            # aws_secret_access_key='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')

CornellLocs = dynamodb.Table('CornellLocs')


hall_name = "MPS lab"
city = "Ithaca"
location = "Rhodes 153"

response = CornellLocs.put_item(
   Item={
        'Hall_Name': hall_name,
        'CIty': city
    }
)

print("PutItem succeeded:")
print(json.dumps(response, indent=4, cls=DecimalEncoder))
