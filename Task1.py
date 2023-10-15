# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 15:07:30 2023

@author: Dell 7490
"""


#PART A

def integerMultiplication(int1, int2):
    
    str_a = str(int1)
    str_b = str(int2)

    length1 = len(str_a)
    length2 = len(str_b)
    totalLength=length1+length2
    product = [0] * (totalLength)


    for i in range(length1 -1,-1,-1):
        for j in range(length2 - 1,-1,-1):
            temp = int(str_a[i]) * int(str_b[j])
            product[i + j + 1] += temp

   
    carry = 0
    for i in range(len(product) - 1, -1, -1):
        total = product[i] + carry
        product[i] = total % 10
        carry = total // 10

    result_str = ""
    for num in product:
       result_str += str(num)  

    return result_str

#PART B

def stringMultiplication(str_a, str_b):
    
    

    len_a = len(str_a)
    len_b = len(str_b)
    
    partial_products = [0] * (len_a + len_b)


    for i in range(len_a -1,-1,-1):
        for j in range(len_b - 1,-1,-1):
            product = int(str_a[i]) * int(str_b[j])
            partial_products[i + j + 1] += product

   
    carry = 0
    for i in range(len(partial_products) - 1, -1, -1):
        total = partial_products[i] + carry
        partial_products[i] = total % 10
        carry = total // 10

    result_str = ""
    for num in partial_products:
       result_str += str(num)  

    return result_str


a = "12"
b = "3"
result = integerMultiplication(12,12)
r2=stringMultiplication(a, b)
print(r2)
print(result)
