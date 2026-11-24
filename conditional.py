#IF

num = 7

if num % 2 == 0:
    print("even")

#ELSE

if num % 2 == 0:
    print("even")

else:
    print("odd")

#NESTED IF

num = 100
if num % 2 == 0:
    if num > 50:
        print("Good job")
    else:
        print("Better luck next time")
else:
    print("Better luck next time")

#ELSE IF

if num == 50:
    print("avg")
elif num > 50:
    print("good")
else:
    print("poor")

#MATCH CASE

match input("How are you doing ?"):
    case "😁":
        print("You look happy")
    case "😒":
        print("You look tired")
    case "😭":
        print("You look sad")
    case _:
        print("I didnt catch that")
