class Solution(object):
    def intersect(self, nums1, nums2):
        common = list(set(nums1)&set(nums2))
        ans = []
        count1 = 0
        count2 = 0
        for i in common:
            for n in nums1:
                if ( i == n ):
                     count1 = count1 + 1
            for m in nums2:
                if ( i == m ):
                     count2 = count2 + 1
            
            ans = ans + [ i for j in range(min(count1,count2)) ]

            count1 = 0
            count2 = 0
        return ans
        