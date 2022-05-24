N = int(input())

chapeuzinho, vo, lobo = 0,0,0

for i in range(N, 0, -1):
    if chapeuzinho == vo and vo == lobo:
        chapeuzinho += 1
    elif chapeuzinho > vo and vo == lobo:
        vo += 1
    else:
        lobo += 1

print("Chapeuzinho Vermelho", chapeuzinho)
print("Vovozinha", vo)
print("Lobo Mau", lobo)