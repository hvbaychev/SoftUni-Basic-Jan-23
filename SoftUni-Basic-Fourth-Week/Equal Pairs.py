n = int(input())


first_pair_sum = 0
second_pair_sum = 0
max_diff_pair = 0

for i in range(2 * n):
    curr = int(input())
    first_pair_sum += curr

    if i % 2 != 0 and i >= 3:
        max_diff_pair = max(max_diff_pair, abs(first_pair_sum - second_pair_sum))
        second_pair_sum = first_pair_sum
        first_pair_sum = 0

    elif i % 2 != 0 and i >= 1:
        second_pair_sum = first_pair_sum
        first_pair_sum = 0

if max_diff_pair != 0:
    print("No, maxdiff={0}".format(max_diff_pair))
else:
    print("Yes, value={0}".format(second_pair_sum))