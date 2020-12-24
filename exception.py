try:
    a = int(input("请输入一个整数:"))
except Exception as e:
    print("类型错误！")
else:
    print("bingo!")
finally:
    print("hello")