desire_jump = int(input())

current_jump = 0
starting_jump = desire_jump - 30
jump_counter = 0
jump_fail_counter = 0
high_jump = False

jump = int(input())
while True:
    jump_counter += 1
    if jump > desire_jump:
        high_jump = True
        break

    if jump <= starting_jump:
        jump_fail_counter += 1
        if jump_fail_counter == 3:
            print(f"Tihomir failed at {starting_jump}cm after {jump_counter} jumps.")
            break

    if jump > starting_jump:
        starting_jump += 5
        jump_fail_counter = 0

    jump = int(input())

if high_jump:
    print(f"Tihomir succeeded, he jumped over {desire_jump}cm after {jump_counter} jumps.")