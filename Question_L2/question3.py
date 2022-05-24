X1, Y1 = input().split()
X2, Y2 = input().split()

conta1 = int(X1) + int(X2)
conta2 = int(Y1) + int(Y2)

if int(X1) == int(X2) and int(Y1) == int(Y2):
    print("Soltar pacote")
elif int(X1) != int(X2) or int(Y1) != int(Y2):
    print("Nao soltar pacote")