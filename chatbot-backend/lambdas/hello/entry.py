import json
from codebase import get_logger, json_handler
from codebase.hello import hello
from codebase.responses import client_error, critical_error, http_response, server_error
from codebase.exceptions import ServerlessClientException, ServerlessException

logger = get_logger()

def lambda_handler(event, context):
    logger.info('RequestContext ' + json.dumps(["currentIntent"], default=json_handler))

    try:
        return hello(event, context)

    except ServerlessClientException as e:
        return client_error(e)

    except ServerlessException as e:
        return server_error(e)

    except Exception as e:
        return critical_error(e)



