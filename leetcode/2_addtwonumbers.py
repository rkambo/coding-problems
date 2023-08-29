# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        head = dummy
        temp = l1
        temp2 = l2
        carry = 0
        
        while temp or temp2:
            if temp and not temp2:
                sumVal = temp.val + carry
                if sumVal >= 10:
                    dummy.next = ListNode(sumVal - 10)
                    carry = 1
                else:
                    dummy.next = ListNode(sumVal)
                    carry = 0
                temp = temp.next
            elif temp2 and not temp:
                sumVal = temp2.val + carry
                if sumVal >= 10:
                    dummy.next = ListNode(sumVal - 10)
                    carry = 1
                else:
                    dummy.next = ListNode(sumVal)
                    carry = 0
                temp2 = temp2.next
            else:
                sumVal = temp.val + temp2.val + carry
                if sumVal >= 10:
                    dummy.next = ListNode(sumVal - 10)
                    carry = 1
                else:
                    dummy.next = ListNode(sumVal)
                    carry = 0
                temp = temp.next
                temp2 = temp2.next
            dummy = dummy.next
            
        if carry == 1:
            dummy.next = ListNode(1)
        
        return head.next