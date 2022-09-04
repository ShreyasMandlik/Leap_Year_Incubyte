
import unittest
from unittest import result
import LeapYear


class TestLeapYear(unittest.TestCase):
    
    def test_leapYear(self):

        result=LeapYear.LeapYear(-2000)
        stri="Year cannot be negative"
        self.assertEqual(result,stri) 
  
        result1=LeapYear.LeapYear(2000)
        self.assertEqual(result1,True)             # If the year is divisible by 400 then it is leap year


    if __name__=='__main__':
        unittest.main()
