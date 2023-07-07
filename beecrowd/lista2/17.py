total = 0
positive = 0
for n in range(0,6):
    numbers = float(input())
    if numbers > 0:
        total += numbers
        positive += 1
average = float(total/positive)
print(f'{positive} valores positivos')
print(f'{average:.1f}')
