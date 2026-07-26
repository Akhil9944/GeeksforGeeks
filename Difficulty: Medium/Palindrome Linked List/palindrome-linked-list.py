'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''

class Solution:
    def isPalindrome(self, head):
        # code here
        if not head or not head.next:
            return True
            
        slow=head
        fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            
        prev=None
        curr=slow
        while curr:
            next_node=curr.next
            curr.next=prev
            prev=curr
            curr=next_node
        first=head
        second=prev
        
        while second:
            if first.data!=second.data:
                return True if False else False
            first=first.next
            second=second.next
        return True
        