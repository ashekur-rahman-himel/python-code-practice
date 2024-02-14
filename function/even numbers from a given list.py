'''
Write a Python program to print the even numbers from a given list.
Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]
Expected Result : [2, 4, 6, 8] 

'''

def even_num(x):
   
    even = []
       
    for n in x:
     
        if n % 2 == 0:
      
            even.append(n)  
    return even

y = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(even_num(y)) 