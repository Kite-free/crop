class student(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def study(self,course):
        print('%s正在学习%s.' % (self.name,  course))#格式化字符串
    def movie(self):
        if self.age > 18:
            print('%s可以看日本动作电影' % (self.name))
        else:
            print('%s禁止看日本动作电影' % (self.name))


def main():
    stu1 = student('zz', 22)
    stu1.study('python')
    stu1.movie()


if __name__ == '__main__':
    main()
