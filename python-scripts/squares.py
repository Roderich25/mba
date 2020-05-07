def squares(n):
    print(n)
    for i in range(n):
        # print(i,end='')
        if i % n == 0 or (i + 1) % n == 0:
            print("*" * n)
        else:
            print("*", " " * (n - 2), "*", sep="")
    print()


for i in range(2, 8):
    squares(i)
