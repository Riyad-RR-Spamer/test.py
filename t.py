import os, sys
try:
    __import__("aq").Main()
except Exception as e:
    exit(str(e))
