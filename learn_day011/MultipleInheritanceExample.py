from Tools.scripts.var_access_benchmark import C


class Customer:

    def __init__(self, name, address):
        self.name = name
        self.address = address
        print("Customer Constructor ", self.name, self.address)

    def purchase(self):
        print("Customer made a Purchase", self.name)

    def address_validation(self):
        print("Very Simple USPS Based Address Validation")


class GoogleMapValidator:

    def __init__(self, address):
        self.address = address
        print("Google Map Validation Class", self.address)

    def address_validation(self):
        print("Address Validation with Google Map", self.address)


class PreferredCustomer(Customer, GoogleMapValidator):

    def __init__(self, name, address):
        Customer.__init__(self, name, address)
        GoogleMapValidator.__init__(self, address)
        print("Preferred Customer Initialization")

    def address_validation(self):
        GoogleMapValidator.address_validation(self)


class CreditValidator:

    def __init__(self, ssn):
        self.ssn = ssn
        print("CreditValidator Validation Class", self.ssn)

    def credit_validation(self):
        print("Credit Validation with Experian", self.ssn)


class CreditCardCustomer(PreferredCustomer, CreditValidator):

    def __init__(self, name, address, ssn, email):
        PreferredCustomer.__init__(self, name, address)
        CreditValidator.__init__(self, ssn)
        self.email = email
        print("CreditCardCustomer Constructor")




# default init will be from First Parent
#pCust = PreferredCustomer('Buzz Aldrine', '2210 Moon Land Parkway')
#pCust.purchase()
# If method is present in both Parents - First Parent gets preference
# You can call second class Constructor as well as method by explicit calling
#pCust.address_validation()

ccCust = CreditCardCustomer('Buzz Aldrine', '2210 Moon Land Parkway', '324234', 'some@dsfo.com' )
ccCust.purchase()
ccCust.address_validation()
ccCust.credit_validation()