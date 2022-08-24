import os, sys
try:
    __import__("test").Main()
except Exception as e:
    exit(str(e))