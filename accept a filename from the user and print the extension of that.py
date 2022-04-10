# -*- coding: utf-8 -*-
"""
Created on Sun Apr 10 12:00:10 2022

@author: Arin
"""



fn= input("Enter Filename: ")

f = fn.split(".")

ext={"py":"python","txt":"text"}

print ("Extension of the file is : " + ext["py"]  ) 
