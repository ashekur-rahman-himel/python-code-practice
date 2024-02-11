#3. Write a Python script to check whether a given key already exists in a dictionary.

myDi = {
    1: 'value1',
    2: 'value2',
    3: 'value3'
}

if 1 in myDi:
    print("key exists in the dictionary")
else:
    print("key no exist in the dictionary")
