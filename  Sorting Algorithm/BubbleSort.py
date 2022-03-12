def bubbleSort(nums):
    """
    冒泡排序
    :param nums:
    :return:
    """
    for i in range(len(nums)):
        for j in range(len(nums) - i - 1):
            if nums[j] > nums[j + 1]:
                t = nums[j]
                nums[j] = nums[j + 1]
                nums[j + 1] = t
    return nums


if __name__ == '__main__':
    print(bubbleSort([3, 2, 1, 4, 8, -1]))
    print(bubbleSort([3, 2, 1]))
