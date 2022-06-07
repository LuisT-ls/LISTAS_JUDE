num = int(input())
par = []
impar = []

for i in range(num):
    a: int = input().split()
    
    if a % 2 == 0:
        par.append(a)
    else:
        impar.append(a)

print(f"{par}")
print(f"{impar}")
