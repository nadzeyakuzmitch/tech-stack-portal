import logging
from logging.config import dictConfig

import flask
from app.logging_config.log_formatters import RequestFormatter
from flask import current_app, request

log_con = flask.Blueprint('log_con', __name__)


@log_con.before_app_first_request
def configure_logging():
    logging.config.dictConfig(LOGGING_CONFIG)

    current_app.logger.info("Initial request handler executed")

    appInfoLogger = logging.getLogger("appInfo")
    appInfoLogger.info("Initial request handler executed")


@log_con.before_app_request
def before_request_logging():
    current_app.logger.info("Before request handler executed")

    appInfoLogger = logging.getLogger("appInfo")
    appInfoLogger.info("Before request handler executed")


@log_con.after_app_request
def after_request_logging(response):
    if request.path == '/favicon.ico':
        return response
    elif request.path.startswith('/static'):
        return response
    elif request.path.startswith('/bootstrap'):
        return response

    current_app.logger.info("After request handler executed")

    appRequestLogger = logging.getLogger("appRequests")
    appRequestLogger.info("After request handler executed")

    return response


LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
        },
        'RequestFormatter': {
            '()': 'app.logging_config.log_formatters.RequestFormatter',
            'format': '[%(asctime)s] [%(process)d] %(remote_addr)s requested %(url)s'
            '%(levelname)s in %(module)s: %(message)s'
        }
    },
    'handlers': {
        'default': {
            'level': 'DEBUG',
            'formatter': 'standard',
            'class': 'logging.StreamHandler',
            'stream': 'ext://sys.stdout',
        },
        'file.handler.rootLogger': {
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'standard',
            'filename': 'app/logs/rootLogger.log',
            'maxBytes': 10000000,
            'backupCount': 5,
        },
        'file.handler.appInfo': {
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'standard',
            'filename': 'app/logs/appInfo.log',
            'maxBytes': 10000000,
            'backupCount': 5,
        },
        'file.handler.appRequests': {
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'RequestFormatter',
            'filename': 'app/logs/appRequests.log',
            'maxBytes': 10000000,
            'backupCount': 5,
        },
        'file.handler.appErrors': {
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'standard',
            'filename': 'app/logs/appErrors.log',
            'maxBytes': 10000000,
            'backupCount': 5,
        }
    },
    'loggers': {
        '': {
            'handlers': ['default', 'file.handler.rootLogger'],
            'level': 'DEBUG',
            'propagate': True
        },
        'appInfo': {
            'handlers': ['file.handler.appInfo'],
            'level': 'INFO',
            'propagate': False
        },
        'appErrors': {
            'handlers': ['file.handler.appErrors'],
            'level': 'INFO',
            'propagate': False
        },
        'appRequests': {
            'handlers': ['file.handler.appRequests'],
            'level': 'INFO',
            'propagate': False
        }
    }
}
