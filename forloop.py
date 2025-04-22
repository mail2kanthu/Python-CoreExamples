salaries = [20000, 30000, 40000, 100000]
new_salary = []
for i in salaries:
    if i < 40000:
        increment = i + (i * 10 / 100)
        new_salary.append(increment)

print(new_salary)
