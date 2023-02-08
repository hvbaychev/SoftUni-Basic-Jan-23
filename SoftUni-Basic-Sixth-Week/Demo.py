import string

main_string = string.ascii_letters
first_word = ''
final_string = ''

c_counter = 0
o_counter = 0
n_counter = 0


letter = input()

while letter != "End":

    if letter == 'C' or letter == 'c' and c_counter == 0:
        c_counter += 1
    elif letter == 'O' or letter == 'o' and o_counter == 0:
        o_counter += 1
    elif letter == 'N' or letter == 'n' and n_counter == 0:
        n_counter += 1
    else:
        first_word += letter

    if c_counter > 1:
        first_word += letter
    elif o_counter > 1:
        first_word += letter
    elif n_counter > 1:
        first_word += letter

    if c_counter == 1 and o_counter == 1 and n_counter == 1:
        first_word += ' '
        final_string += first_word
        first_word = ''
        c_counter = 0
        o_counter = 0
        n_counter = 0
        letter_count = 0

    letter = input()

print(final_string)