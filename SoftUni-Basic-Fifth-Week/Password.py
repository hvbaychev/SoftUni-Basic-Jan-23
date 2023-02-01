username = input()
password = input()

command = input()

while command != password:
    command = input()
print(f'Welcome {username}!')