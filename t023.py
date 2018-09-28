
from t000 import ListNode, heappush, heappop


class Solution:
    """ 23
    合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。
    """
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        result = ListNode(0)
        tmp = result
        lis = []
        for l in lists:
            if l is not None:
                heappush(lis, (l.val, l))
        while len(lis) != 0:
            _, node = heappop(lis)
            tmp.next = node
            tmp = tmp.next
            if node.next is not None:
                heappush(lis, (node.next.val, node.next))
        return result.next
