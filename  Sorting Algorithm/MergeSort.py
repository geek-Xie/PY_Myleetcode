def merge(left_sort, right_sort):
    left_index = 0
    right_index = 0
    res = []

    while left_index < len(left_sort) and right_index < len(right_sort):
        if left_sort[left_index] <= right_sort[right_index]:
            res.append(left_sort[left_index])
            left_index += 1
        else:
            res.append(right_sort[right_index])
            right_index += 1
    if left_index == len(left_sort):
        while right_index < len(right_sort):
            res.append(right_sort[right_index])
            right_index += 1
    else:
        while left_index < len(left_sort):
            res.append(left_sort[left_index])
            left_index += 1
    return res


def mergeSort(nums):
    """
    归并排序
    :param nums:
    :return:
    """
    if len(nums) == 1:
        return nums
    left_sort = mergeSort(nums[:len(nums) // 2])
    right_sort = mergeSort(nums[len(nums) // 2:])

    return merge(left_sort, right_sort)


if __name__ == '__main__':
    print(mergeSort([3, 2, 1, 4, 8, -1]))
    print(mergeSort([19, 12, 11, 9, 8, -1]))
    print(mergeSort([3, 2, 1]))
