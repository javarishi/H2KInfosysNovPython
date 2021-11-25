class Customer(object):

    def __init__(self, gender, age, height):
        self.gender = gender
        self.age = age
        self.height = height
        self.discount = 2
        print("Customer Created with ", self.gender, self.age, self.height)

    def get_discount(self):
        print("Customer Discount % is " , self.discount)


# Child doesnt have init - its going to use Parent's init
class PreferredCustomer(Customer):

    def __init__(self, gender, age, height, name, email, address):
        Customer.__init__(self, gender, age, height)
        self.name = name
        self.email = email
        self.address = address
        self.discount = 5 # shadowing variable
        print("This is Preferred Customer ", self.name, self.email, self.address)

    def send_promotions(self):
        print("Send Promotions to ", self.email)
        print("Send Promotions to ", self.address)

    def get_discount(self):
        Customer.get_discount(self)
        print("Preferred Customer Discount from Email Coupons " , self.email)


class CreditCardCustomer(PreferredCustomer):

    def __init__(self, gender, age, height, name, email, address, cell_num, ssn_num):
        PreferredCustomer.__init__(self, gender, age, height, name, email, address)
        self.cell_phone = cell_num
        self.ssn = ssn_num
        print("Credit Card Customer is Created - send text to ", self.cell_phone)

    def process_loyalty_points(self):
        print("For each $4 purchase - customer will get 1 Loyalty Point ", self.email)

    def send_promotions(self):
        print("Send Promotions to ", self.cell_phone)
        print("Send Promotions to ", self.email)


'''
pCust01 = PreferredCustomer('M', 22, 172, "Neil", "neil.armstrong@nasa.com", "13 Apollo Street, Moon Lander")
pCust01.get_discount()
pCust01.send_promotions()
'''
ccCust01 = CreditCardCustomer('M', 22, 172, "Neil", "neil.armstrong@nasa.com", "13 Apollo Street, Moon Lander", '43294324', '3247832894')
ccCust01.process_loyalty_points()
ccCust01.send_promotions()
ccCust01.get_discount()

