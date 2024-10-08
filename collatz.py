#collatz conjecture


flag = 0
n = int(input('whats n? '))
if n == 1:
    print(True)
else:
    while n != 1:
        if n % 2 == 0:
            n = n/2
            flag += 1
            continue
        elif n % 2 != 0:
            n = (3 * n) + 1
            flag += 1
            continue

print(flag)

# testing new git features