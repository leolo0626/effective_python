# write a fybction list of integer single integer
# objective pair of number and sum up to
# [ 2, 6, 10, 9] # 8 #[0,1]

def find_sum_of_two_integer(list_of_integer , target) :

    int_map = {}
    # key : num2  value : index
    for idx, num1 in enumerate(list_of_integer) :
        num2 = target - num1
        if num2 in int_map :
            return [int_map[num2], idx]
        else :
            int_map[num1] = idx

    return [-1, -1]

if __name__ == "__main__" :
    orignal_list = [2, 3, 11, 5, 6, 10]
    target_a = 16
    print(find_sum_of_two_integer(orignal_list, target_a))

