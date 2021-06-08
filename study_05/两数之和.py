
def twoSum( List, target):
    # 创建一个字典
    hashtable = dict()
    for i, num in enumerate(List):
        # 判断 是否存在
        if target - num in hashtable:
            return [hashtable[target - num], i]
        hashtable[List[i]] = i
        print(hashtable)

    return []


print(twoSum([2, 7, 11, 15], 9))
print(twoSum([3, 2, 4], 6))