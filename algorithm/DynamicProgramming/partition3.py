# Uses python3
import sys
import itertools

def partition3(A):
    # Give Some Description on the algorithm
    total_weights = sum(A)
    if len(A) < 3:
        return 0
    if total_weights %3 != 0:
        return 0

    partition_sum = total_weights // 3
    weights = [[[0] * (partition_sum + 1) for _ in range(partition_sum + 1)] for _ in range(len(A)+1)]
    weights[0][0][0] = 1
    for i in range(1, len(A)+1) :
        for j in range(0, partition_sum+1) :
            for k in range(0, partition_sum+1):
                weights[i][j][k] = weights[i][j][k] | weights[i-1][j][k]
                if j >= A[i-1] :
                    weights[i][j][k] = weights[i][j][k] | weights[i - 1][j - A[i - 1]][k];
                if (k >= A[i - 1]):
                    weights[i][j][k] = weights[i][j][k] |  weights[i-1][j][k-A[i-1]];

    return weights[len(A)][partition_sum][partition_sum]

if __name__ == '__main__':
    # input = sys.stdin.read()
    # n, *A = list(map(int, input.split()))
    A = [6, 1, 6, 1, 6, 4] #Tricky Test Case
    print(partition3(A))

