import unittest
from algos import search

# Unit tests for function last_position()
class is_last_postion_tests(unittest.TestCase):
    def test_1(self):
        s=search()
        nums_test = [1,2,3,4,5]
        target = 3
        self.failUnless(s.last_position(nums_test, target)==2)

    def test_2(self):
        s=search()
        nums_test = [1,2,3,3,4,5]
        target = 3
        self.failUnless(s.last_position(nums_test, target)==3)

    def test_3(self):
        s=search()
        nums_test = [3]
        target = 3
        self.failUnless(s.last_position(nums_test, target)==0)

    def test_4(self):
        s=search()
        nums_test = [3,3]
        target = 3
        self.failUnless(s.last_position(nums_test, target)==1)
        
    def test_5(self):
        s=search()
        nums_test = [1,2,4,5]
        target = 3
        self.failUnless(s.last_position(nums_test, target)==-1)

def main():
    unittest.main()

if __name__ == '__main__':
    main()
