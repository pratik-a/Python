f = open("datatry.txt", "r")

f1 = open("copy", "w")

for data in f:
    f1.write(data)