class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k=sorted(set(nums))
        if len(k)>=3:
            return k[-3]
        else:
            return k[-1]