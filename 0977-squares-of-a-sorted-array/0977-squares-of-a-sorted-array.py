class Solution(object):
    def sortedSquares(self, nums):
        
        sq_list = [num**2 for num in nums]
        sq_list.sort()
        return sq_list