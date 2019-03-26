import os
from flask import Flask

class Config(object):
    SECRET_KEY = 'my_secret_key'
    DEBUG = True
'''class DevelopmentConfig(Config):
    #DEBUG = True
    DEBUG = True
'''
