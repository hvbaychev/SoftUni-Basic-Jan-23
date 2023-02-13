deposit = float(input())
time = int(input())
percent = float(input())

sum_deposit = deposit * (percent / 100)
tax = sum_deposit / 12
total_sum =  deposit + time * tax

print(total_sum)