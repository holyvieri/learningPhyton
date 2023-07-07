n = int(input())
for even in range(n+1):
    if even%2 == 0 and even!=0:
        sqr = even**2
        print(f'{even}^2 = {sqr}')
