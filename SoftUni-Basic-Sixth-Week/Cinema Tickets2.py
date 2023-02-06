count_students = 0
count_standard = 0
count_kid = 0
count_ticket_movies = 0

end_program = 'False'
type_ticket = ''
total_tickets = 0

movies_name = input()
while movies_name != 'Finish':

    count_ticket_movies = 0
    free_space = int(input())
    for spaces in range(free_space):
        type_ticket = input()
        if type_ticket == 'student':
            count_students += 1
        elif type_ticket == 'standard':
            count_standard += 1
        elif type_ticket == 'kid':
            count_kid += 1
        elif type_ticket == 'End':
            break
        count_ticket_movies += 1

    total_tickets = count_standard + count_kid + count_students
    print(f"{movies_name} - {(count_ticket_movies / free_space) * 100:.2f}% full.")

    movies_name = input()

print(f"Total tickets: {total_tickets}")
print(f"{(count_students / total_tickets) * 100:.2f}% student tickets.")
print(f"{(count_standard / total_tickets) * 100:.2f}% standard tickets.")
print(f"{(count_kid / total_tickets) * 100:.2f}% kids tickets.")


