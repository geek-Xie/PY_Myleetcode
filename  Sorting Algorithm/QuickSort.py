def quickSort(nums, low, high):
    """
    快速排序
    :param nums:
    :param low:
    :param high:
    :return:
    """
    i = low
    j = high
    if i > j:
        return nums
    temp = nums[i]
    while i < j:
        while i < j and nums[j] >= temp:
            j -= 1
        nums[i] = nums[j]
        while i < j and nums[i] <= temp:
            i += 1
        nums[j] = nums[i]
    nums[i] = temp

    quickSort(nums, low, i - 1)
    quickSort(nums, j + 1, high)

    return nums


if __name__ == '__main__':
    print(quickSort([3, 2, 1, 4, 8, -1], 0, 5))
    print(quickSort([19, 12, 11, 9, 8, -1], 0, 5))
    print(quickSort([3, 2, 1], 0, 2))
