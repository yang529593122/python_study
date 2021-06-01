def print_hi():
    # lsit 列表的操作
    # arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # print (arr[9])    # 2
    # print (arr[-10])  # 1
    # print (arr[1:4])  # 切片会得出 起始位置 到 结束位置之前的 元素 （左闭右开）
    # print (arr[0:10:3]) # 【1，4，7，10】
    # print ([1, 2]+[4, 5, 6])    # [1,2,4,5,6]
    # print ([1, 2]*2)    # [1,2,1,2]

    # 用 in 判断 原属是否在列表中 存在返回 true 不存在 返回false
    user = [1, 2, 3, 4]
    # print (1 in user)  # true
    # print (5 in user)  # false

    arr_fn = [1, 2]

    # list常用方法

    # [].append() 将一个元素附加到列表结尾
    # arr_fn.append(3)
    # print (arr_fn)  # [1, 2, 3]

    # [].insert() 将一个元素插入到列表中指定的位置
    # arr_fn.insert(1, 4)
    # print (arr_fn)  # [1, 4, 2]

    # [].extend() 将多个值添加列表末尾
    # extent_arr = [213, 212]
    # arr_fn.extend(extent_arr)
    # print (arr_fn)  #[1, 2, 213, 212]

    # [].copy()  复制列表
    # copy_arr_fn = arr_fn.copy()
    # print (copy_arr_fn)  # [1, 2]
    # print (arr_fn)  # [1, 2]
    # copy_arr_fn[1] = 9
    # print (copy_arr_fn, arr_fn)  # [1, 9] [1, 2]


    # [].count()  计算出指定的元素在列表中出现的次数
    nums = [1, 8, 2, 3, 4, 1]
    # print (nums.count(1))   # 3

    # [].index()  查找制定元素在列表中第一次出现的索引
    # print (nums.index(1))  # 0

    # [].pop()   从列表中删除末尾元素,并返回这一元素
    # print (nums.pop())  # 1

    # [].remove() 删除第一个为指定值的元素
    # print (nums.remove(1))
    # print (nums)
    # [].clear() 清空列表内容
    #  print (nums.clear())
    # [].del()  删除列表中的元素
    # del nums[2]
    # print (nums)
    # [].sort() 对列表进行排序
    nums.sort()
    print (nums)
# 按间距中的绿色按钮以运行脚本。

if __name__ == '__main__':
    print_hi()


