#buy and sell
# price = [7, 1, 5, 3, 6, 4]
# target = max profit  # expected 5

def find_max_profit(list_of_stock_price) :
    n = len(list_of_stock_price)
    max_profit = 0
    for i in range(n) :
        buy_price = list_of_stock_price[i]
        for j in range(i+1, n) :
            sell_price = list_of_stock_price[j]
            profit = sell_price - buy_price
            max_profit = max(profit, max_profit)

    return max_profit


if __name__ == "__main__" :
    list_of_price = [7, 6, 4, 3, 1]
    print(find_max_profit([7, 6, 4, 3, 1]))