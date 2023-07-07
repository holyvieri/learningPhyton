x = int(input())
y = int(input())
total = 0

if x > y:
    x, y = y, x

for number in range(x + 1, y):
    if number % 2 != 0:
        total += number

print(total)

