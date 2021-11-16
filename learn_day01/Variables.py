# Dynamically Typed Programming Language

age = 28
age_21 = 21
_ = 100

Age = 22
AGE = 23
print(age, Age, AGE)

percentage = 99.14
name = "David"
complex_data = 1 + 6j
isValidZipCode = False

print(age, type(age))
print(percentage, type(percentage))
print(name, type(name))
print(complex_data, type(complex_data))
print(isValidZipCode, type(isValidZipCode))

new_percentage = int(percentage)
print(new_percentage, type(new_percentage))
store_number = int("1001")
print(store_number, type(store_number))

tax = 0.02
total_price = 1200
final_price = int( (tax*total_price) + total_price)
print(final_price, type(final_price))


