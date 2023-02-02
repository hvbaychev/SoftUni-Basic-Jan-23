love_book = input()
count = 0
no_more = 'False'
find = 'False'

while True:
    new_book = input()
    if new_book == 'No More Books':
        no_more = 'True'
        break

    if new_book == love_book:
        find = 'True'
        break
    count += 1
if no_more == 'True':
    print('The book you search is not here!')
    print(f'You checked {count:.0f} books.')
else:
    print(f'You checked {count:.0f} books and found it.')
