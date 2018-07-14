# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 21:48:16 2017

@author: Sandbox999
"""
#this is Sandbox's Python Code

#object-oriented programming

class Animal:
    __name = "" #__ indicates private variables
    __height = 0
    __weight = 0
    __sound = 0
    
    def __init__(self, name, height, weight, sound): #constructor
        self.__name = name
        self.__height = height
        self.__weight = weight
        self.__sound = sound
    
    def set_name(self, name): #to access private variables use set & get methods
        self.__name = name
        
    def get_name(self):
        return self.__name
    
    def set_height(self, height): #to access private variables use set & get methods
        self.__height = height
        
    def get_height(self):
        return self.__height
    
    def set_weight(self, weight): #to access private variables use set & get methods
        self.__weight = weight
    
    def get_weight(self):
        return self.__weight
    
    def set_sound(self, sound): #to access private variables use set & get methods
        self.__sound = sound
    
    def get_sound(self):
        return self.__sound
    
    def get_type(self):
        print("Animallllll")
        
    def toString(self):
        return "{} is {} inch tall and {} kg heavy and says {}".format(self.__name,
                                                                        self.height,
                                                                        self.weight,
                                                                        self.sound)
        
cat = Animal('MyWhiskers', 33, 10, 'meowww')

print(type(cat))

print(cat)
    

print(cat.get_sound())

    
print(cat.get_type())