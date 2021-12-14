from unittest import TestCase
from learn_day017.Validation import validation_zipcode


class TestAddressValidation(TestCase):

    @staticmethod
    def setUpClass() -> None:
        print("Setup Class Method for TestAddressValidation ")

    def setUp(self) -> None:
        print("Setup method for TestAddressValidation")

    def tearDown(self) -> None:
        print("tearDown method for TestAddressValidation")

    @staticmethod
    def tearDownClass() -> None:
        print("tearDownClass method for TestAddressValidation")


    def test_general_zipCode(self):
        print("test_general_zipCode")
        self.assertTrue(validation_zipcode("33639"))

    def test_general_zipCode_wrong(self):
        print("test_general_zipCode_wrong")
        self.assertFalse(validation_zipcode("336391"))