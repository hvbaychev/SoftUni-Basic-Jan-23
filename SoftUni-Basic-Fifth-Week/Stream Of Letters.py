count_c = 0
count_o = 0
count_n = 0
word = ''
new_word = ''

command = input()
while command != 'End':
    if 'a' <= command <= 'z' or 'A' <= command <= 'Z':
        if command == 'n' and count_n == 0:
            count_n += 1
        elif command == 'c' and count_c == 0:
            count_c += 1
        elif command == 'o' and count_o == 0:
            count_o += 1
        else:
            word += command

        if count_o == 1 and count_c == 1 and count_n == 1:
            new_word = new_word + word + ' '

            word = ''
            count_n = 0
            count_o = 0
            count_c = 0

    command = input()

print(new_word)
