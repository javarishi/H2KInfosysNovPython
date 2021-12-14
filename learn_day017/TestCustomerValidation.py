from unittest import TestCase
from learn_day017.Validation import validate_age

'''
EBC - 17, 18, 19, 120, 121, 122, 50
Negative - -45
String Value - 12ABC
Zero - 0
Special Chara - 12$
'''

class TestCustomerValidation(TestCase):

    def test_validate_age_18(self):
        age = 18
        actual_result = validate_age(age)
        expected = True
        self.assertEqual(expected, actual_result)

    def test_validate_age_121(self):
        age = 121
        actual_result = validate_age(age)
        expected = False
        self.assertEqual(expected, actual_result)

    def test_validate_age_50(self):
        age = 50
        actual_result = validate_age(age)
        expected = True
        self.assertEqual(expected, actual_result)

    def test_validate_age_negative(self):
        age = -50
        with self.assertRaises(ValueError):
            validate_age(age)

    def test_validate_age_stringage(self):
        age = "12GHG"
        with self.assertRaises(ValueError):
            validate_age(age)

