bottle_of_cream = float(input())
spended_cream = 0

while True:
    if spended_cream <= 500:
        cream = float(input())
        spended_cream += cream
        print(f"Used cream: {spended_cream}")
    if spended_cream >= 500:
        print(f"Bottle of cream is finished")
        break