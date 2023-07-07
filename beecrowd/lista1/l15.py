values = input().split(" ")
a = int(values[0])
b = int(values[1])
c = int(values[2])
m = (a+b+(abs(a-b)))/2
if (m > c):
    print(f'{m:.0f} eh o maior')
else:
    print(f'{c:.0f} eh o maior')