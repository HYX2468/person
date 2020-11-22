import random 
num=random.randint(1,100)
print(num)
i=1
while i <= 5:
    a=int(input("请输入你猜的数字："))
    
    if a < num:
        print("数字偏小")
        i=i+1
    elif a > num:
        print("数字偏大")
        i=i+1
    elif a == num:
        print("回答正确")
        break
    if i > 5:
        print("游戏结束！")
        break 