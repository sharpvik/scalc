import sys

def log(msg):
    print(f'[LOG] {msg}')

def err(msg):
    print(f'[ERR] {msg}')
    sys.exit(1)

