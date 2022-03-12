import collections


def swap_param(heap, i, j):
    """
    交换堆顶元素和堆中最下最右元素
    :param heap:
    :param i:
    :param j:
    :return:
    """
    heap[i], heap[j] = heap[j], heap[i]
    return heap


def head_adjust(heap, start, end):
    """
    构建堆的过程
    :param heap:
    :param start:
    :param end:
    :return:
    """
    temp = heap[start]
    i = start
    j = 2 * i

    while j <= end:
        if j < end and heap[j] < heap[j + 1]:
            j += 1
        if temp < heap[j]:
            heap[i] = heap[j]
            i = j
            j = 2 * i
        else:
            break
    heap[i] = temp


def heapSort(nums):
    """
    堆排序
    :param nums:
    :return:
    """
    heap = collections.deque(nums)
    heap.appendleft(0)
    heap_len = len(heap) - 1
    first_sort_count = heap_len // 2
    # 将序列调整为一个大根堆
    for i in range(first_sort_count):
        head_adjust(heap, first_sort_count - i, heap_len)

    # 交换堆顶元素和最右最下元素，然后重新构建大根堆
    for i in range(heap_len - 1):
        # 将堆顶最大的元素和最后一个元素交换位置，并把最后的位置固定下来
        heap = swap_param(heap, 1, heap_len - i)
        # 将最后一个位置之前的序列重新构建成一个大根堆
        head_adjust(heap, 1, heap_len - i - 1)

    return [heap[i] for i in range(1, len(heap))]


if __name__ == '__main__':
    print(heapSort([3, 2, 1, 4, 8, -1]))
    print(heapSort([19, 12, 11, 9, 8, -1]))
