
#https://leetcode.com/problems/implement-strstr/#/description
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        lenh = len(haystack) 
        lenn = len(needle)
        if lenh == lenn and lenh < 1: #there is no needle and no haystack
            return 0 
        if lenn < 1 and lenh > 0: #haystack is larger than needle but there is no needle
            return 0
        elif lenh < 1 and lenn > 0: #needle is larger than haystack but there is no haystack
            return -1
        elif lenn > lenh: # needle is larger than haystack
            return -1
        else: #haystack is larger than needle but there is needle - We find the index.
            return haystack.find(needle)
