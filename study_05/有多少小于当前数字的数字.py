def smallerNumbersThanCurrent(list):
    n = len(list)
    ans = [0] * n
    for i in range(n):
        for j in range(n):
            if i != j and list[i] > list[j]:
                ans[i] += 1
    return ans


list = [8, 1, 2, 2, 3]
print(smallerNumbersThanCurrent(list))
