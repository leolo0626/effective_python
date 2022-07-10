# Uses python3
'''
Task. The goal in this problem is to find the minimum number of coins needed to change the input value
(an integer) into coins with denominations 1, 5, and 10.
Input Format. The input consists of a single integer 𝑚.
Constraints. 1 ≤ 𝑚 ≤ 103.
Output Format. Output the minimum number of coins with denominations 1, 5, 10 that changes 𝑚.

'''
import sys

def get_change(m):
    #write your code here
    return  m // 10 + (m % 10)//5 + m % 5

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
