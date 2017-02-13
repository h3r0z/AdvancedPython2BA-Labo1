# test_utils.py
# Author: Sébastien Combéfis
# Version: February 2, 2016

import unittest
import utils

class TestUtils(unittest.TestCase):
    def test_fact(self):
        self.assertEqual(utils.fact(0),0)
        self.assertEqual(utils.fact(3),6)
        pass
    
    def test_roots(self):
        self.assertEqual(utils.roots(2,1,3),())
        pass
    
    def test_integrate(self):
        self.assertEqual(utils.integrate(1,0,150),150)
        pass

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestUtils)
    runner = unittest.TextTestRunner()
    exit(not runner.run(suite).wasSuccessful()) 
