
from boto3.session import Session
from codebase import json_handler
from codebase.responses import http_response
import json


# ====== Get weather
# import boto3
#
# import logging
# import urllib
# import weather

# ======

aws = Session()


# lex = aws.client('lex-runtime')

def hello_world(event, context):
    hello_world_data = dict(
        ApiResponse='Hello World!',
    )

    hello_world_body = json.dumps(hello_world_data, default=json_handler)

    return http_response(status_code='200', body=hello_world_body)


def random_id(event, context):
    random_id_dict = dict(
        RandomId='AjI32b12',
    )

    random_id_json = json.dumps(random_id_dict, default=json_handler)

    return http_response(status_code='200', body=random_id_json)


# def process_user_audio(event, context):
# use http python3 libs to parse POST request

# audio = event['Audio']

# lex.post_content(
#     botName='my-bot',
#     botAlias='my-bot-alias',
#     userId='my-user-id',
#     contentType='audio/mp3',
#     inputStream=b'bytes',
# )

