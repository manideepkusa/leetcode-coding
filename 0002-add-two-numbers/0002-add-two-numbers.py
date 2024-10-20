# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummyNode=ListNode()
        curr=dummyNode
        carry=0
        while l1 or l2:
            v1=l1.val if l1 else 0
            v2=l2.val if l2 else 0
            sum=v1+v2+carry
            ele=sum%10
            carry=sum//10
            curr.next=ListNode(ele)
            
            curr=curr.next
            if l1:
                l1=l1.next
            if l2:
                l2=l2.next
        if carry ==1 :
            curr.next=ListNode(carry)
        return dummyNode.next
        