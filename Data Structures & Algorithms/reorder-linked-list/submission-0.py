# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        
        # Count nodes
        count = 0
        cur = head
        while cur:
            count += 1
            cur = cur.next
        
        # Split list
        half = count // 2
        cur = head
        for _ in range(half - 1):
            cur = cur.next
        
        second = cur.next
        cur.next = None
        
        # Reverse second half
        prev = None
        cur = second
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        
        # Merge
        first = head
        second = prev

        while first and second:
            temp1 = first.next
            temp2 = second.next
            
            first.next = second
            
            if temp1 is None:
                break
                
            second.next = temp1
            
            first = temp1
            second = temp2