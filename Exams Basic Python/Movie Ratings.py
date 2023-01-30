import sys

movies_number = int(input())

max_rating = -sys.maxsize
min_rating = sys.maxsize
average = 0
sum_of_average = 0
name_min = ''
name_max = ''


for _ in range(movies_number):
    name_movie = input()
    rating = float(input())

    max_rating = max(rating, max_rating)
    min_rating = min(rating, min_rating)

    if rating == max_rating:
        name_max = name_movie
    elif rating == min_rating:
        name_min = name_movie

    sum_of_average += rating
    average = sum_of_average / movies_number

print(f"{name_max} is with highest rating: {max_rating:.1f}")
print(f"{name_min} is with lowest rating: {min_rating:.1f}")
print(f"Average rating: {average:.1f}")

