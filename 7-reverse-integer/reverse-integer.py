class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        # 123 -> 321
        newNum = 0
        sign = 1 if x > 0 else -1
        x = abs(x)

        while x > 0:
            rem = x % 10
            newNum = newNum * 10 + rem
            if newNum > 2**31 - 1:
                return 0
            x = x/10 
        
        return newNum * sign
        