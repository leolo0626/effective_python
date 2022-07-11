# Uses python3
import sys

def optimal_weight(W, w):
    # initialise a dynamic array
    w_count = len(w)
    weights_matrix = [[0] * (W + 1) for _ in range(w_count+1)]
    for j  in range(1, W+1):
        for i in range(1, w_count+1):
            weights_matrix[i][j] = weights_matrix[i-1][j]
            # why i-1 because w does not has 0 in prefix
            if j >= w[i-1]:
                val = weights_matrix[i-1][j-w[i-1]] + w[i-1]
                if weights_matrix[i][j] < val:
                    weights_matrix[i][j] = val
    return weights_matrix[-1][-1]



if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))

