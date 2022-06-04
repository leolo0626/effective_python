#Find the maximum Subarray

#O(n^3)
def find_max_sum_in_subarray (arr) :
    n = len(arr)
    max_total = 0
    for i in range(n) :
        for j in range(i, n):
            total = sum(arr[i:j])
            max_total = max(max_total, total)
    return max_total

#O(n^2)
def find_max_sum_in_subarray_2 (arr):
    n = len(arr)

    max_total = 0
    for i in range(n):
        cur_sum = 0
        for j in range(i, n-1):
            cur_sum += arr[j]
            max_total = max(max_total, cur_sum)
    return max_total

#O(n)
def find_max_sum_in_subarray_3 (arr):
    maxSub = arr[0]
    curSum = 0

    for n in arr :
        if curSum < 0:
            curSum = 0
        curSum += n
        maxSub = max(maxSub, curSum)
    return maxSub


if __name__ == "__main__" :
    arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(find_max_sum_in_subarray(arr))
    print(find_max_sum_in_subarray_2(arr))
    print(find_max_sum_in_subarray_3(arr))
