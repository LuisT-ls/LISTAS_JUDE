T = int(input())
P = "O Havai pode dormir tranquilo"

num = 1

while num != 0:
    num = int(input())

    if num > T:
        P = "ALARME"

print(P)
