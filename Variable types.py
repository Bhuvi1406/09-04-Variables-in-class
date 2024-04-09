class phone():
    def __init__(self,brand,price,chargertype):
        self.brand=brand
        self.price=price
        self.chargertype=chargertype
    def display(self):
        print("Brand: ",self.brand)
        print("Price: ",self.price)
        print("Charger Type: ",self.chargertype)

Bhuvanesh=phone("C","a","o")
Bhuvanesh.display()
