size = int(input())
for i in range(1, size + 1):
    print(' ' * (size - i) + '*' * (2 * i - 1))

for i in range(size - 2, 0, -1):
    print(' ' * (size - i - 1) + '*' * (2 * i + 1))
