# Uses python3
import sys

def optimal_sequence(n) :
    min_num_of_operations = [0] * (n+1)


    for i in range(2, n+1):
        min_num_of_operations[i] = min_num_of_operations[i-1] + 1
        if i % 2 == 0 and i // 2 >= 1:
            min_num_of_operations[i] = min(min_num_of_operations[i], min_num_of_operations[i // 2] + 1)

        if i % 3 == 0 and i // 3 >= 1:
            min_num_of_operations[i] = min(min_num_of_operations[i], min_num_of_operations[i // 3] + 1)

    solution = []
    while n > 1:
        solution.append(n)
        if min_num_of_operations[n-1] == min_num_of_operations[n] -1 :
            n = n - 1

        elif n % 2 == 0 and min_num_of_operations[n//2] == min_num_of_operations[n] - 1:
            n = n // 2

        elif n % 3 == 0 and min_num_of_operations[n//3] == min_num_of_operations[n] - 1:
            n = n // 3

    solution.append(1)
    return reversed(solution)

input = sys.stdin.read()
n = int(input)
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')


