xx = (lambda x: x ** 3)(3)

print(xx)

example = (lambda x, y: (x + y) / 2)
print(example(10, 20))

even_odd = lambda x: "even" if x % 2 == 0 else "odd"
print(even_odd(5))

list1 = [1, 2, 3, 4, 5, 6]
for i in list1:
    print(i, ":", (lambda x: "even" if x % 2 == 0 else "odd")(i))

mapList = list(map(lambda x: "even" if x % 2 == 0 else "odd",list1))
print(mapList)
