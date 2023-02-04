class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        list_ans = ListNode()
        carry, list_ans.val = divmod(l1.val + l2.val, 10)
        if carry:
            list_ans.next = self.addTwoNumbers(
                ListNode(1), self.addTwoNumbers(l1.next, l2.next)
            )
        else:
            list_ans.next = self.addTwoNumbers(l1.next, l2.next)
        return list_ans
