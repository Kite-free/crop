#趣味问题2：生兔子 Fibonacci数列
a1 = 1
b1 = 0
c1 = 0
for i in range(29):
    a2 = c1 + b1
    b2 = a1
    c2 = b1 + c1
    a1 = a2
    b1 = b2
    c1 = c2
    print('小兔子:', a1, '  中兔子:', b1, '  大兔子:', c1, '  总数为:', a1 + b1 + c1)