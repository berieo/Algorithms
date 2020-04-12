# 快速排序
def quicksort(array, start, end):
    if start >= end:
        return
    low = start
    high = end
    key = array[start]
    # 一直比较直到将所有数比较完
    while low < high:
        # 从右边遍历，如果发现小于的放在左边
        while low < high and array[high] >= key:
            high -= 1
        array[low] = array[high]
        # 从左边遍历，如果发现大于的放在右边
        while low < high and array[low] < key:
            low += 1
        array[high] = array[low]
    # 将key值放回数组
    array[low] = key
    quicksort(array, start, low - 1)
    quicksort(array, low + 1, end)
