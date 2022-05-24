attack, defense, dust = map(int, input().split())
force = attack + defense + dust

percent = int((force / 110) * 100)

if percent > 100:
    print("Hum, parece que houve um erro")
else:
    if percent <= 50:
        print("Seu pokemon nao fara progresso em batalhas")
    elif percent <= 66:
        print("Seu pokemon esta acima da media")
    elif percent <= 79:
        print("Seu pokemon certamente me chamou atencao")
    else:
        print("Seu pokemon e uma maravilha")
