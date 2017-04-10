class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num < 1:
            return 0
            
        high = num + 1
        low = 1
        
        while low < high:
            mid = low + (high-low)/2
            product =  mid * mid 
            if product > num:
                high = mid
            elif product < num:
                low = mid + 1
            else:
                return True
        return False
