import unittest
from learn_day017.TestAddressValidation import TestAddressValidation
from learn_day017.TestCustomerValidation import TestCustomerValidation


test_cases = (TestCustomerValidation, TestAddressValidation)

def load_tests():
    suite = unittest.TestSuite()
    for test_class in test_cases:
        tests = unittest.TestLoader().loadTestsFromTestCase(test_class)
        suite.addTests(tests)
    return suite

#suite.addTest(TestStoreApplication("test_validate_survey_age_15"))
#suite.addTest(TestStringFunctions("test_string_uppar"))
runner = unittest.TextTestRunner()
runner.run(load_tests())
