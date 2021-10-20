# 计算BMI指数

def BMI():
    h = float(input("请输入身高"))
    w = float(input("请输体重"))
    return w / (h ** 2)


print("你的BMI指数是", BMI())
