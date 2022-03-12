def selectSort(nums):
    """
    每一趟遍历数组，选择一个最小的数字，与当前的第一个数字做交换，固定在当前的第一位
    :param nums:
    :return:
    """
    for i in range(len(nums) - 1):
        mini_num = nums[i]
        mini_index = i
        for j in range(i, len(nums)):
            if nums[j] < mini_num:
                mini_index = j
        t = nums[i]
        nums[i] = nums[mini_index]
        nums[mini_index] = t

    return nums


if __name__ == '__main__':
    print(selectSort([3, 2, 1, 4, 8, -1]))
    print(selectSort([3, 2, 1]))