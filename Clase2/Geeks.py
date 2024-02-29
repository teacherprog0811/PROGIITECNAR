class Geeks: 
     def __init__(self): 
          self._age = 0
       
     # using property decorator 
     # a getter function 
     @property
     def age(self): 
         print("getter method called") 
         return self._age 
       
     # a setter function 
     @age.setter 
     def age(self, a): 
         print("setter method called") 
         self._age = a 