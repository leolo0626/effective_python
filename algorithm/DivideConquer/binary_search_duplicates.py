def binary_search(keys, query):
    # write your code here
    def binary_search_algorithm(left, right):
        mid = (left + right) // 2
        if left > right:
            return -1

        if keys[mid] == query and mid == left:
            return mid
        elif keys[mid] == query :
            return binary_search_algorithm(left, mid)
        elif keys[mid] > query:
            return binary_search_algorithm(left, mid - 1)
        else:
            return binary_search_algorithm(mid + 1, right)

    return binary_search_algorithm(0, len(keys) - 1)


if __name__ == '__main__':
    num_keys = int(input())
    input_keys = list(map(int, input().split()))
    assert len(input_keys) == num_keys

    num_queries = int(input())
    input_queries = list(map(int, input().split()))
    assert len(input_queries) == num_queries

    for q in input_queries:
        print(binary_search(input_keys, q), end=' ')
