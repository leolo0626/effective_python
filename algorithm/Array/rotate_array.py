
def rotate_array(arr, k ):
    count = 0
    n = len(arr)
    cur_index = 0
    cur_val = arr[cur_index]
    while count < n :
        if n % 2 :
            curr_swap_target = (n - k + cur_index - 1) % n
        else:
            curr_swap_target = (n - k + cur_index ) % n


        next_value = arr[curr_swap_target]
        arr[curr_swap_target] = cur_val
        cur_index = curr_swap_target
        cur_val = next_value
        count += 1

if __name__ == "__main__":
    nums = [1,2,3,4,5,6,7]
    k_3 = 3
    rotate_array(nums, k_3)
    print(nums)
    nums_2 = [-1, -100, 3, 99]
    k_2 =2
    rotate_array(nums_2, k_2)
    print(nums_2)