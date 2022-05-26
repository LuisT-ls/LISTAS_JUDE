num = int(input())
par = []
impar = []

for i in range(num):
    number: int = input().split()
    if number % 2:
        par.append(number)
    else:
        impar.append(number)

print(f"{par}")
print(f"{impar}")
