from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def make_list(lst: List[int]) -> ListNode:
    head, prev = None, None

    for value in lst:
        node = ListNode(value)

        if head is None:
            head = node
        else:
            prev.next = node

        prev = node

    return head


def print_list(head: ListNode):
    while head:
        print(head.val, end=' ')
        head = head.next

    print()


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        prev, head = None, None
        carry = 0

        while l1 or l2:
            digit1 = l1.val if l1 else 0
            digit2 = l2.val if l2 else 0
            digit = carry + digit1 + digit2
            node = ListNode(digit % 10)
            carry = digit // 10

            if head is None:
                head = node
            else:
                prev.next = node

            prev = node

            if l1:
                l1 = l1.next

            if l2:
                l2 = l2.next

        if carry:
            prev.next = ListNode(carry)

        return head


if __name__ == '__main__':
    solution = Solution()
    print_list(solution.addTwoNumbers(make_list([2, 4, 3]), make_list([5, 6, 4])))
    print_list(solution.addTwoNumbers(make_list([0]), make_list([0])))
    print_list(solution.addTwoNumbers(make_list([9, 9, 9, 9, 9, 9, 9]), make_list([9, 9, 9, 9])))
