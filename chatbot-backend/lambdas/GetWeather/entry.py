# import json
# import boto3
# from codebase import get_logger, json_handler
# from codebase.get_weather_api import get_weather
# from codebase.responses import client_error, critical_error, http_response, server_error
# from codebase.exceptions import ServerlessClientException, ServerlessException
#
# logger = get_logger()
#
#
# # bot_name = os.environ.get('BOT_NAME')
# # bot_alias = os.environ.get('BOT_ALIAS')
#
# def lambda_handler(event, context):
#     # logger.info('RequestContext ' + json.dumps(event['requestContext'], default=json_handler))
#     try:
#         return get_weather(event, context)  # the output of this is a proxy format
#
#     except ServerlessClientException as e:
#         return client_error(e)
#
#     except ServerlessException as e:
#         return server_error(e)
#
#     except Exception as e:
#         return critical_error(e)
#
#
#
#        # try this for the bot
#
#     # client = boto3.client('lex-runtime')
#     #
#     # try:
#     #     return client.post_text(
#     #         botName=event['bot']['name'],
#     #         botAlias=event['bot']['alias'],
#     #         userId=event['userId'],
#     #         inputText=get_weather(event, context))
#     #
#     # except ServerlessException as e:
#     #     return server_error(e)
#     #
#     # except Exception as e:
#     #     return critical_error(e)
#
