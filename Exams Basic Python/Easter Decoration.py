customers = int(input())

basket = 1.50
wreath = 3.80
chocolate_bunny = 7

all_buyer_sum = 0
total_sum = 0
average = 0

count_purchase = 0

for buyer in range(customers):
    while True:
        purchase = input()
        if purchase == 'Finish':
            if count_purchase % 2 == 0:
                total_sum = total_sum * 0.80
                print(f"You purchased {count_purchase} items for {total_sum:.2f} leva.")
                break
            else:
                print(f"You purchased {count_purchase} items for {total_sum:.2f} leva.")
                break

        if purchase == 'basket':
            count_purchase += 1
            total_sum += basket
        elif purchase == 'wreath':
            count_purchase += 1
            total_sum += wreath
        elif purchase == 'chocolate bunny':
            count_purchase += 1
            total_sum += chocolate_bunny

    all_buyer_sum += total_sum
    total_sum = 0
    count_purchase = 0


average = all_buyer_sum / customers
print(f"Average bill per client is: {average:.2f} leva.")










