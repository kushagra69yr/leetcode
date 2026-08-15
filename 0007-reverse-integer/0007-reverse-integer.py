class Solution:
    def reverse(self,x):
        sign = -1 if x <0 else 1
        x = abs(x)
        r = int(str(x)[::-1])
        r *=sign
        return r if -2**31 <= r <=2**31 -1 else 0