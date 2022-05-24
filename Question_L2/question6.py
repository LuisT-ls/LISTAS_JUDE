A, D, P = input().split()

resultado: int = (int(A) + int(D) + int(P))

percentage = resultado / 110
percentage: float = percentage * 100

if 0 <= percentage <= 100:

    if 0 <= percentage < 51:
        print("Seu pokemon nao fara progresso em batalhas")
    elif 51 <= percentage < 67:
        print("Seu pokemon esta acima da media")
    elif 67 <= percentage < 80:
        print("Seu pokemon certamente me chamou atencao")
    else:
        print("Seu pokemon e uma maravilha")
else:
    print("Hum, parece que houve um erro")