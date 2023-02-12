import math
import sys

powerful_word = -sys.maxsize
total_sum = 0
current_score = 0
winner_name = ''

command = input()
while command != 'End of words':
    len_of_the_name = len(command)
    x = command[0]
    for letter in command:
        total_sum += ord(letter)
    if (x == 'a' or x == 'e' or x == 'i' or
            x == 'o' or x == 'u' or x == 'A' or
            x == 'E' or x == 'I' or x == 'O' or
            x == 'U' or x == 'y' or x == 'Y'):
        total_sum = total_sum * len_of_the_name
    else:
        total_sum = total_sum / len_of_the_name

    if total_sum >= powerful_word:
        powerful_word = total_sum
        winner_name = command

    total_sum = 0
    command = input()

print(f"The most powerful word is {winner_name} - {math.floor(powerful_word)}")







