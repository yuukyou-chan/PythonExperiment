# 输入任意大的自然数，输出各位数字之和

def sum():
    num = input("请输入一个数字")
    s = 0
    for i in num:
        s += int(i)
    return num, s


sum = sum()
print("你输入的数字是 %s , 它的各位数和是 %d" % (sum[0], sum[1]))
