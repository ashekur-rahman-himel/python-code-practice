#1. Write a Python script to sort (ascending and descending) a dictionary by value.

student = {
    "sakib" : 10,
    "rakib" : 20,
    "rahim" : 5

}

y = student.values()

x = sorted(y)

print(x)

#y = student.values()

z = sorted(y,reverse= True)

print(z)


