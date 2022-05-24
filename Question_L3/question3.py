letter: str = "A"
num = 1

while letter != "#" and num != 0:
    letter, num = input().split()
    num = int(num)

    if 90 > num > 0:
        print(letter, "Internar")
    elif num >= 90:
        print(letter, "Alta")
