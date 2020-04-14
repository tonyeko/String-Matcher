import os

UPLOAD_FOLDER = "../test"

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret_key'
    UPLOAD_FOLDER = UPLOAD_FOLDER
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024 #16MB