z, g = input().split()
d, c = input().split()

if d == z and g == c:
    print("Driblado")
    print("Gol")

if d == z and g != c:
    print("Driblado")
    print("...e o goleiro pega")

elif d != z:
    print("Bloqueado")