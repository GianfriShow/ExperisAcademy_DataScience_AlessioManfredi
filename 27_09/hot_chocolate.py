from chocolate import Chocolate

class HotChocolate(Chocolate):
    def __init__(self, type, temperature, density):
        self.temperature = temperature
        self.density = density
        self.type = type
        self.cost = 5*density/2
    def produce(self):
        if Chocolate.all_info[self.type]['available'] >= self.cost:
            Chocolate.all_info[self.type]['available'] -= self.cost
            Chocolate.all_info[self.type]['sales']['hot_chocolates'] += 1
        else:
            print(f'Insufficient {self.type} chocolate: {Chocolate.all_info[self.type]['available']} units left and {self.cost} required.')
            choice = int(input('Would you like to print a summary of sales and refill (choose number)?\n    1) No\n    2) Yes\n'))
            if choice:
                print(Chocolate.all_info[self.type]['sales'])
                Chocolate.all_info[self.type]['sales'] = {key: 0 for key in Chocolate.all_info[self.type]['sales']}
                Chocolate.all_info[self.type]['available'] = Chocolate.all_info[self.type]['daily_max']
            else:
                pass