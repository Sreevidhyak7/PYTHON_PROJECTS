
lst = [ num for num in range(0,11) ]                    #creates a list 0 to 10
print(lst)

names = ["jane", "amy", "sam", "alex"]
print(names)
NAMES =[ name.capitalize() for name in names ]       
print(NAMES)


def is_even(num):
	return num%2 == 0
l = [num
    for num in range(11)
	if is_even(num)]

print(l)

pair = [f"{x} {y}"
        for x in range(3)
        for y in range(2)]
print(pair)

set_value = {x for x in range(3)	
}

print(set_value)

def is_even(num):
	return num%2 == 0
l_set = {num
    for num in range(11)
	if is_even(num)}
print(l_set)

pair_set = {f"{x} {y}"
        for x in range(3)
        for y in range(2)}
print(pair)

dictionary = { x: x*x
              for x in range(11)	
}
print(dictionary)