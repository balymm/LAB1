def down_zero_generator(n):
    for i in range(n, n - n - 1, -1):
        yield i

n = int(input())
to_zero = down_zero_generator(n)

for zeros in to_zero:
    print(zeros)