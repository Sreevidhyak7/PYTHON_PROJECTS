class computer:
    
    brand = "Intel"
    money = 100
    
    def __init__(self, cpu, ram):
        self.cpu = cpu
        self.ram = ram

    def config(self):
        print(f"CPU : {self.cpu} RAM : {self.ram}")

    @classmethod
    def info(cls):
        return cls.brand

    @staticmethod
    def gb_to_bytes(gb):
        return gb * (1024 ** 3)

    def rate(self):
        #return self.__class__.money + 100      git
        return computer.money + 100             # another way to work with class variables 
                                                # but in this case we need an instance to use this 


comp1 = computer("i5", "16GB")
comp2 = computer("i9", "96GB")

comp1.config()
comp2.config()

print(computer.info())
print(comp1.info())
print(comp2.info())


print(computer.gb_to_bytes(16))

print(comp2.rate())