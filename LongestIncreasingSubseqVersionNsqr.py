#https://leetcode.com/problems/longest-increasing-subsequence/

class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        size = len(nums)
        seq = [0 for x in range(size)]
        index  = size - 1
        seq[index] = 1
        index -= 1
        while index >= 0:
            inner = size - 1
            while inner > index:
                if nums[index] < nums[inner]:
                    if seq[index] < seq[inner] + 1:
                        seq[index] = seq[inner] + 1
                
                inner -= 1
            if seq[index] == 0:
                seq[index] = 1
            
            index -= 1
        max_seq = 0
        for i in seq:
            if i  > max_seq:
                max_seq = i
        return max_seq
        
