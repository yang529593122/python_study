def replaceElements(list):
    max_val = -1
    res = [0]*len(list)
    for i in range(len(list)-1, -1, -1):
        res[i] = max_val
        if list[i] > max_val:
            max_val = list[i]
        else:
            max_val
    return res


list = [17, 18, 5, 4, 6, 1]

print(replaceElements(list))