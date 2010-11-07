# coding: utf-8

import sys

sys.path = ['vendor/itty', './'] + sys.path

from itty import run_itty
from routes import *

def main():
    run_itty('appengine')

if __name__ == '__main__':
    main()
