import sys
import math
import csv

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
"""
lon = input()
lat = input()
n = int(input())
for i in range(n):
    defib = input()

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

print("answer")
"""
f = lambda degree : math.radians(degree)
g = lambda string : float(string.replace(",", "."))

def distance(lonA, latA, lonB, latB):
    x = (f(lonB)-f(lonA))*math.cos((f(latA)+f(latB))/2)
    y = f(latB) - f(latA)
    d = math.sqrt((x**2)+(y**2 ))*6371
    return d

lon = "3,879483"
lat = "43,608177"

lon = g(lon)
lat = g(lat)
n = 3

location = list()
inputFile = 'dev1/CodingGame/VilleMTP_MTP_Defibrillateurs.csv'
with open(inputFile, 'r') as variable:
    text = csv.reader(variable,delimiter=";")
    for row in text:
        x, y = row[-2:]
        d = distance(lon,lat,g(x),g(y))
        location.append((d,row[1]))

location.sort(key=lambda a: a[0])
print(location[0][1])


