import sys
import math

def ref(x,y):
    if x[0] == "$":
        return int(y[int(x[1:])][3])
    else:
        return int(x)


def compute(a,b,c):
    if a == "VALUE":
        return b
    if a == "ADD":
        return int(b) + int(c)
    if a == "SUB":
        return int(b) - int(c)
    if a == "MULT":
        return int(b) * int(c)
        

n = int(input())
a = [None]*n

for i in range(n):
    ope, arg1 , arg2 = input().split()
    print(ope,arg1,arg2,file=sys.stderr)
    if arg1[0] == "$" or arg2[0] == "$":
        a[i] = [ope, arg1 , arg2, (arg1,arg2)]
    else:
        a[i] = [ope, arg1 , arg2, compute(ope, arg1 , arg2)]
    print(a[i],file=sys.stderr)
    print(type(a[i][3]),file=sys.stderr)

print(a,file=sys.stderr)

for j in range(n):
    if type(a[j][3]) is not tuple:
        print(a[j][3])
    else:
        x, y = a[j][3]
        a[j][3] = compute(a[j][0],ref(x,a),ref(y,a))
        #print(ref(y,a),file=sys.stderr)
        print(a[j][3])
