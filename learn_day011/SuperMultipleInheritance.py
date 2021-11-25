class Address:
    def __init__(self, address):
        self.address = address
        print("Address provided ", address)


class ValidAddress(Address):
    def __init__(self, address, zipcode):
        super().__init__(address)
        self.zipcode = zipcode
        print("Zipcode is provided with ", self.address)


class ValidNumber(Address):
    def __init__(self, address, zipcode = None):
        super().__init__(address)
        print("house_number is provided with ", self.address)


class CustomerAddress(ValidAddress, ValidNumber):
    def __init__(self, address, zipcode):
        super().__init__(address, zipcode)
        print("DONE!")


cust01 = CustomerAddress("1234 Somebody Blvd, FewCity 99887", 3434)