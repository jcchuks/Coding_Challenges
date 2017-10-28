#https://leetcode.com/problems/combination-sum-ii/description/
class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """ 
 
        self.candidates = candidates
        self.size = len(candidates)
        self.rtype = [] 
        def findsums(valuesum,valuelist, index, target):  
            complete = False
            if valuesum > target:
                return
            elif valuesum == target:  
                if valuelist not in self.rtype:
                    self.rtype.append(valuelist)
                return
            while index < self.size:
                
                if valuesum + self.candidates[index] == target: 
                    good = valuelist[:]
                    good.append(self.candidates[index]) 
                    if good not in self.rtype:
                        self.rtype.append(good )
                        return
                elif valuesum + self.candidates[index] < target:
                    less = valuelist[:]
                    less.append(self.candidates[index])
                    findsums(valuesum + self.candidates[index],less,index + 1,target)
                elif valuesum + self.candidates[index] > target: 
                    great = valuelist[:]
                    return 
                index += 1
        count = 0
        self.candidates.sort()
        while count < self.size :
            findsums(self.candidates[count],[self.candidates[count]],count + 1,target)
            count += 1
        return self.rtype
