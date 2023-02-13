order_chicken = int(input())
order_fish = int(input())
order_Veg = int(input())

chicken_menu = 10.35 * order_chicken
fish_menu = 12.40 * order_fish
veg_menu = 8.15 * order_Veg
delivery = 2.50

total_sum = chicken_menu + fish_menu + veg_menu
desert = total_sum * 0.20
total_sum = total_sum + desert + delivery
print(total_sum)