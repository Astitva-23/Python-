n = int(input("Enter the term "))
c = 2
f = 0
s = 1
print(f)
print(s)
while(c<n):
    t = f+s
    f = s
    s = t
    print(t)
    c = c+1