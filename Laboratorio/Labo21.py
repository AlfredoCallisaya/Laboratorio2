import math
class Circulo:
    def __init__ (self, radio):
        self.radio = radio
    def Area(self):
        return math.pi *self.radio**2
    def Circunferencia (self):
        return 2* math.pi*self.radio
radio= float (input("Ingrese un numero para caluclar el area y circunferencia del circulo: "))
circulo =Circulo(radio)
print(f"El area del circulo es: {circulo.Area()}")
print (f"La circunferencia del circulo es: {circulo.Circunferencia()}")