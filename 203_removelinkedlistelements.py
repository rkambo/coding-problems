# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        temp = dummy
        
        while temp:
            while temp.next and temp.next.val == val:
                temp.next = temp.next.next
            temp = temp.next
        return dummy.next