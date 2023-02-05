n = int(input())

spaces = ' '
star = '*'
pipe = '|'

for i in range(0, n+1):
    spaces = n-i
    star = i*1
    print(' '*spaces + '*'*star + ' | ' + '*'*star)

