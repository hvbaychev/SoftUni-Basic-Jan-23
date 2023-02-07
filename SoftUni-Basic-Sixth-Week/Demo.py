amount_bottles = int(input()) * 750
reloading = 0
dishes = 0
pots = 0
command = None
cycles = 0
ml = 0

while amount_bottles >= 0:
    command = input()

    if command == "End":
        if amount_bottles >= 0:
            print("Detergent was enough!")
            print(f"{dishes} dishes and {pots} pots were washed.")
            print(f"Leftover detergent {amount_bottles} ml.")
            break
        else:
            print(f"Not enough detergent, {abs(amount_bottles)} ml. more necessary!")
            break
    cycles += 1
    if cycles == 3:
        amount_bottles -= int(command) * 15
        pots += int(command)
        cycles = 0
    else:
        amount_bottles -= int(command) * 5
        dishes += int(command)

else:
    print(f"Not enough detergent, {abs(amount_bottles)} ml. more necessary!")