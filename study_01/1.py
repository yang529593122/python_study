def print_hi():
    # name = input('姓名：')
    # age = int(input('年龄：'))
    # print('你的姓名是%s,年龄是%d' %(name,age))


    # 变量的基本类型
    # int  整形  变量名 = 数字 （数字不带小数点）
    # float 浮点型 变量名 =  数字 （数字带小数点）
    # str 字符串   变量名 =  "字符串"
    # list 列表   列表名 = [ 元素1，元素2，... ]
    # tuple 元组  远组名 = （元素1，元素2，...）
    # set  集合   集合名 = {  元素1，元素2，... }
    # bool 布尔   true （真） False （假）

    age = 2
    print(type(age))
    a = 1.222
    print(type(a))
    b="123"
    print(type(b))
    c=[1,2,3]
    print(type(c))
    d=(1,2,3)
    print(type(d))
    e={ 1,1}
    print(type(e))
    f= True
    print(type(f))
# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    print_hi()


