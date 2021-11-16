company = "hello, h2KInfosys"
age = "21"
hello = "Something"
print(company)
print(company[0])
print(company[10])
print(company[1:5]) # start:end+1
print(company[:5])
print(company[6:])
print(company[-3:])
print("Revere the sting ::" , company[::-1])

# HW : Reverse a String in single statement - rishi.h2kinfosys@gmail.com
print("len(company) ::" , len(company))
print("company.upper() ::" , company.upper())
print("company.lower() ::" , company.lower())
print("company.title() ::" , company.title())
print("company.capitalize() ::" , company.capitalize())
print("company.replace() ::" , company.replace('l', 'J'))
separated_string = company.split(',')
print("company.split() ::" , separated_string)
print("Just hello " , separated_string[0])
# Boolean checks on inside values
print("company.isdigit() ::" , company.isdigit())
print("age.isdigit() ::" , age.isdigit())
print("company.isnumeric() ::" , company.isnumeric())
print("age.isnumeric() ::" , age.isnumeric())
print("company.isalpha() ::" , company.isalpha())
print("hello.isalpha() ::" , hello.isalpha())

# take an input name and print if its alpha or not
name = input("Enter You Name:")
print("Valid Name is: " , name.isalpha())
age = input("Enter Your Age:")
print("Valid Age " , age.isnumeric())
# Add 10 to age
print(type(age))
print("Add 10 to age", (int(age)+10))


