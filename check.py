f = open('C:/Users/suman/Microsoft VS Code/vscode/first/word.txt', 'r+')
line = f.readline()
counter_dict = {}

while line:
    line = line.strip()
    if line in counter_dict:
        counter_dict[line] += 1
    else:
        counter_dict[line] = 1
    line = f.readline()

print(counter_dict)

# This is the second way of doing this


import collections
import pprint

file_name = input("File name: ")
with open(file_name, 'r+') as f:
    count = collections.Counter(f.read().upper())
    value = pprint.pformat(count)

print(value)
