import os
import sys
from flask import Flask
# Imports libraries

DEBUG = True # Sets whether code is in development stage or not

def log(s):
    """ Prints debug log (s) to screen"""
    if DEBUG:
        print(s)

