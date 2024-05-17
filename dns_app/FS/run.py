from flask import Flask
from socket import *
import logging

app = Flask (__name__)
logging.getLogger().setLevel(logging.DEBUG)


def fibnacci(n):
    if n < 0:
        logging.info("Input should be a non-negative integer.")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibnacci( b-1 ) + fibnacci( b-2 )