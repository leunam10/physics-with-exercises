"""
Given two vectors a and b compute (in two or three dimensions):

 - sum
 - scalar product
 - vector product

"""


import numpy as np
import math
import sys


def vector_sum(space_dimension, v1, v2):
    v_sum = np.zeros((space_dimension))
    for i in range(space_dimension):
        v_sum[i] = v1[i]+v2[i]
    
    return v_sum
    
def vector_scalar_product(v1, v2):
    return np.sum(v1*v2)

def cross_product(space_dimension, v1, v2):

    m = np.zeros((3, space_dimension))
    for i in range(3):
        for j in range(space_dimension):
            if i == 1:
                m[i][j] = v1[j]
            elif i == 2:
                m[i][j] = v2[j]


    vx = m[1][1]*m[2][2] + m[1][2]*m[2][1]
    vy = m[1][0]*m[2][2] - m[1][2]*m[2][0]
    vz = m[1][0]*m[2][1] + m[1][1]*m[2][0]
        
    
    return np.array([vx, vy, vz])

## INPTU PARAMETERS 
# dimension of the vector space
space_dimension = 3
v1 = np.array([1,2,3])
v2 = np.array([0,2,1])
#############################################àà


v_sum = vector_sum(space_dimension, v1, v2)
v_scalar_product = vector_scalar_product(v1, v2)
v_cross_product = cross_product(space_dimension, v1, v2)

print(f"\nv1 = {v1}")
print(f"v2 = {v2}\n")
print("SUM")
print(f"{v1} + {v2} = {v_sum}\n")
print("SCALAR PRODUCT")
print(f"{v1} * {v2} = {v_scalar_product}\n")
print("CROSS PRODUCT")
print(f"{v1} x {v2} = {v_cross_product}\n")

