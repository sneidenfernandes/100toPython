import random


class Buyer:
    def __init__(self,budget):
        self.budget = budget

    def purchase(self,price):
        if self.budget >= price:
            self.budget -= price
            return True
        else:
            return False
        
class Seller:

    def __init__(self, inventory, cost_price):
        self.inventory = inventory
        self.cost_price = cost_price


    def sell(self):
        if self.inventory > 0:
            self.inventory -= 1
            return self.cost_price + random.uniform(5.0, 2.0) #Add a profit margin
        else:
            return None
        

class main():

    buyers = [Buyer(random.randint(50,200)) for _ in range(10)]
    sellers = [Seller(random.randint(1,10), random.uniform(5.0,15.0)) for _ in range(10)]

    for day in range(30):

        print(f'Day {day+1}:')

        for buyer in buyers:
            seller = random.choice(sellers)
            price = seller.sell()

            if price is not None and buyer.purchase(price):

                print(f"Buyer with budget ${buyer.budget} purchased a product for ${price}")
            else:
                print("Buyer couldn't make a purchase")
        
    print("\nEnd of Simulation:")

    for buyer in buyers:

        print(f"Buyer with final budget ${buyer.budget}")


if __name__ == '__main__':
    main()







        