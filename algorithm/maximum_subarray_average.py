# brute force
# O(n^2)
def max_avg_sub_array(nums, k):
    if len(nums) <= k :
        return sum(nums)/k
    max_total = float('-inf')
    for i in range(len(nums)-k+1):
        max_total = max(sum(nums[i: i+k]), max_total)
    return max_total / k

# Sliding window O(n)
def max_avg_sub_array_2(nums, k):
    if len(nums) <= k:
        return sum(nums)/k
    max_total = sum(nums[0: k])
    total = max_total
    for i in range(k, len(nums)):
        total += nums[i] - nums[i-k]
        max_total = max(max_total, total)
    return max_total / k




if __name__ == "__main__":
    nums = [0, 1, 1, 3, 3]
    k = 4
    print(max_avg_sub_array_2(nums, k))