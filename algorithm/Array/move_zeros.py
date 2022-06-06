def moveZeroes(nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    i = 0
    j = 1
    while j < len(nums) and i < len(nums):
        if nums[i] == 0:
            if i >= j:
                j = i + 1
            if j >= len(nums):
                break
            # swap the position
            for k in range(j, len(nums)):
                if nums[k] != 0:
                    j = k
                    break
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp
            j = j + 1
            i = i + 1
        else:
            i += 1

