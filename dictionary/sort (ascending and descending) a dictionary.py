#1. Write a Python script to sort (ascending and descending) a dictionary by value.

student = {
    "sakib" : 10,
    "rakib" : 20,
    "rahim" : 5

}

y = student.values()

x = sorted(y)

print(x)

student1 = {
    "sakib" : 10,
    "rakib" : 20,
    "rahim" : 5

}

s = student1.values()

a = reversed(s)

print(a)
