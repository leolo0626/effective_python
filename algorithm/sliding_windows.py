#first solution
def best_total_price(prices, k):
    max_total = 0
    for i in range(len(prices)-k+1):
        total = sum(prices[i:i+k])
        max_total = max(max_total, total)
    return max_total
#second solution
def best_total_price_2(prices, k):
    if len(prices) < k:
        return 0
    total = sum(prices[:k])
    maxtotal = total

    for i in range(len(prices)-k):
        total -= prices[i]
        total += prices[i+k]
        maxtotal = max(maxtotal, total)
    return maxtotal

if __name__ == "__main__" :
    prices = [1, 2, 3,4, 5, 6, 7, 8]
    print(best_total_price(prices, 2))
    print(best_total_price_2(prices, 2))