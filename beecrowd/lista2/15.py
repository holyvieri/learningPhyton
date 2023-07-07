positive = 0
for numbers in range(0, 6):
    n = float(input())
    if n > 0:
        positive += 1
print(f'{positive} valores positivos')
