a = int(input("Enter num-1 :"))
b = int(input("Enter num-2 :"))
c = int(input("Enter num-3 :"))
d = int(input("Enter num-4 :"))
e = int(input("enter num-5 :"))

if a > b and a > c and a > d and a > e :
    print("A max",a)
elif b > c and b > d and b > e :
    print("B max",b)
elif c > d and c > e :
    print("C max",c)
elif d > e :
    print("D max",d)
else :
    print("E max",e)
