country = ["india", "china", "pakistan"]
names = ["kantharao", "syam", "joshu", 0]
empty = []

print(all(country))
print(all(names))
print(all(empty))

print(any(country))
print(any(names))
print(any(empty))

# map(function, iterablObject)

phone_brand = ["NOKIA", "SAMSUNG", "REDMI", "APPO"]


def length(x):
    return len(x)


len_brands = list(map(length, phone_brand))
print(len_brands)

numbers = [1, 2, 5, 20, 30, 85, 15, 18, 19, 500, 50, 60, 70, 80, 70]


def compare(x):
    return x < 30


numLess_20 = list(filter(compare, numbers))
print(numLess_20)
maxNum = max(numbers)
print(maxNum)
minNum= min(numbers)
print(minNum)
sumNUm = sum(numbers)
print(sumNUm)

