country = input()
device = input()

total_sum = 0
difficulty = 0
performance = 0

max_evaluation = 20

if country == 'Russia':
    if device == 'ribbon':
        difficulty = 9.100
        performance = 9.400
    elif device == 'hoop':
        difficulty = 9.300
        performance = 9.800
    elif device == 'rope':
        difficulty = 9.600
        performance = 9.000

if country == 'Bulgaria':
    if device == 'ribbon':
        difficulty = 9.600
        performance = 9.400
    elif device == 'hoop':
        difficulty = 9.550
        performance = 9.750
    elif device == 'rope':
        difficulty = 9.500
        performance = 9.400

if country == 'Italy':
    if device == 'ribbon':
        difficulty = 9.200
        performance = 9.500
    elif device == 'hoop':
        difficulty = 9.450
        performance = 9.350
    elif device == 'rope':
        difficulty = 9.700
        performance = 9.150

sum_of_point = difficulty + performance
remain_points = abs(max_evaluation - sum_of_point)

total_sum = (remain_points / max_evaluation) * 100

print(f"The team of {country} get {sum_of_point:.3f} on {device}.")
print(f"{total_sum:0.2f}%")
