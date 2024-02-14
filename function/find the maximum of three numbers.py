#Write a Python function to find the maximum of three numbers.


def max(a, b, c): 
 
    if (a > b) and (a > c): 
        return a
 
    elif (b > a) and (b > c): 
        return b 
    else: 
        return c 

a = 30
b = 14
c = 20
print(max(a, b, c)) 



