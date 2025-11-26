n=11
for i in range(n):
    line=[]
    for j in range(n):
        if i == j or i + j == n - 1:
            line.append("*")
        else:
            line.append(" ")
    print("".join(line))