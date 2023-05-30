import numpy as np

def knapsack01(prices, calories, stocks, budget):
    n = len(prices)
    dp = np.zeros((n + 1, budget + 1), dtype=int)

    for i in range(1, n + 1):
        for j in range(1, budget + 1):
            if prices[i - 1] <= j:
                maxCal = 0
                for k in range(stocks[i - 1] + 1):
                    if prices[i - 1] * k <= j:
                        maxCal = max(maxCal, calories[i - 1] * k + dp[i - 1][j - prices[i - 1] * k])
                dp[i][j] = maxCal
            else:
                dp[i][j] = dp[i - 1][j]

    maxCal = dp[n][budget]
    return maxCal

prices = [2360, 2120, 1890, 3770, 2870]
calories = [91, 71, 105, 103, 96]
stocks = [3, 3, 5, 10, 5]
budget = 25000

maxCal = knapsack01(prices, calories, stocks, budget)

print("Kalori maksimal :", maxCal)
