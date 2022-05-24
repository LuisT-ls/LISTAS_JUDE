a, b, c = input().split()

resposta = int(a) * int(b)

if resposta > int(c):
    print("S")
elif resposta <= int(c):
    print("N")