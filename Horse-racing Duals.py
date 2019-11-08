import sys
import math

n = 3

inputList = [5, 8, 9]

horseList = inputList
deltaList = list()

print(horseList,file=sys.stderr)

for i,horse in enumerate(sorted(horseList)):
    if i == 0:
        horseP = horse    
    if i > 0:
        delta = horse - horseP
        deltaList.append(delta)
        horseP = horse

print(deltaList)
print(sorted(deltaList)[0])
