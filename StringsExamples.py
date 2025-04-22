print("hellow" + " world")
name = "www.datascience.com"
print(len(name))
print(name.startswith("www"))  # returns true
print(name.endswith("www"))  # returns false
print(name.endswith("com"))
print(name.startswith("data", 4, 12))

# replace()
name = "j-o-s-e-p-h"
name = name.replace("-", "")
print(name)
university = "h-ar-w-a-r-d"
university = university.replace("-", "", 2)
print(university)

# spelling substituiotn
sentence = "I live In India"
print(sentence.swapcase())  # swaps each letter upper to lowre, lower to upper
print(sentence.capitalize())  # conver  each start work in lower
print(sentence.upper())
print(sentence.lower())
print(sentence.title())  # convert each start leter with upper

# clipping methods strip(), lstrip(), rstrip()
exa = "  example  "
print(exa.strip())
print(exa.lstrip())
print(exa.rstrip())
print(exa.strip().strip("e"))  # removes space and then e letter removes
print(dir("space"))

# Index ans slicing
car = "ferrari"
print("firlst letter", car[1:5])
print(car[1:])
print(car[:len(car)])

print(car[-5:-1])
print(car[1:5:2])
print(*car)
print(car + "dallas")
print(car * 3)

# formattting %d,%s,%f

stringformat = "I am %d old , my height is %.2f cm"
stringformat1 = " In the school %s are there"
age = 40
height = 160.25
print(stringformat % (age, height))
print(stringformat1 % "teachers")

bazaar = "I bouthgt {} kilos of {} from bazar"
kilos = 2
vegtlbles = "tomotos"
print(bazaar.format(kilos, vegtlbles))

print("I bouthgt {} kilos of {} from bazar".format(kilos, vegtlbles))

result = "{3} vs {2} ended {1} - {0}"
print(result.format(3, 4, "ind", "pak"))

print(f"I bouthgt {kilos} kilos of {vegtlbles.upper()} from bazar")
