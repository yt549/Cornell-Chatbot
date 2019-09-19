import json
import logging
from datetime import datetime
from decimal import Decimal

logger = logging.getLogger()
logger.setLevel(logging.INFO)
logging.getLogger('boto').propagate = False
logging.getLogger('boto3').propagate = False
logging.getLogger('botocore').propagate = False

def get_logger():
    return logger

def json_handler(o):
    if isinstance(o, datetime):
        return o.isoformat()
    elif isinstance(o, Decimal):
        return float(o)
    else:
        logger.warning('Unknown Type in json_handler: ' + str(o))
        return str(o)
    