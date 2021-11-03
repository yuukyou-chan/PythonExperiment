# 输入6个学生的姓名和年龄构成的字典，读出其键和值，并分别保存输出到两个列表中。

dic = {}
status = True

while status:
    name = input("请输入姓名")
    age = input("请输入年龄")
    dic[name] = age
    print("你输入的数据为", dic)
    s = input("**********是否继续输入？(y/n)**********")
    if s != "y":
        status = False


name = list(dic.keys())
age = list(dic.values())
print("字典的键为",name)
print("字典的值为",age)

