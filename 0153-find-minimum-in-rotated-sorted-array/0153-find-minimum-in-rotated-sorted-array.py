class Solution(object):
    def findMin(self, nums):

        smallest = nums[0]
        for n in nums:
            if n < smallest:
                smallest = n
        return smallest
        