def maximumWealth( accounts):
    res = [0] * len(accounts)
    for i in range(len(accounts)):
        res[i] = sum(accounts[i])
    return max(res)


print(maximumWealth([[1, 3], [2, 4], [5, 6, 7]]))

