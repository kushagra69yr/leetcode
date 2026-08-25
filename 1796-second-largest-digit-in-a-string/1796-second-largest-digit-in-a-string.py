class Solution(object):
    def secondHighest(self, s):

        nums = set(c for c in s if c.isdigit())

        if len(nums) < 2:
            return -1

        nums.remove(max(nums))
        return int(max(nums))
        