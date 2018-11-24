import unittest
from validate_email import *


class Test(unittest.TestCase):
    def test_filter_mail(self):
        e = ['dheeraj-234@gmail.com','itsallcrap','harsh_1234@rediff.in','kunal_shin@iop.az','matt23@@india.in']
        self.assertEqual(['dheeraj-234@gmail.com', 'harsh_1234@rediff.in', 'kunal_shin@iop.az'], filter_mail(e))
