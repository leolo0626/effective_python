
def merge(arr, start, mid, end):
    # build temp array to avoid modify the original contents
    temp = [0] * (end-start + 1)
    i, j , k = start, mid+1, 0

    # while both sub-array have values, then try and merge them in sorted value
    while i <= mid and j <= end :
        if arr[i] <= arr[j] :
            temp[k] = arr[i]
            i+=1
            k+=1
        else :
            temp[k] = arr[j]
            k+=1
            j+=1
    # Add the rest of left sub array to result
    while i <= mid :
        temp[k] = arr[i]
        k+=1
        i+=1
    # Add the rest of right sub array to result
    while j <= end :
        temp[k] = arr[j]
        k+=1
        j+=1
    # inplace the value
    for i in range(start, end+1) :
        arr[i] = temp[i-start]



def merge_sort(arr, start, end):
    if (start < end) :
        mid = (start + end) // 2
        merge_sort(arr, start, mid)
        merge_sort(arr, mid+1, end)
        merge(arr, start, mid, end)

if __name__ == "__main__" :
    arr = [-5, 20, 10, 3, 2, 0]
    merge_sort(arr, 0, len(arr)-1)
    print(arr)


