a = [1, 2, 3, 4, 5]
b = [10, 20, 30, 40, 50]
c = [100, 200, 300, 400, 500]
d = [1000, 2000, 3000, 4000, 5000]

result = list(zip(a, b, c))

args = [a, b, c, d]

result_new = list(zip(*args))

print(result_new)

print(args)
print(*args)

print(help(tuple))
