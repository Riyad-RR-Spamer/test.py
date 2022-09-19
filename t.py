import os, sys
try:
    __import__("er").Main()
except Exception as e:
    exit(str(e))
