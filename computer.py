class Computer:

    # What attributes will it need?
    description: str
    processor_type: str
    hard_drive_capacity: int
    memory: int
    operating_system: str
    year_made: int
    price: int

    # How will you set up your constructor?

    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self, dscpt:str, pt:str, hdc:int, mmy:int, ops: str, ym:int, prc: int) -> None:
        self.description = dscpt
        self.processor_type = pt
        self.hard_drive_capacity = hdc
        self.memory = mmy
        self.operating_system = ops
        self.year_made = ym
        self.price = prc


    # What methods will you need?
    def info(self):
        """ Function prints out details about the computer object"""
        print(self.description + "," + self.processor_type + "," + str(self.hard_drive_capacity) + "," + 
              str(self.memory) + "," + self.operating_system + "," + str(self.year_made) + "," + str(self.price))
        
      


def main():
    computer = Computer("Mac Pro (Late 2013)",
        "3.5 GHc 6-Core Intel Xeon E5",
        1024, 64,
        "macOS Big Sur", 2013, 1500)
    computer.info()
    
if __name__ == "__main__": main()
    
