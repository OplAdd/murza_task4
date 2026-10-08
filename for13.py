n = int(input())

total = 0.0

for i in range(1, n + 1):
    value = 1 + i / 10
    if i % 2 == 1:
        total += value
    else:
        total -= value

print(total)