vehicle= {"car":"tiago","airbus":"usa"}
print(vehicle)

school = {"school1": {"CLASSA":70,
                      "CLASSB":80,
                      "CALSS C":90},

          "school2": {"CLASSA": 80,
                      "CLASSB": 80,
                      "CALSS C": 90}
          }

print(school["school1"],school["school2"])
print(school["school1"]["CLASSA"])

list1 = list(school.keys())
print(list1)
list2 = list(school.values())
print(list2)