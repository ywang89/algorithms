import unittest

# binary search
class search(object):
    def last_position(self, nums, target):
        '''
        :type nums: List[int]
        :type target: int
        :rtype: int
        '''
        if nums is None or len(nums) == 0:
            return -1
        	
        left = 0
        right = len(nums)-1
            
        while left + 1 < right:
            m = int( left + (right - left) * 1.0 / 2 ) # prevent overflow
            if nums[m] == target:
                left = m
            elif nums[m] < target:
                left = m
            elif nums[m] > target:
                right = m
            else:
                pass
        
        if nums[right] == target:
            return right
        elif nums[left] == target:
            return left
        else:
            return -1

# Here's our "unit tests".
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
