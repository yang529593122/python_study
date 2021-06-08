# 不改变原数据
def oneArr(nums):
    out = []
    temp = 0
    for i in range(len(nums)):
        out.append(temp + nums[i])
        temp += nums[i]
    return out


# 改变数据
def yesChange(nums):
    for i in range(len(nums)):
        if i == 0:
            nums[i] = nums[i]
        else:
            nums[i] += nums[i - 1]
    return nums


print(oneArr([1, 2, 3, 4]))
print(yesChange([1, 2, 3, 4]))