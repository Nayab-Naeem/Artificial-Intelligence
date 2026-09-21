m = int (input ("Rows m :"))
n = int (input ("Columns n :"))
arr = []
for i in range(m):
    row = []
    for j in range(n):
        row.append(i*j)
    arr.append(row)

print (arr)     