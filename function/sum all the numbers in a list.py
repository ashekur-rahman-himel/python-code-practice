#Write a Python function to sum all the numbers in a list


def sum(num):

    total = 0
    for x in num:
     
        total =  total + x
    
    return total
number = [1,5,6,9]

print(sum(number))
        
