#Given a sorted array of integer arr and an integer target, find index of first and last position of target in arr
#Otherwise, target can't be found in arr return [-1, -1]


# First solution : Brute force
def first_and_last_position(arr, target):
    startIdx = -1
    endIdx = -1
    i = 0
    while i < len(arr) :
        if startIdx == -1  and arr[i] == target:
            startIdx = i

        if startIdx != -1 and arr[i] == target :
            endIdx = i
            break
        i += 1

    if startIdx == -1 :
        return [-1, -1]
    return [startIdx, endIdx]

# Second solution : Binary solution
def start_index_helper(arr, target):
    if arr[0] == target :
        return 0
    left, right = 0, len(arr)-1
    while left <= right :
        mid = (left + right) // 2
        if arr[mid] == target and arr[mid-1] < target :
            return mid
        elif arr[mid] < target :
             left = mid + 1
        else :
            right = mid - 1
    return -1

def end_index_helper(arr, target):
    if arr[-1] == target :
        return len(arr) -1

    left, right = 0, len(arr)-1
    while left <= right :
        mid = (left + right) // 2
        if arr[mid] == target and arr[mid+1] > target :
            return mid
        elif arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return -1

def first_and_last_position_2(arr, target) :
    if len (arr) == 0 or arr[0] > target or arr[-1] < target :
        return [-1, -1]
    return [start_index_helper(arr, target) , end_index_helper(arr, target)]


if __name__ == "__main__":
    test_arr = [1, 2, 3, 3, 3, 3, 5]
    print(first_and_last_position([1, 2, 3, 3, 3, 3, 5], 3))
    print(first_and_last_position_2(test_arr, 3))