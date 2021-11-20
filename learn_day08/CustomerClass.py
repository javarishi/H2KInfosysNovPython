class Customer:
    first_name = "David"
    last_name = "Copperfield"
    # methods - instance methods
    def discount(self):
        print(self.first_name , " received Discount of 5%")

    @staticmethod
    def store_location_promotion():
        print("Store Location Promotion")

# instance - object of class Customer
cust01 = Customer()
print(cust01.first_name, cust01.last_name)
# change variables
cust01.first_name = "Niel"
cust01.last_name = "Armstrong"
print(cust01.first_name, cust01.last_name)
cust01.discount()

cust02 = Customer()
print(cust02.first_name, cust02.last_name)
cust02.discount()

# static methods do not need instance to call
Customer.store_location_promotion()

# H.W. find type of instance function of a class and function without a class