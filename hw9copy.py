'''Zhiwei Liu HW9'''

class Card:
    def __init__(self,rank,suit):
        self.rank=int(rank)
        self.suit=suit
    def get_rank(self):
        return self.rank
    def get_suit(self):
        return self.suit
    def bj_value(self):
        if(self.rank >=11):
            return 10
        else:
            return self.rank
    def __repr__(self):
        num2words = {1: 'Ace', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 
             6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten',
            11: 'Jack', 12: 'Queen', 13: 'King'}
        if (self.suit=="d"):
           return f'{num2words[self.rank]} of Diamonds'
        elif(self.suit=="c"):
           return f'{num2words[self.rank]} of Clubs'
        elif(self.suit=="h"):
           return f'{num2words[self.rank]} of Hearts'
        elif(self.suit=="s"):
           return f'{num2words[self.rank]} of Spades'





            


        
