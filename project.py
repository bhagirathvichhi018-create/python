print("=====================================================")
print("                PERSONAL INFORMATION                  ")
print("=====================================================\n")
name = (input("Enter your Name : "))
age = int(input("Enter your Age : "))
height = float(input("Enter Your Height : "))
fav_num = int(input("Enter Your favorite number : "))

print("\nThenk you! Here is The Information We Collected:")

print("\n=========USER INFORMATION==========\n")

print("Name           :",name)
print("Age            :",age)
print("Height         :",height)
print("Favorit Number :",fav_num)

print("\n====BIRTH YEAR CALCULATION====\n")

current_year = 2026
birth_year = current_year - age
print("Your Birth year :",birth_year)

print("\n======== DATA TYPE AND ID =========\n")
print(f"""
Name      : {name}
Data type : {type(name)}
ID        : {id(name)}
""")

print(f"""
Age       : {age}
Data Type : {type(age)}
ID        : {id(age)}""")

print(f"""
Height    : {height}
Data Type : {type(height)}
ID        : {id(height)}""")

print(f"""
Favorit Number : {fav_num})
Data Type : {type(fav_num)}
ID : {id(fav_num)}""")

print("\nThenk You For Using The Pesonal Data Collector Goodbye!")



        
