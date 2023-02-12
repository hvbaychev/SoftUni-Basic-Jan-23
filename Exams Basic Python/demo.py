movie_counter = 0
winner_movie = 0
winner_name = ''
total_points = 0
while True:
    movie = input()

    if movie == 'STOP':
        print(f"The best movie for you is {winner_name} with {winner_movie} ASCII sum.")
        break

    movie_counter += 1

    if movie_counter == 7:
        print(f"The limit is reached.")
        print(f"The best movie for you is {winner_name} with {winner_movie} ASCII sum.")
        break

    movie_points = 0
    points = 0

    for char in movie:
        ascii_value = ord(char)

        if 'a' <= char <= 'z':
            points = ascii_value - (2 * len(movie))
            movie_points += points
        elif 'A' <= char <= 'Z':
            points = ascii_value - len(movie)
            movie_points += points
        else:
            points = ascii_value
            movie_points += ascii_value

    if movie_points > winner_movie:
        winner_movie = movie_points
        winner_name = movie