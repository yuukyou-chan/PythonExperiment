# 输入一个包含若干整数的列表，输出一个新列表，要求新列表中只包含原列表中的偶数。

lis = list(map(int, input("请输入一个列表(以空格为分隔符)").split()))


def even(lis):
    lis1 = []
    for i in lis:
        if i % 2 == 0:
            lis1.append(i)
    return lis1


print("列表中的偶数为",even(lis))
