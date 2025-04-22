def even_odd(*number):
    even = []
    odd = []
    for i in number:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    print(even)
    print(odd)

    even_odd(1, 2, 5, 8, 18, 9, 20, 500, 750, 3, 19)
    # key arguments


def keyargs(**team):
    for key, value in team.items():
        print(key, "is in", value)


dict_team = {"KKR": "KOLKATTA",
             "DR": "DELHI",
             "SRH": "HYDERABAD"}
keyargs(**dict_team)