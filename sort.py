
def bub(arr):
    """冒泡排序"""
    length = len(arr)
    while length > 1:
        for i in range(1, length):
            if arr[i-1] > arr[i]:
                arr[i-1], arr[i] = arr[i], arr[i-1]
        length -= 1
    return arr


def sel(arr):
    """选择排序"""
    i = 0
    while i+1 < len(arr):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[min_idx], arr[i] = arr[i], arr[min_idx]
        i += 1
    return arr


def ins(arr):
    """插入排序"""
    i = 1
    while i < len(arr):
        for j in reversed(range(i)):
            if arr[j] > arr[j+1]:
                arr[j+1], arr[j] = arr[j], arr[j+1]
            else:
                break
        i += 1
    return arr


def mer(arr):
    """归并排序"""
    def merge(arr1, arr2):
        result = []
        i, j = 0, 0
        while i < len(arr1) and j < len(arr2):
            if arr1[i] < arr2[j]:
                result.append(arr1[i])
                i += 1
            else:
                result.append(arr2[j])
                j += 1
        while i < len(arr1):
            result.append(arr1[i])
            i += 1
        while j < len(arr2):
            result.append(arr2[j])
            j += 1
        return result
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2
    left = mer(arr[:mid])
    right = mer(arr[mid:])
    return merge(left, right)


def qui(arr):
    """快速排序"""
    pass


if __name__ == "__main__":
    print(bub([1, 3, 4, 0, 8, 6, 3, 8]))
    print(sel([1, 3, 4, 0, 8, 6, 3, 8]))
    print(ins([1, 3, 4, 0, 8, 6, 3, 8]))
    print(mer([1, 3, 4, 0, 8, 6, 3, 8]))
