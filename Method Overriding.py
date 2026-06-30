class Vehicle:
    def __init__(self, brand, model):
        self.brand=brand
        self.model=model
    def show_info(self):
        print(f"_Brand : {self.broad}")
        print(f"Model : {self.model}")
class Car(Vehicle):
    def __init__(self,brand, model,color):
        super().__init__(brand, model)
        self.color=color
    def show_info(self):
        print(f"model : {self.model}")
        print(f"Brand : {self.brand}")
        print(f"Color : {self.color}")
s=Car(input("Enter the Brand name : "),
      input("Enter the model name : "),
      input("Enter the color of the car : "))
s.show_info()
