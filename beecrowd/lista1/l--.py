s = int(input())
h = s//3600
m = (s%3600)//60
s = (s%60)//1
time = f'{h}:{m}:{s}'
print(f'{time}')