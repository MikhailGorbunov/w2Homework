class Guest:
    
    def __init__(self, name, wallet, age, drunkenness, fav_song):
        self.name = name
        self.wallet = wallet
        self.age = age
        self.drunkenness = drunkenness
        # self.room_name = room_name
        self.fav_song = fav_song
        
    
    def buy_drink(self, drink):
        if self.sufficient_funds(drink):
            self.wallet -= drink.price
            self.drunkenness += drink.alcohol_level
    
    
    def buy_food(self, food):
        if self.sufficient_funds(food):
            self.wallet -= food.price
            self.drunkenness -= food.rejuvination_level
    
    def sufficient_funds(self, item):
        return self.wallet >= item.price

    def buy_entrance_fee(self, entrance_fee):
        if self.sufficient_funds(entrance_fee):
            self.wallet -= entrance_fee.price
    
    def fev_song(self, guest):
        if self.fav_song == guest.fav_song:
            return "Whoo!"
        else:
            return "Next song"