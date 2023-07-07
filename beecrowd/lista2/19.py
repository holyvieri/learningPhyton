positive = negative = even = odd = 0
for n in range(0, 5):
    numbers = int(input())
    if numbers > 0:
        positive += 1
    elif numbers < 0:
        negative += 1
    if numbers % 2 == 0:
        even += 1
    else:
        odd += 1
print(f'{even} valor(es) par(es)')
print(f'{odd} valor(es) impar(es)')
print(f'{positive} valor(es) positivo(s)')
print(f'{negative} valor(es) negativo(s)')
