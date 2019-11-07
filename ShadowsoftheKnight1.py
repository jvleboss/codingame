import sys
from math import *

def createList(size):
    newList = []
    i = 0
    while i < size:
        newList.append(i) 
        i += 1
    return newList

    ## Improve
    #createList2 = lambda size : list(range(size))

f = lambda listL : floor((listL[0]+listL[len(listL)-1])/2)

w, h = [int(i) for i in input().split()]
n = int(input())  # maximum number of turns before game over.
x0, y0 = [int(i) for i in input().split()]
W = createList(w)
H = createList(h)
x = x0
y = y0
while True:
    bomb_dir = input()  # the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)
    directions = list(bomb_dir)
    for direction in directions:
        if direction == "U":
            H = H[0:H.index(y)]
        if direction == "D":
            end = len(H)
            H = H[H.index(y+1):end]
        if direction == "L":
            W = W[0:W.index(x)]
        if direction == "R":
            end = len(W)
            W = W[W.index(x+1):end]
    x = f(W)
    y = f(H)
    print(x,y)