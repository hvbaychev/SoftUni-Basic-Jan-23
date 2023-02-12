import sys

max_points = -sys.maxsize
max_name = ''

points = 0
value = 0

count_movies = 0

while True:
    command = input()
    if command == 'STOP':
        break
    count_movies += 1
    if count_movies == 7:
        break
    for letter in command:
        len_of_movie = int(len(command))
        points += ord(letter)
        value = ord(letter)
        if letter.isupper():
            points = points - len_of_movie
        elif letter.islower():
            points = points - (len_of_movie * 2)
        else:
            points = points

        if points >= max_points:
            max_points = points
            max_name = command

    points = 0

if count_movies == 7:
    print(f"The limit is reached.")
    print(f"The best movie for you is {max_name} with {max_points} ASCII sum.")
else:
    print(f"The best movie for you is {max_name} with {max_points} ASCII sum.")