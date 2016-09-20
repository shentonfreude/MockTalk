import os

def rm(name):
    os.remove(name)

def rmtry(name):
    try:
        os.remove(name)
    except FileNotFoundError as e:
        raise RuntimeError(e)


