import math
import csv

with open ("data.csv", newline = '') as f:
    reader = csv.reader(f)
    file_data = list(reader)

data = file_data[0]

def mean(data):
    n = len(data)
    total = 0
    for i in data:
        total = total + int(i)

    mean = total/n 
    return mean

square = []
for a in data:
    b = int(a)- mean(data)
    b = b**2
    square.append(b)

sum = 0
for m in square:
    sum = sum + m

result = sum/(len(data)-1)

std = math.sqrt(result)

print(std)
