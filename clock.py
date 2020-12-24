import time
import os
class clock(object):
    def __init__(self,hour=0, min=0, second=0):
        self.hour = hour
        self.min = min
        self.second = second


    def show(self):
        time =  '%2d:%2d:%2d'%(self.hour,self.min,self.second)
        return time

    def run(self):
        self.second += 1
        if self.second == 60:
            self.min += 1
            self.second = 0
            if self.min == 60:
                self.hour += 1
                self.min = 0
                if self.hour == 24:
                   self.hour = 0

def main():
    clock1 = clock(23,59,58)
    while True:
        print('时间：' + clock1.show())
        time.sleep(1)
        clock1.run()

if __name__ == '__main__':
    main()