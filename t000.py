# solution of leetcode.com or leetcode-cn.com


# 单链表结点定义
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 列表转单链表
def list_to_link(lists):
    link = tmp = ListNode(0)
    for l in lists:
        tmp.next = ListNode(l)
        tmp = tmp.next
    return link.next


# 单链表转列表
def link_to_list(link):
    l = []
    while link is not None:
        l.append(link.val)
        link = link.next
    return l


# 小顶堆，移出堆顶，item:(num, object)
def heappop(lists):
    top = lists[0]
    lists[0], lists[-1] = lists[-1], lists[0]
    del lists[-1]
    i = 0
    while 2*i+1 < len(lists):
        l = 2 * i + 1
        r = l + 1
        if r < len(lists):
            if lists[r][0] > lists[l][0]:
                if lists[i][0] > lists[l][0]:
                    lists[i], lists[l] = lists[l], lists[i]
                    i = l
                else:
                    break
            else:
                if lists[i][0] > lists[r][0]:
                    lists[i], lists[r] = lists[r], lists[i]
                    i = r
                else:
                    break
        else:
            if lists[i][0] > lists[l][0]:
                lists[i], lists[l] = lists[l], lists[i]
            break
    return top


# 小顶堆，入堆，item:(num, object)
def heappush(lists, item):
    lists.append(item)
    i = len(lists) - 1
    while (i-1)//2 >= 0:
        p = (i-1)//2
        if lists[i][0] < lists[p][0]:
            lists[i], lists[p] = lists[p], lists[i]
            i = p
        else:
            break


# 打印列表形式的二叉树，item:(num, object)
def print_heap(lists):
    n = len(lists)
    h = 0
    h_n = 1
    while n > 0:
        h += 1
        n -= h_n
        h_n *= 2
    h_ = 1
    max_space = 1
    for val, _ in lists:
        if len(str(val)) > max_space:
            max_space = len(str(val))
    for i in range(len(lists)):
        val = lists[i][0]
        if i+1 > 2**h_-1:
            h_ += 1
        if i+1 == 2**(h_-1):
            print((2**(h-h_)-1)*max_space*' ', end='')

        print(str(val)+(max_space-len(str(val)))*' ', end='')
        if i+1 == 2**h_-1:
            print()
        else:
            print((2**(h-h_+1)-1)*max_space*' ', end='')
    print('\n')


# 二叉树结点定义
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 列表转二叉树
def list_to_tree_link(lists):
    if len(lists) == 0:
        return None
    root = TreeNode(lists[0])
    for idx, val in enumerate(lists[1:]):
        if val is None:
            continue
        idx += 1
        stack = []
        while idx > 0:
            if idx % 2 == 0:
                stack.append(1)
                idx = idx // 2 - 1
            else:
                stack.append(0)
                idx = idx // 2
        tmp = root
        for t in stack[1:][::-1]:
            if t == 0:
                tmp = tmp.left
            else:
                tmp = tmp.right
        if stack[0] == 0:
            tmp.left = TreeNode(val)
        else:
            tmp.right = TreeNode(val)
    return root
