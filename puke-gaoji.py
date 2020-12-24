import collections
import random
card = collections.namedtuple('card', ['rank', 'suit'])#快速建立一个只有少数属性没有方法的类


class FrenchDeck:
    ranks = [str(x) for x in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split( ) #这里使用了三种方法去生成list列表
    # 使用split可以按需求分割任意的字符串，如按空格分割或者其他字符分割

    def __init__(self):  #初始化一副扑克
        self._cards = [card(rank, suit) for rank in self.ranks for suit in self.suits]

    def __len__(self):   #让扑克类支持len求扑克张数
        return len(self._cards)

    def __getitem__(self, position):   #让扑克类支持迭代与切片操作
        return self._cards[position]

suit_values = dict(spades = 3,hearts = 2,diamonds = 1,clubs =0)

def spades_high(card):
    rank_values = FrenchDeck.ranks.index(card.rank)*len(card.suit) + suit_values[card.suit]
    return rank_values

if __name__ == '__main__':
    deck = FrenchDeck()
    print(len(deck))#支持len方法求扑克张数
    print(deck[1])  #支持通过序列访问 也自动支持切片操作
    print(deck[1:3])
    card1 = random.choice(deck) #随机取出一张扑克
    print(card1)
    for i in deck:  #打印所有扑克，形成的deck实例是支持迭代的
        print(i)
    for i in reversed(deck):  #支持反向迭代
        print(i)
    print(card('Q', 'hearts') in deck) #支持通过in判断card实例是否在扑克组中
    print(suit_values)
    for card in sorted(deck,key=spades_high,reverse=True):
        print(card)