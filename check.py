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