#ENUMERATE()

lst = ["milk", "egg", "bread"]
print(lst)

for item in lst:
    print(item)

for index in range(len(lst)):
    print(f"{index+1}.{lst[index]}")

#the above operation can be done with enumerate() function

for index, item in enumerate(lst, start=1):
    print(f"{index}.{item}")

#ZIP()

name = ["jane", "amy", "sam", "alex"]
info = [101, 102, 103, 104]


for nm, inf in zip(name, info):
    print(nm,inf)

name = ["jane", "amy", "sam", "alex"]
info = [101, 102, 103]

for nm, inf in zip(name, info):
    print(nm,inf)

phone = dict(zip(name, info))
print(phone)

#if length of iterables differ then paired ones given as output
#if we dont want that then use zip_longest()

from itertools import zip_longest

for nm, inf in zip_longest(name, info, fillvalue=0): #we can add default value for non pair else set as None
    print(nm,inf)

    #ALL() AND ANY()
values = ["sam", "tom", ""]
    
if not all(values):
    print("yes")

if any(values):
    print("value exists")

#COUNT()
from itertools import count
    
counter = count(start=1,step=2)  #default start is 0

    
print(next(counter))
print(next(counter))
print(next(counter))

#CYCLE()

from itertools import cycle

loop = ["EAT", "SLEEP"]
val = 0

for item in cycle(loop):
    print(item)
    
    if val == 5: break
    val+=1

 #REPEAT()

from itertools import repeat

for msg in repeat("be patient", times =3):
    print(msg)

#COMBINATIONS() PERMUTATIONS() COMBINATIONS_WITH_REPLACEMENTS()

from itertools import combinations,permutations,combinations_with_replacement

players = ["jane", "amy", "sam", "alex"]

for group in combinations(players,2):
    print(group)

for group in permutations(players,2):
    print(group)

for group in combinations_with_replacement(players,2):   #allows combination including with itself
    print(group)

#PRODUCT()

from itertools import product
A = ["john[A]", "sam[A]"]
B = ["tina[B]", "kyle[B]"]

for pair in product(A, B):  #we can pass 3 teams like A,B,C as well
    print(pair)

for pair in product(A, repeat=3): #if we want A x A x A we can change to 2,3,4 etc
    print(pair)

#CHAIN()

from itertools import chain

gen = (x for x in range(2,10,2))
lst = [12, 16, 18]

for num in chain(gen, lst):             # takes multiple iterables and links them together
    print(num)

#ISLICE()

from itertools import islice

gen = (x for x in range(2,10,2))


for num in islice(gen, 1, 4):      # mainly to slice generator
    print(num)

#COMPRESS()

from itertools import compress

name = ["jane", "amy", "sam", "alex"]
adult = [True, 0, True, True]           # both true or 1 can work

for adult_name in compress(name, adult):
    print(adult_name)


#FILTER() AND FILTERFALSE()

from itertools import filterfalse

age = [27, 17, 21, 19]

adults = filter(
    lambda age : age >= 18,          # true values of filter taken
    age
)

print([age for age in adults])

minors = filterfalse(
    lambda age : age >= 18,         # false values of filter taken
        age
)
print([age for age in minors])

#ACCUMULATE()

from itertools import accumulate
from operator import add

age = [27, 17, 21, 19]

for acc_age in accumulate(age, add):           # accumulate the operation specified by operator/ defined function
    print(acc_age)

#GROUPBY()

from itertools import groupby

people = [
    {'name' : 'Jake', 'adult': True},
    {'name' : 'Kyle', 'adult': False}
]

adult_select = lambda person : person['adult']
for group in groupby(people, adult_select):
    print("ADULT" if group[0] else "MINOR")