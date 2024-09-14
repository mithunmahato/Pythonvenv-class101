#!/usr/bin/python3

class FloWer:
    def __init__(self,name,color):
        self.name=name
        self.color=color
        
    def __str__(self):
        return f"{self.name}({self.color})"
        
fl = FloWer("rose","red")
print(fl)
del fl.color
print(fl)
