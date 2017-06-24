import os, sys ,csv

path = "/home"

outwriter = csv.writer(open("numFiles.csv", 'w')

dirc = []

for root, dirs, files in os.walk(path):
    for d in dirs:
        a = str(d)
        count = 0
        for fi in files:
            count += 1
        y = (a, count)
        dirc.append(y)

    for i in dir_count:
        outwriter.writerow(i)
