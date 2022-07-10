# Uses python3
import sys

def find_max_value(values, weights):
    max_index = 0
    cur_max = values[max_index] / weights[max_index]
    for idx, (cur_val, cur_weight) in enumerate(zip(values, weights)):
        val_per_weight = cur_val/cur_weight
        if val_per_weight > cur_max :
            cur_max = val_per_weight
            max_index = idx
    return max_index


def get_optimal_value(capacity, weights, values):
    value = 0
    # write your code here
    while capacity > 0 and len(weights) != 0:
        max_idx = find_max_value(values, weights)
        amount = min(capacity, weights[max_idx])
        value += amount / weights[max_idx] * values[max_idx]
        capacity -= amount
        del weights[max_idx]
        del values[max_idx]
    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))