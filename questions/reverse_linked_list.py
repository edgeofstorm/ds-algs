from ds.linked_list import LinkedList, Node
from typing import Optional


def solution(ll: Optional[LinkedList]) -> None:
    """
    create prev, curr
    prev is None
    in each iter:
        assign curr to head
        move head to head.next
        assign curr.next to prev
        assign prev to curr
    """
    prev = None
    while ll.head:
        curr = ll.head
        ll.head = ll.head.next
        curr.next = prev
        prev = curr
    ll.head = prev


def main():
    ll = LinkedList()
    for i in range(10, 0, -1):
        ll.insert(i)

    assert ll.print() == "1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> 10"
    solution(ll)
    assert ll.print() == "10 -> 9 -> 8 -> 7 -> 6 -> 5 -> 4 -> 3 -> 2 -> 1"


if __name__ == "__main__":
    main()


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


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
