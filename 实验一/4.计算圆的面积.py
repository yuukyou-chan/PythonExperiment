# 4、输入圆的半径，输出圆面积（只保留整数）和半径的内存地址。

def area(r):
    return 3.14 * r ** 2


r = float(input("请输入圆的半径"))
s = area(r)
print("r为 %s，的圆的面积是 %s，r的内存地址为 %s"%(r, s, id(r)))

