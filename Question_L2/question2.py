L1, P1 = input().split()
L2, P2 = input().split()
L3, P3 = input().split()

Lucas = int(L1) + int(L2) + int(L3)
Pedro = int(P1) + int(P2) + int(P3)

if int(Lucas) > int(Pedro):
    print("Lucas")
elif int(Lucas) == int(Pedro):
    print("Empate")
elif int(Lucas) < int(Pedro):
    print("Pedro")
