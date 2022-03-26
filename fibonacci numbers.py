# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 11:46:56 2022

@author: Arin
"""

n = int(input("Enter the value of 'n': "))
a = 0
b = 1
sum = 0
count = 1
print("Fibonacci Series: ", end = " ")
while(count <= n):
  print(sum, end = " ")
  count += 1
  a = b
  b = sum
  sum = a + b