# known unknown parameters - handle known first , args later
def validation(address, county, zipcode, **kwargs):
    str_address = str(address)
    print(str_address, county)
    if str(zipcode).isdigit():
        print("Valid ZipCode")
    else:
        print("Invalid ZipCode")

    for key,value in kwargs.items():
        print(key, value)

validation("Something", "Smryna", 30080, addressL2="address Line 2", state= "GA", city="Atlanta")
validation(57, "abc", "ABC89", addressL2="address Line 2", state= "FL", city="Oldsmar")