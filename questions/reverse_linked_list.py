# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # if not head.next:
        #     return head
        
        # curr = head.next
        # new_head = head.next
        # prev = head
        # prev.next = None
        # while curr:
        #     new_head.next = prev
        #     prev = curr
        #     new_head = curr.next
        #     curr = curr.next
        # return new_head

        prev = None
        while head:
            curr = head
            head = head.next
            curr.next = prev
            prev = curr
        return prev

        # cur, prev = head, None
        # while cur:
        #     cur.next, prev, cur = prev, cur, cur.next
        # return prev

    # def reverseList(self, head: ListNode) -> ListNode:
    #     if not head or not head.next:
    #         return head
    #     node = self.reverseList(head.next)
    #     head.next.next = head
    #     head.next = None
    #     return node

    # def reverseList(self, head, prev=None):
    #     if not head:
    #       return prev
  
    #     curr, head.next = head.next, prev
    #     return self.reverseList(curr, head)