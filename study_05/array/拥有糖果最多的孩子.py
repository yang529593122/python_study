def kidsWithCandies(candies, extraCandies):
    maxi = max(candies)
    judge = []
    for i in candies:
        judge.append(i + extraCandies >= maxi)
    return judge


candies = [2,3,5,1,3]
extraCandies = 3
print(kidsWithCandies(candies, extraCandies))


def shuffle(nums, n):
    list = []
    for i in range(n):
        list.append(nums[i])
        list.append(nums[i + n])
    return list


nums = [1, 1, 2, 2]
n = 2

print(shuffle(nums, n))