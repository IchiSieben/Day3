print(x for x in range(50) if x < 5)

print([x for x in range(50) if x < 5])

l = [0,1,2,3,4,5,6,7,8,9]
pares = filter(lambda n: n % 2.0 == 0, l)
print([x for x in pares])