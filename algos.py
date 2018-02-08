# binary search
class search(object):
	def binary_search(self, nums, target):
		'''
		:type nums: List[int]
		:rtype: int
		'''
	
		left = 0
		right = len(nums)-1
		output = 0
		'''
		try:
			left > right
		except:
			print 'search unsuccesful'
		'''
		while left <= right:
			m = int((left + right)*1.0/2)
			if nums[m] < target:
				left = m + 1
			elif nums[m] > target:
				right = m - 1
			elif nums[m] == target:
				output = m
				break
			else:
				pass
	
		return(output)

s = search()
nums = [1,2,3,4,5]
target = 3
print s.binary_search(nums, target)
