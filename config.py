import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or b"\xf8m\xfbc\xf1\xf5\xbc\x95'}\xca%\x1d\xef_\x03"

    MONGODB_SETTINGS = { 'db' : 'NeuroFlow' }


    