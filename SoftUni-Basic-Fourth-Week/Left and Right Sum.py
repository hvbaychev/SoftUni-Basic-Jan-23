n = int(input())

left_sum = 0
right_sum = 0

for num in range(0, n*2):
    current_number = int(input())
    if num < n:
        left_sum = left_sum + current_number
    else:
        right_sum = right_sum + current_number

if left_sum == right_sum:
    print(f'Yes, sum = {left_sum}')
else:
    diff = abs(left_sum - right_sum)
    print(f'No, diff = {diff}')

