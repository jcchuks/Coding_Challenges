class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        
        Note variations, 
        to go low, set high to mid on find. 
        to go high, set low to mid + 1 on find
        """
        
        
        index1 = -1
        index2 = -1
        if not nums:
            return [index1,index2]
        high = len(nums)
        low = 0
        while low < high:
            mid = low + (high - low)/2
            if nums[mid] > target:
                high = mid
            elif nums[mid]  < target:
                low = mid + 1
            else:
                index1 = mid
                high = mid 
                
        low = index1 
        high = len(nums)
        while low < high:
            mid = low + (high - low)/2
            if nums[mid] >  target:
                high = mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                index2 = mid 
                low = mid + 1
         
        return [index1,index2]
                
                
        
