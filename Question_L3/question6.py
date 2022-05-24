start, end = map(int, input().split())
count = 0

for i in range(start, end + 1):
    multiplies = 0

    for j in range(2, i + 1):
        if 0 == i % j:
            multiplies += 1
    if multiplies != 1:
        continue
    count += 1

print(count)
