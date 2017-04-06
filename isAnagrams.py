
#https://leetcode.com/submissions/detail/99215025/
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
         
        s = sorted(s)
        t = sorted(t)
        return s == t
