"""
Given an integer n,
 return the number of trailing 
 zeroes in n!.

Ej: 3! -> 0
    5! -> 1 (120 tiene un cero)

"""

#Input: a single num, cero
# Plan: Receive num
# iterate previus nums. How? for 1 to range num/ while
# multiply previus to actual, counter
# counter ceros in the result
#output: single num counting zeros
def factorials(num): 
    factorial= num*(num-1) #5 por 4 - 20   
    while num > 1:  
        num = num - 2  # ya no es 5 es 3           
        res = factorial*(num)  # 20 por 3 -- 60    
        res = res
        print (res)   # print 60    
    

user = int(input())
print(factorials(user))