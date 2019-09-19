import json
import logging
from . import get_logger, json_handler

DEFAULT_CACHE_CONTROL = 'no-cache, no-store, must-revalidate'

logger = get_logger()

def http_response(status_code, body, content_type='application/json', cache_control=DEFAULT_CACHE_CONTROL):
    resp = {
        'statusCode': status_code,
        'headers': {
            'Cache-Control': cache_control,
            'Content-Type': content_type,
        },
        'body': body + '\n',
    }

    return resp
    
def client_error(e):
    errors = json.dumps(e.errors, default=json_handler)
    logger.warning('Client Error ' + errors)
    return http_response(e.http_status, json.dumps({ 'errors': errors }, default=json_handler))

def server_error(e):
    errors = json.dumps(e.errors, default=json_handler)
    logger.error('Server Error ' + errors)
    logging.exception('Server Error Traceback:')
    return http_response(e.http_status, json.dumps({ 'errors': errors }, default=json_handler))

def critical_error(e):
    logging.exception('Critical Error:')
    logger.critical(e)
    return http_response('500', json.dumps({ 'errors': ['SERVER_ERROR'] }, default=json_handler))
