def money_change_recursive(money, coins):
    if money == 0 :
        return 0

    min_num_of_coins = float('inf')

    for coin in coins :
        if money >= coin :
            number_of_coin = money_change_recursive(money-coin, coins)
            if number_of_coin + 1 < min_num_of_coins :
                min_num_of_coins = number_of_coin + 1

    return min_num_of_coins


if __name__ == '__main__' :
    print(money_change_recursive(7, [1, 5, 6]))