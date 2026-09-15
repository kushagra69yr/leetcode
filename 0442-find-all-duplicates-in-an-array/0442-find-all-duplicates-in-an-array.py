class Solution(object):
    def findDuplicates(self, nums):
        seen = set()
        ans = []
        for n in nums:
            if n in seen:
                ans.append(n)
            else:
                seen.add(n)
        return ans
        