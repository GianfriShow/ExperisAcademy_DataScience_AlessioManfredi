class Chocolate:
    all_info = {}
    def __init__(self, type, cocoa_percentage, daily_max = 100):
        self.type = type
        self.cocoa_percentage = cocoa_percentage
        self.daily_max = daily_max
        Chocolate.all_info[self.type] = {"cocoa_percentage": self.cocoa_percentage, "daily_max": self.daily_max, "available": self.daily_max, "sales": {'cakes':0,'bars':0,'hot_chocolates':0}}
        self.info = Chocolate.all_info[self.type]
    def produce(self):
        print(f'The chocolate type is "{self.cocoa_percentage}" and the cocoa percentage is {self.cocoa_percentage}%')