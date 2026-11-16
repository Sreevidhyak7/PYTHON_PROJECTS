def fire(rounds):
    print("Loading ammo")
    print("...Firing...")

    if rounds <= 0:
        print("No ammo to fire")
    while rounds > 0:
        print("     🔥")
        rounds -=1
    print("Reload to fire")
        


ammo = int(input("How many ammos do you have?"))
fire(ammo)