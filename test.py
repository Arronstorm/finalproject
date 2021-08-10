import sys
import csv

def subTopper(x,y):
    top = []
    for i in range(1,len(x)):
        temp = 0
        for j in range(len(y)):
            random = int(y[j][i])
            if(random > temp):
                temp = random
                nextval = j
        top.append(nextval)
    for k in range(1,(len(x)-1)):
        p = top[k]
        print("Topper in",x[k],"is",y[p][0])

def topper(p, q):
    overall = []
    toprank = []
    for i in range(len(q)):
        temp = 0
        for j in range(1,len(p)):
            temp = temp + int(q[i][j])
        overall.append(temp)
    for i in range (3):
        x = overall.index(max(overall))
        overall[x] = 0
        toprank.append(x)
    print("\nBest students in the class are: 1st", q[toprank[0]][0],"2nd", q[toprank[1]][0],"3rd", q[toprank[2]][0],"\n")

filename = sys.argv[1]
fields = []
rows = []
with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    fields = next(csvreader)
    for row in csvreader:
        rows.append(row)

subTopper(fields, rows)
topper(fields, rows)


#Student_marks_list.csv
