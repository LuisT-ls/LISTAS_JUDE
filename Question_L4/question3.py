num = int(input())
par = []
impar = []

for i in range(num):
    a = int(input())
    
    if a % 2 == 0:
        par.append(int(a))
    else:
        impar.append(int(a))

print(f"{par}")
print(f"{impar}")
