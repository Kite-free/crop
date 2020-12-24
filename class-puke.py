import random
class card:
    def __init__(self,color,value,real_value):
        self.color = color
        self.value = value
        self.real_value = real_value

    def __str__(self):
        return '%s %s %d'%(self.color,self.value,self.real_value)

class cards():
    def __init__(self):
        self.cards = []
        self.threecards = []

    def __getitem__(self, item):
        return self.cards[item]

    def __str__(self):
        return '%s'%self.cards

    def init_cards(self):
        values = [str(x) for x in range(2,11)] + ['J','Q','K','A']
        for i in "♥♠♦♣":
            k = 1
            for j in values:
                c = card(i,j,k)
                k +=1
                self.cards.append(c)

    def fa_pai(self):
        for i in range(3):
            index = random.randint(0,len(self.cards)-1)#randint范围是a<=x<=b
            self.threecards.append(self.cards.pop(index))

    def showallcards(self):
       for i in self.cards:
           print(i)

    def showthreecards(self):
        for i in self.threecards:
            print(i)

    def compare_pai(self):
        a = self.threecards[0]
        b = self.threecards[1]
        c = self.threecards[2]
        if a.color == b.color == c.color:
            print('同花顺')
        else:
            print('普通牌')

def value(card):
    return card.real_value


def main():
    cards1 = cards()
    cards1.init_cards()
    # cards1.showallcards()
    # cards1.fa_pai()
    # cards1.showthreecards()
    # cards1.compare_pai()
    for card in  sorted(cards1,key=value,reverse=True):  #根据您扑克牌组中的单张扑克的real-value排序
        print(card)



if __name__ == '__main__':
    main()