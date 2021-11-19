# known unknown parameters - handle known first , args later
def validation(address, county, zipcode, *args):
    str_address = str(address)
    print(str_address, county)
    if str(zipcode).isdigit():
        print("Valid ZipCode")
    else:
        print("Invalid ZipCode")
    for eachArg in args:
        print(eachArg)


validation("Something", "Smryna", 30080, "address Line 2", "GA", "Atlanta")
validation(57, "abc", "ABC89", "address Line 2", "FL", "Tampa")