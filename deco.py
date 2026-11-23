#INNER FUNCTION

def outer():
    print("In outer")

    def inner():
        print("In inner")

    return inner                #its like returning pointer to this function inner


get = outer()                  #the pointer is assigned to get
get()                          #now get() behaves like a function call

#DECORATOR  

def greater_first(func):                #takes the function as argument 
    def wrap(a,b):                       # will have same parameters as the function which needs to be decorated
        if a<b:
            a,b =b,a
        return func(a,b)
    return wrap


@greater_first
def divide(a,b):
    return a/b

result = divide(4,2)
print(result)

#DECORATOR eg2

def fence(func):
    
    def add_fence(val):
        
        print("+"*5)
        func(val)
        print("+"*5)
    
    return add_fence

@fence
def log(val):
    
    print(val)