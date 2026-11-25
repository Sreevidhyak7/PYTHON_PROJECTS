# single inheritance is easy one parent, one child 

# Hierarchical is also easy. One parent but many child

# Multilevel - looks at the immediate parent class, if not then the next level grandparent and so on

# MULTIPLE - many parents one child Precedence is from left to right

class A:
    def __init__(self):
        print("Inside A")


class B(A):
    def __init__(self):
        print("Inside B")


class C(A):
    def __init__(self):
        print("Inside C")


class D(B,C):
    pass


D1 = D()            # First looks in B class if not then C if still no then parent of B then parent of C