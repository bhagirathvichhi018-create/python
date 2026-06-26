a = int(input("Enter 1st Number :"))
b = int(input("Enter 2nd Number :"))
c = int(input("Enter 3rd Number :"))

if a==b and b==c :
    print("All Same")
elif a > b :
    print(" A is Largest")
elif b > c :
    print("B is Largest")
else :
    print("C is Largest")
