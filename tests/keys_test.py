import unittest
from pytils import keys


class KeysTest(unittest.TestCase):

    def test_alphanumeric_length(self):
        a = keys.alfanumeric(10)
        self.assertEqual(10, len(a))
        b = keys.alfanumeric(21)
        self.assertEqual(21, len(b))

    def test_alphanumeric(self):
        a = keys.alfanumeric(30)
        non_digits = all([x.isdigit() or x.isalpha() for x in a])
        self.assertTrue(non_digits)

    def test_alphanumeric_lowercase(self):
        a = keys.alfanumeric(30, keys.Case.LOWER)
        lower_case = all([x.islower() or x.isdigit() for x in a])
        self.assertTrue(lower_case)

    def test_alphanumeric_uppercase(self):
        a = keys.alfanumeric(30, keys.Case.UPPER)
        upper_case = all([x.isupper() or x.isdigit() for x in a])
        self.assertTrue(upper_case)

    def test_hexadecimal(self):
        a = keys.hexadecimal(10)
        print(a)
        lower_case = all([x.isupper() or x.isdigit() for x in a])
        self.assertTrue(lower_case)


if __name__ == '__main__':
    unittest.main()
