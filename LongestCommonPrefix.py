#Solution to https://leetcode.com/problems/longest-common-prefix/discuss/
#Toggle commented lines to get a variation of the longest common prefix problem - longest common subsequence :)
#Run time in big O notaion = (O)m * n where m is number of strings and n is the length of the shortest string.
# runtime = m + (m * n)

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return "" 
        pref = ""
        old = ""
        new = ""
        numOfStrs = len(strs)
        length = float("inf")
        choice = ""
        #find shortest string
        # runtime = m
        for string in strs:
            l = len(string)
            if l == 0:
                return ""
            else:
                if l < length:
                    length = l 
                    choice = string
       
       #Use shortest string as iterator.
       #Benefit, avoids ArrayIndexOutOfBoundsError, makes it simple and intuitive
       #Cons, adds extra runtime (m) above.
       
       #runtime = m * n
        for idx,c in enumerate(choice):
            count = 0
            for ring in strs:
                if c == ring[idx]:
                    count += 1
                else:
                    return pref #comment and uncomment others
                    #if len(pref) > 0 and len(pref) > len(old):
                        #old = pref
                        #pref = ""
                    #else:
                        #pref = ""
            if count == numOfStrs:
                pref += c
        
        #if len(pref) > 0 and len(pref) > len(old):
        #    old = pref
        #    pref = ""             
        return pref    
        
