# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cur = head
        count = 1
        while cur:
            count += 1
            cur = cur.next
        cur = head
        prev = head
        print(count - n - 1)
        for i in range(count - n - 1):
            prev = cur
            cur = cur.next
        if (count - n - 1 == 0):
            return head.next
        if cur:
            prev.next = cur.next
        else:
            prev.next = None
        return head
        