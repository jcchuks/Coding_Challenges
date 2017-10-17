# https://leetcode.com/problems/reverse-nodes-in-k-group/description/
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class keeper:
    def __init__(self):
        self.head = None
        self.count = 0
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        def reverse_group(prev_hd, head, k):
            count = 0 
            curr = head
            prev = None
            while count < k:
                if curr: 
                    nextnode = curr.next
                    curr.next = prev
                    prev = curr
                    curr = nextnode
                count += 1
            if prev_hd:
                prev_hd.next = prev 
            return nextnode, head, prev
        
                
        worker = keeper()
        if not head:
            return None 
        
        reversed_grp_head = head
        no_of_grp = 0
        next_grp_hd = head
        prev_grp_hd = None
        while next_grp_hd:
            
            while next_grp_hd and worker.count < k :
                if worker.count == 0:
                    worker.head = next_grp_hd
                worker.count += 1
                next_grp_hd = next_grp_hd.next
                
            if worker.count == k: 
                next_grp_hd,prev_grp_hd,prev_grp_tail = reverse_group( prev_grp_hd ,worker.head, k)
                worker.count = 0
                if no_of_grp == 0:
                    reversed_grp_head = prev_grp_tail
                no_of_grp += 1
            else:  
                if prev_grp_hd:
                    prev_grp_hd.next = worker.head
                return reversed_grp_head
     
        return reversed_grp_head
                
