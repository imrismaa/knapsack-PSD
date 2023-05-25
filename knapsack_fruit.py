import numpy as np

# fungsi utk menghitung max calories
def knapsack01 (calories, price, stock, budget):
    n = len(calories)
    dp = np.zeros((n + 1, budget + 1), dtype=int)

    # memilih buah yg akan dibeli agar dapat max calories
    for i in range(1, n + 1):
        for j in range(1, budget + 1):
            if price[i - 1]*stock[i - 1] <= j:
                dp[i][j] = max((calories[i - 1]*stock[i - 1]) + dp[i - 1][j - (price[i - 1]*stock[i - 1])], dp[i - 1][j])
            else:
                dp[i][j] = dp[i - 1][j]

    maxCal = dp[n][budget]

    # mencari index buah yg dipilih
    selectedItems = []
    j = budget
    for i in range(n, 0, -1):
        if dp[i][j] != dp[i - 1][j]:
            selectedItems.append(i - 1)
            j -= price[i - 1]*stock[i - 1]
    return maxCal, selectedItems

# fungsi utk print tiap buah yg dipilih
def printItems (selectedItems) :
    totalPrice = 0
    print("Daftar buah yang dibeli :")
    for i in selectedItems:
        print("-", fruitName[i])
        print("  Harga :", price[i]*stock[i])
        print("  Kalori :", calories[i]*stock[i])
        totalPrice += price[i]*stock[i]
    print("-----------------------------")
    print("Total Harga Buah      :", totalPrice)

# data buah
price = [2360, 2120, 1890, 3770, 2870]
calories = [91, 71, 105, 103, 96]
stock = [3, 3, 5, 10, 5]
fruitName = ["Apel", "Jeruk", "Pisang", "Kiwi", "Mangga"]
budget = 25000

# pemanggilan fungsi knapsack01 dan selectedItems
maxCal, selectedItems = knapsack01(calories, price, stock, budget)
printItems(selectedItems)

print("Total Maksimal Kalori :", maxCal)