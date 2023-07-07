positive = 0
for numbers in range(0, 5):
    n = int(input())
    if n%2 == 0:
        positive += 1
print(f'{positive} valores pares')
