import os
import logging

def rm(name):
    os.remove(name)

def rmtry(name):
    try:
        os.remove(name)
    except FileNotFoundError as e:
        logging.error(e)
        raise RuntimeError(e)


