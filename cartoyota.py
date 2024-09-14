class car:
    def __init__(dfdf,name,brand):
        dfdf.name=name
        dfdf.brand=brand
    
    def myfunct(kdkd):
        print("This is a " + kdkd.name)
        print("This is a " + kdkd.brand)
        
class Vehicle(car):
    def __init__(ilil, name, brand):
      car.__init__(ilil,name,brand)


mycar = car("Toyota","camry")

mycar.myfunct()

myvehical = Vehicle("Audi","Q5")
myvehical.myfunct()

