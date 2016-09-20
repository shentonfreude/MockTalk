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

def groups():
    return os.getgroups()


class Filer:
    def __init__(self, name):
        self.name = name
    def rm(self):
        os.remove(self.name)
