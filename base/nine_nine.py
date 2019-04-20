rows = ['X', 1, 2, 3, 4, 5, 6, 7, 8, 9]
cols = ['X', 1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in rows:
    for j in cols:
        if i == 'X':
            print(j, '  ', end='')
        elif j == 'X':
            print(i, '  ', end='')
        else:
            print(i * j, '  ', end='')
    print()

print('\n\n\n')

for i in range(1, 10):
    for j in range(1, i + 1):
        if j > i:
            break
        print('{} * {} = {}  '.format(j, i, i * j), end='')

    print()
