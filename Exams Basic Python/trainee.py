import string

#main_string = string.ascii_letters
first_word = ''
final_string = ''

c_counter = 0
o_counter = 0
n_counter = 0

letter = input()

while letter != "End":
    if 'a' <= letter <= 'z' or 'A' <= letter <= 'Z':
        if letter == 'c' and c_counter == 0:
            c_counter += 1
        elif letter == 'o' and o_counter == 0:
            o_counter += 1
        elif letter == 'n' and n_counter == 0:
            n_counter += 1
        else:
            first_word += letter

    if c_counter == 1 and o_counter == 1 and n_counter == 1:
        final_string = final_string + first_word + ' '
        first_word = ''
        c_counter = 0
        o_counter = 0
        n_counter = 0

    letter = input()


print(final_string)
