x = int(input())

h = x // 3600

m = int((x % 3600) // 60)
s = int((x % 3600) % 60)

print(str(h) + "h", str(m) + "m", str(s) + "s")
