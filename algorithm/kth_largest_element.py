# find k th largest element
# arr = [4, 2, 9, 7, 5, 6, 7, 1, 3]
# k = 4
# ans = 6
import heapq
#kth largest element
# O(nk)
def kth_largest_element(arr, k):
    for i in range(k-1):
        arr.remove(max(arr))

    return max(arr)

#second solution
#O(nlogn)
def kth_largest_element_2(arr, k):
    n = len(arr)
    arr.sort()
    return arr[n-k]

#Third solution
def kth_largest_element_3(arr, k):
    arr = [-elem for elem in arr]
    heapq.heapify(arr)
    for i in range(k-1):
        heapq.heappop(arr)
    return -heapq.heappop(arr)

if __name__ == "__main__" :
    test_arr = [4, 2, 9, 7, 5, 6, 7, 1, 3]
    print(kth_largest_element(test_arr, 4))
    test_arr = [4, 2, 9, 7, 5, 6, 7, 1, 3]
    print(kth_largest_element_3(test_arr, 4))