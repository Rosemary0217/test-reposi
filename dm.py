# -*- coding: utf-8 -*-
"""
Created on Wed Jan 26 16:57:18 2022

@author: Gabrielle
"""

class hospital(object):
    def __init__(self,num_of_quotes,name):
        self.num_of_quotes=num_of_quotes
        self.name=name
        self.residents=[]    #住院师名单，初始化为空
    def get_num_of_residents(self):
        return len(self.residents)
    def get_num_of_quotes(self):
        return self.num_of_quotes
    def add_resident(self,resident_name):
        self.residents.append(resident_name)
    def remove_resident(self,resident_name):
        self.residents.remove(resident_name)
    
h1=hospital(3,"h1")
h2=hospital(2,"h2")

h1.add_resident("Joe")
print(h1.get_num_of_quotes())
print(h1.get_num_of_residents())
h1.remove_resident("Joe")
print(h1.get_num_of_quotes())
print(h1.get_num_of_residents())
    
