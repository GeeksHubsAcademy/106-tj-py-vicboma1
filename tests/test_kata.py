import pytest
import unittest   # The test framework

from kata import apply

class Test_kata(unittest.TestCase):
    
    def test_apply_1(self):
        expected = -1
        result = apply(None)
        assert(expected == result) 

    def test_apply_2(self):
        expected = -1
        result = apply([])
        assert(expected == result) 


    def test_apply_3(self):
        expected = 1
        result = apply([1])
        assert(expected == result) 


    def test_apply_4(self):
        expected = 2
        result = apply([1, 0, 2])
        assert(expected == result) 


    def test_apply_5(self):
        expected = 2
        result = apply([1, 2, 2])
        assert(expected == result) 


    def test_apply_6(self):
        expected = 2
        result = apply([1, 2, 2, 9])
        assert(expected == result) 

    def test_apply_7(self):
        expected = 20
        result = apply([1, 2, 2, 1, 10])
        assert(expected == result) 


    def test_apply_8(self):
        expected = 10
        result = apply([1, 2, 2, 1, 5, 7])
        assert(expected == result) 


    def test_apply_9(self):
        expected = 630
        result = apply([1, 2, 2, 1, 7, 10, 45])
        assert(expected == result) 


    def test_apply_10(self):
        expected = 1260
        result = apply([1, 2, 2, 1, 7, 10, 45, 0, 2])
        assert(expected == result) 


    def test_apply_11(self):
        expected = 100
        result = apply([10, 0, 5, 1, 2])
        assert(expected == result) 


    def test_apply_12(self):
        expected = -25
        result = apply([-5, 0, 5])
        assert(expected == result) 


    def test_apply_13(self):
        expected = 8
        result = apply([2, 0, -2, 0, -2])
        assert(expected == result) 
 
    

if __name__ == '__main__':
	unittest.main()