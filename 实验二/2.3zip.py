# 输入两个分别包含若干整数的列表lsta, lstb，输出一个字典，
# 要求使用列表lsta中的元素为键，列表lstb中的元素为值，
# 并且最终字典中的元素数量取决于lsta和lstb中元素最少的列表的数量。

lsta = list(map(int, input("请输入lsta(以空格为分隔符)").split()))
lstb = list(map(int, input("请输入lstb(以空格为分隔符)").split()))

length = len(lsta) - len(lstb)
if length > 0:
    for i in range(length):
        lsta.pop()

elif length < 0:
    for i in range(abs(length)):
        lstb.pop()

# zip = dict(zip(lsta, lstb))

# 方法二：
# zip = dict.fromkeys(lsta)
# i = 0
# for key in zip:
#     zip[key] = lstb[i]
#     i = i+1

print(zip)

dic = {}
dic.values()
