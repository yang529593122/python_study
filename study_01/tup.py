def print_hi():
    arr = (1, 2, 3, 4, 5)
    # 删除元组
    # del arr
    # 如果元组中包含列表 其中列表中的值是可以修改操作的
    new_arr = (1, 2, [1, 2])
    new_arr[2][1] = 9
    print (new_arr)
    # 元组 可以和 列表相互转换
    a = [1, 2, 3]
    # 使用tuple() 函数 把列表转换为元组
    b = tuple(a)
    print (b)
    # 使用list()函数 把元组转换为列表
    c = list(b)
    print (c)

print_hi ()


