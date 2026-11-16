def fire(rounds):
    print("Loading ammo")
    print("...Firing...")

    while rounds:
        print("     🔥")
        rounds -=1

ammo = int(input("How many ammos do you have?"))
fire(ammo)