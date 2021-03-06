import sys

if not 'test' in sys.argv or 'test_coverage' in sys.argv:

 LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'standard': {
            'format': '%(levelname)s %(name)s %(asctime)s %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(name)s: %(message)s'
        },
    },
    'handlers': {
        'null': {
            'level':'DEBUG',
            'class':'django.utils.log.NullHandler',
        },
        'file':{
            'level':'WARNING',
            'class':'logging.handlers.TimedRotatingFileHandler',
            'when': 'midnight',
            'filename': '/var/log/what/general.log',
            'formatter': 'standard'
        },
        'comm_file':{
            'level':'INFO',
            'class':'logging.handlers.TimedRotatingFileHandler',
            'when': 'midnight',
            'filename': '/var/log/what/comm.log',
            'formatter': 'standard'
         },
        
        'email_file':{
            'level':'INFO',
            'class':'logging.handlers.TimedRotatingFileHandler',
            'when': 'midnight',
            'filename': '/var/log/what/email.log',
            'formatter': 'standard'
         },
                 
        
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'formatter': 'verbose'
        }
    },
    'loggers': {
        'django': {
            'handlers':['null'],
            'propagate': True,
            'level':'INFO',
        },
        'django.request': {
            'handlers': ['file', 'mail_admins'],
            'level': 'ERROR',
            'propagate': False,
        },
        '': {
            'handlers': ['file', 'mail_admins'],
            'level': 'ERROR',
        },
        'comm': {
            'handlers': ['comm_file'],
            'level': 'INFO',
        },
        'email': {
            'handlers': ['email_file'],
            'level': 'INFO',
        },
    }
}