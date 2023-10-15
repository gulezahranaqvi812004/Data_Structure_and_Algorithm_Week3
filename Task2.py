# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 08:17:07 2023

@author: Dell 7490
"""



def nSquare(array):
    length=len(array)
    result=[]
    for i in range(0,length):
        for j in range(i+1,length):
            if array[i][1]>=array[j][0] and array[i][0]<=array[j][1]:
                result.append((i+1,j+1))
          
    return result    

input=[[1,4],[2,5],[7,9],[9,10],[6,10]]
print(nSquare(input))

