class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        l1_list = []
        l2_list = []   
        s1 = ""
        s2 = ""
        
        while l1:
            l1_list.append(l1.val)
            l1 = l1.next
        
        while l2:
            l2_list.append(l2.val)
            l2 = l2.next
        
        for x in l1_list[::-1]:
            s1 += str(x)
        for y in l2_list[::-1]:
            s2 += str(y)
        
        total = int(s1) + int(s2)
        
        a = b = ListNode(-1)
        
        for x in str(total)[::-1]:
            a.next = ListNode(x)
            a = a.next
        
        return b.next
