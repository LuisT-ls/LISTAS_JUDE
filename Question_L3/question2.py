inhabitants = int(input())

count = 0
num = []
man = 0
woman = 0

while count < inhabitants:
    count = count + 1
    num = int(input())
    if num == 1:
        man = man + 1
    elif num == 2:
        woman = woman + 1

print(man)
print(woman)