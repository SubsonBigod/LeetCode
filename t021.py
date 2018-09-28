
from t000 import ListNode


class Solution:
    """ 21
    将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。
    """
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = ListNode(0)
        tmp = result
        while l1 is not None and l2 is not None:
            if l1.val < l2.val:
                tmp.next = ListNode(l1.val)
                l1 = l1.next
            else:
                tmp.next = ListNode(l2.val)
                l2 = l2.next
            tmp = tmp.next
        if l1 is not None:
            tmp.next = l1
        if l2 is not None:
            tmp.next = l2
        return result.next
