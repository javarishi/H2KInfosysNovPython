class Employee:

    def __init__(self, empid=999):
        self.emp_id = empid
        print("This is Employee Initializer, Emp ID ", self.emp_id)

    def pay_roll(self):
        print("Employee Payroll, for emp ", self.emp_id)

    @staticmethod
    def print_company_name():
        print("Best Buy Inc.")


# constructor - initializer
emp01 = Employee(100) # instance creation will call initializer function __init__
emp01.pay_roll()
emp02 = Employee()
emp02.pay_roll()
emp02.print_company_name() # not a recommended way
Employee.print_company_name()