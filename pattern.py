a = 0
for i in range(1,5):
    a = int((i*(i+1))/2)
    for j in range(4-i):
        print(" ",end=" ")
    for k in range(i):
        print(a, end=" ")
        a = a-1   
    print()


