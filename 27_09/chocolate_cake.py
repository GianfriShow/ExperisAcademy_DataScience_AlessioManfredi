from chocolate import Chocolate

class ChocolateCake(Chocolate):
    def __init__(self, type, shape, filling):
        self.shape = shape
        self.filling = filling
        self.type = type
        self.cost = 40
    def produce(self):
        if Chocolate.all_info[self.type]['available'] >= self.cost:
            Chocolate.all_info[self.type]['available'] -= self.cost
            Chocolate.all_info[self.type]['sales']['cakes'] += 1
        else:
            print(f'Insufficient {self.type} chocolate: {Chocolate.all_info[self.type]['available']} units left and {self.cost} required.')
            choice = int(input('Would you like to print a summary of sales and refill (choose number)?\n    1) No\n    2) Yes\n'))
            if choice:
                print(Chocolate.all_info[self.type]['sales'])
                Chocolate.all_info[self.type]['sales'] = {key: 0 for key in Chocolate.all_info[self.type]['sales']}
                Chocolate.all_info[self.type]['available'] = Chocolate.all_info[self.type]['daily_max']
            else:
                pass