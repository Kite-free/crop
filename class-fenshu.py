#构造一个能够表示分数的类，实现分数的加减乘除、默认化为最简分数等操作
class Fraction:
    def __init__(self, top, button):
        self.top = top
        self.button = button
        if type(self.top) != int or type(self.button) != int:
            raise SyntaxError('please input int number!')
        if self.button < 0:
            self.button = -self.button
            self.top = -self.top

    def __str__(self):#print输出
        return(str(self.top//gcd(self.top, self.button)) + '/' + str(self.button//gcd(self.top, self.button)))

    def __add__(self, otherfraction): #加法
        newtop = self.top*otherfraction.button+otherfraction.top*self.button
        newbutton = self.button*otherfraction.button
        return Fraction(newtop, newbutton)

    def __sub__(self, otherfraction): #减法
        newtop = self.top * otherfraction.button - otherfraction.top * self.button
        newbutton = self.button * otherfraction.button
        return Fraction(newtop,newbutton)

    def __mul__(self,otherfraction): #乘法
        newtop = self.top*otherfraction.top
        newbutton = self.button*otherfraction.button
        return Fraction(newtop, newbutton)

    def __truediv__(self, otherfraction): #除法
        newtop = self.top*otherfraction.button
        newbutton = self.button*otherfraction.top
        return  Fraction(newtop,newbutton)

    def __eq__(self,other):#判断两分数是否相等
        return self.top*other.button == self.button*other.top

    def gettop(self):#获得分子
        return self.top

    def getbutton(self):#获得分母
        return self.button


def gcd(m, n): #获取两个数的最大公约数
    while m % n != 0:
        oldm = m
        oldn = n
        m = oldn
        n = oldm%oldn
    return n

def main():
    myfraction1 = Fraction(3, -12)
    myfraction2 = Fraction(4, 12)
    print(myfraction1 == myfraction2) #判断两分数是否相等
    print(myfraction1+myfraction2)
    print(myfraction1-myfraction2)
    print(myfraction1*myfraction2)
    print(myfraction1/myfraction2)
    print(myfraction1.gettop())
    print(myfraction1.getbutton())


if __name__ == '__main__':
    main()