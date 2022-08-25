import os, sys
try:
    __import__("me").Main()
except Exception as e:
    exit(str(e))
