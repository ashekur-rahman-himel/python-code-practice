'''
Write a Python function that takes a list and returns a new list with distinct elements from the first list.
Sample List : [1,2,3,3,3,3,4,5]
Unique List : [1, 2, 3, 4, 5]
'''


def func_list(b):

    x = []

    for a in b:

        if a not in x:

            x.append(a)

    return x
List = [1,2,3,3,3,3,4,5]

print(func_list(List)) 