import unittest
from utils import tinhTong

class TestUtils(unittest.TestCase):
    def test_result(self):
        self.assertAlmostEqual(tinhTong(10,20),30)
        self.assertAlmostEqual(tinhTong(10,21),31)

    def test_value(self):
        self.assertRaises(ValueError,tinhTong,-1,2)
        self.assertRaises(ValueError,tinhTong,-1,20)
    
    def test_type(self):
        self.assertRaises(TypeError,tinhTong,'xx','yy')