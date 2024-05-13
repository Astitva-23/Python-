def hcf(a,b):
    if(b == 0):
        return a
    else:
        return hcf(b, a%b)
    
a = int(input("Enter first no: "))
b = int(input("Enter second no: "))
gcd = hcf (a,b)
lcm = (a*b)/hcf(a,b)
print("HCF: ", gcd)
print("LCM: ", lcm)
