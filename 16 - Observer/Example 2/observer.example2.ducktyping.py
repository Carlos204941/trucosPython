class Bidder:    
    def __init__(self, name):
        self._name = name
    
    def update(self, auction_item):
        print(f"{self._name} notified.New highest bid on {auction_item.name} is {auction_item.price}")

class AuctionItem:
    def __init__(self, name, starting_price):
        self.name = name
        self.price = starting_price
        self._bidders = []
        self._highest_bidder = None
        
    def register_bidder(self, bidder):
        self._bidders.append(bidder)

    def remove_bidder(self, bidder):
        self._bidders.remove(bidder)

    def notify_bidders(self):
        for bidder in self._bidders:
            bidder.update(self)

    def new_bid(self, price, bidder):
        if price > self.price:
            self.price = price
            self._highest_bidder = bidder
            self.notify_bidders()

john = Bidder("John")
jane = Bidder("Jane")

item1 = AuctionItem("Item1", 10)

item1.register_bidder(john)
item1.register_bidder(jane)

item1.new_bid(20, john)
item1.new_bid(30, jane)