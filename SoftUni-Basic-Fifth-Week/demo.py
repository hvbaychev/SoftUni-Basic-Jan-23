checking_input = input()
word = ""
new_word = ""
count_c = 0
count_o = 0
count_n = 0
while checking_input != "End":
    if checking_input >= 'a' and checking_input <= 'z' or checking_input >= 'A' and checking_input <= 'Z':
        if checking_input == 'n' and count_n == 0:
            count_n += 1
        elif checking_input == 'c' and count_c == 0:
            count_c += 1
        elif checking_input == 'o' and count_o == 0:
            count_o += 1
        else:
            word += checking_input

        if count_n == 1 and count_c == 1 and count_o == 1:
            new_word = new_word + word + " "

            word = ""
            count_n = 0
            count_c = 0
            count_o = 0

    checking_input = input()

print(new_word)