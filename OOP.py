class Laptop:
    size = 5                            #this is a class variable shared by all objects
    def __init__(self, brand, ram):
        self.b = brand                  #these are instance variables, different obj will have different
        self.r = ram
        val = 0                         #this is a local variable accessible within details method
       
    def details(self):
         print(f"{self.b}, {self.r}")
        
    

l1 = Laptop("abc","1")
l2 = Laptop("def","2")

l1.details()
l2.details()

print(l1.r)
print(l2.r)
print(l1.size)
print(l2.size)


Laptop.size = 10        #class variable changed through class 
print(l1.size)
print(l2.size)

l2.size = 8             #if we mofidy class variable through object  
                        #it creates an instance variable size for l1