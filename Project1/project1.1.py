"""

先采用快速排序将数组变为有序数组，然后查找和为x的两个数

"""

S = [3, 4, 5, 2, 1]
x = 10
start = 0
end = len(S) - 1


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


# 找到和为x的两个数
def findsumx(array, start, end):
    # 从左到右进行比较
    while start < end:
        # 如果存在，则打印并返回
        if array[start] + array[end] == x:
            print("Exist sum is exactly x")
            return
        # 如果大于x，则大的值需要变小，end左移
        elif array[start] + array[end] > x:
            end -= 1
        # 如果小于x，则小的值需要变大，start右移
        elif array[start] + array[end] < x:
            start += 1
    # 若遍历后发现不存在，则需要说明不存在
    print("Not exist sum is exactly x")


quicksort(S, start, end)
print(S)

findsumx(S, start, end)

