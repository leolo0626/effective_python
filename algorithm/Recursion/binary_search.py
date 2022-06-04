def binary_search(arr, left, right, tar) :
    if left > right :
        return -1

    mid = (left + right)//2

    if arr[mid] == tar :
        return mid

    if tar < arr[mid] :
        return binary_search(arr, left, mid-1, tar)

    return binary_search(arr, mid+1, right, tar)

if __name__ == "__main__" :
    arr = [-1, 0, 1, 2, 3, 4, 7, 9, 10, 20]
    print(binary_search(arr, 0, len(arr)-1, 7))