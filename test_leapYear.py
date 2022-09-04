
import unittest
import LeapYear


class TestLeapYear(unittest.TestCase):
    
    def test_LeapYear(self):
        result=LeapYear.LeapYear(-2000)
        self.assertEqual(result,"Year cannot be negative")  # If the year is negative it cannot be taken as Input 


    if __name__=="__main__":
        unittest.main()