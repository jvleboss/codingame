import sys
import math

n = int(input())  # Number of elements which make up the association table.
q = int(input())  # Number Q of file names to be analyzed.

filetypes = dict()

for i in range(n):
    ext, mt = input().split()
    filetypes[ext.lower()] = mt

for i in range(q):
    fname = input()  # One file name per line.
    fname = fname[::-1]
    try:
        index = fname.index('.')
    except ValueError:
        index = None
    if index:
        fname = fname[:index][::-1]
        val = filetypes.setdefault(fname.lower(), "UNKNOWN")
    else:
        val = "UNKNOWN"
    print(val)