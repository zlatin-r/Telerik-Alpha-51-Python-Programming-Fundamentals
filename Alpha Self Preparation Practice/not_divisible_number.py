N = int(input())

for i in range(1, N + 1):
    if i % 3 == 0 or i % 7 == 0:
        continue
    else:
        print(i, end=" ")
