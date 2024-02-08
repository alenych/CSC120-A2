from computer import *

#storing the inventory for the store (resale.py)
#updating a computer's price (resale.py)
#updating a computer's OS (comp.py)
#buying a computer (add to inventory) (resale.py)
#selling a computer (remove from inventory) (resale.py)
#refurbishing a computer (resale.py)

class ResaleShop:
    """ Class sells, buys, updates, and refurbishes computers."""
        
    
    # What attributes will it need? 
    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self):
      self.inventory = []
        

    # What methods will you need?
    
    def buy(self, computer: Computer):
        """ Buys a computer and adds it to the store inventory"""
        # 1. call Computer(...) constructor to create a new Computer instance

        # 2. call inventory.append(...) to add the new Computer instance to the iventory
        self.inventory.append(computer)
   

    def sell(self):
        """ If computer is in the store inventory, this method sells the computer and remvoes it from the list, else an error is printed"""
        if computer in self.inventory:
            self.inventory.remove(computer)
        else:
            print("Error, the inventory is empty")

    def refurbishing(self):
        """ Updates a computers pricing depending on year and also updates its macos if it is not the latest os"""
        if computer in self.inventory:
            if(computer.year_made > 2022):
                computer.price = 2000
            elif(computer.year_made < 2022 >2010):
                computer.price = 1000
            else:
                computer.price = 500 
            if computer.operating_system is not "macOS 14 Sonoma":
                computer.operating_system = "macOS 14 Sonoma"
        else:
              print("Sorry shop inventory is empty")
   
    def inventory_print(self):
       """ Prints out the stores inventory"""
       print(self.inventory)

def main():
    computer_1 = Computer("Mac Pro (Late 2013)",
        "3.5 GHc 6-Core Intel Xeon E5",
        1024, 64,
        "macOS Big Sur", 2013, 1500)
    computer_2 = Computer("MacBook Pro (Early 2022)", "3.5 GHc 6-Core Intel Xeon E5", 1024, 64, "macOS 14 Sonoma", 2022, 2000)

    
    self.buy()
    compshop.inventory_print()
    compshop.sell(computer_1)
    compshop.refurbishing
    compshop.inventory_print()

main()
        

