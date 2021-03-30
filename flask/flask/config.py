import os

class Config(object):
    GREETING = "Hello, SLATTIES!"
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'default-key-for-devs'