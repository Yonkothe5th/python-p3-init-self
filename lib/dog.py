#!/usr/bin/env python3

class Dog:
    def __init__(self,name,breed="Mutt"):
        self.name = name
        self.breed = breed
        print (f"{name} is a {breed} type of dog.")
        
shadow=Dog("Shadow","Husky")