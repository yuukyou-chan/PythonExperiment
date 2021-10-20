# 输入一个自然数，输出它的二、八、十六进制表示形式

'''
# 方法一：

def trans() :
    num = int(input("请输入一个自然数"))
    print("你输入的数字是 %s" % num)
    print("它的二进制表示为：%s" % format(num, 'b'))
    print("它的八进制表示为：%o" % num)
    print("它的十六进制表示为：%x" % num)


trans()

方法二： bin(x)、oct(x)、hex(x)
'''


# 方法三

def trans():
    num = int(input("请输入一个自然数"))
    b = format(num, 'b')
    o = format(num, 'o')
    x = format(num, 'x')

    return num, b, o, x


trans = trans()
print("你输入的数字是 %s\n它的二进制表示为：%s\n它的八进制表示为：%s\n它的十六进制表示为：%s" % (trans[0], trans[1], trans[2], trans[3]))
