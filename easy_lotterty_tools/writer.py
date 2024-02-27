import sys


def refresh():
    sys.stdout.write("\r                         \r")
    sys.stdout.flush()


def output(s):
    sys.stdout.write(s)
    sys.stdout.flush()
