# Uses python3
import sys

def get_change(money):
    # coins for change
    coins = [1, 3, 4]
    # initialise minimum number of coin
    min_number_of_coins = [0] * (money+1)
    for m in range(1, money+1):
        min_number_of_coins[m] = float('inf')
        for coin in coins :
            if m >= coin:
                num_of_coins = min_number_of_coins[m-coin] + 1
                if  num_of_coins < min_number_of_coins[m] :
                    min_number_of_coins[m] = num_of_coins

    return min_number_of_coins[money]

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))