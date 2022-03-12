def insertSort(nums):
    """
    插入排序，第i次遍历假设前i - 1个元素所构成的子序列已经是有序的，在其中查找第i个元素所应该插入的位置，形成新的有序序列
    :param nums:
    :return:
    """
    for i in range(1, len(nums)):
        insert_index = -1
        for j in range(i):
            if nums[j] > nums[i]:
                insert_index = j
                break
        if insert_index != -1:
            insert_num = nums[i]
            for index_ in range(i - 1, insert_index - 1, -1):
                nums[index_ + 1] = nums[index_]
            nums[insert_index] = insert_num
    return nums


if __name__ == '__main__':
    print(insertSort([3, 2, 1, 4, 8, -1]))
    print(insertSort([3, 2, 1]))
