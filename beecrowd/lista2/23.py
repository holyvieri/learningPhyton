n = int(input())
into = out = 0
for i in range(n):
    numbers = int(input())
    if numbers in range(9, 20):
        into += 1
    else:
        out += 1
print(f'{into} in')
print(f'{out} out')
