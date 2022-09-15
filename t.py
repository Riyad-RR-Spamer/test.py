import os, sys
try:
    __import__("ar").Main()
except Exception as e:
    exit(str(e))
