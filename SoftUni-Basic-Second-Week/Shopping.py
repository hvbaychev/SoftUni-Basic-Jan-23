budget = float(input())

gpu_want = int(input())
cpu_want = int(input())
ram_want = int(input())

price_gpu = gpu_want * 250


price_cpu = price_gpu * 0.35
total_price_cpu = price_cpu * cpu_want


price_ram = price_gpu * 0.10
total_price_ram = ram_want * price_ram


total_sum = price_gpu + total_price_ram + total_price_cpu

if gpu_want > cpu_want:
    total_sum = total_sum * 0.85

if total_sum <= budget:
    remain_budget = abs(total_sum - budget)
    print(f'You have {remain_budget:.2f} leva left!')
else:
    remain_budget = abs(budget - total_sum)
    print(f'Not enough money! You need {remain_budget:.2f} leva more!')



