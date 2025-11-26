field=[9,6,15,47,14,8,3,1]
swapped = True
while True:
    for i in range(len(field)-1):
        if field[i]>field[i+1]:
            tmp = field[i]
            field[i] = field[i+1]
            field[i+1] = tmp
            swapped = True
            print(field)
    if swapped==False:
        break