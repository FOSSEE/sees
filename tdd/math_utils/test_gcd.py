import gcd
import unittest

class TestGcdFunction(unittest.TestCase):

    def setUp(self):
        self.test_file = open('gcd_testcases.dat')
        self.test_cases = []
        for line in self.test_file:
            values = line.split(', ')
            a = int(values[0])
            b = int(values[1])
            g = int(values[2])

            self.test_cases.append([a, b, g])

    def test_gcd(self):
        for case in self.test_cases:
            a = case[0]
            b = case[1]
            g = case[2]
            self.assertEqual(gcd.gcd(a, b), g)

    def tearDown(self):
        self.test_file.close()
        del self.test_cases

if __name__ == '__main__':
    unittest.main()
