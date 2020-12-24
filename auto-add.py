def compute():
    sum1 = 0
    sum2 = 0
    sum3 = 0
    for i in range(9):
        def input1():
            try:
                global a
                a = int(input("小图中所有框选的船总数a: "))
            except ValueError as e:
                print("输入错误，请重新输入：")
                input1()
            return a

        def input2():
            try:
                global b
                b = int(input("小图中误检框错的总数b："))
            except:
                print("输入错误，请重新输入：")
                input2()
            return b

        def input3():
            try:
                global c
                c = int(input("小图中漏检没有框选的总数c："))
            except:
                print("输入错误，请重新输入：")
                input3()
            return c
        a = input1()
        b = input2()
        c = input3()
        sum1 += a
        sum2 += b
        sum3 += c
        print("小图中所有框选的船累加总数a: ", sum1)
        print("小图中误检框错的累加总数b：", sum2)
        print("小图中漏检没有框选的累加总数c：", sum3)
    print("这张图所有框选的船总数a: ", sum1)
    print("这张图误检框错的总数b：", sum2)
    print("这张图漏检没有框选的总数c：", sum3)
    compute()


compute()