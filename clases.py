class Minecraft():

    def __init__(self,alt):     #constructor
        self.altura_Steve = alt
        self.color_cabello = 'café'     
        self.__vida = True      #encapsulamiento

    def cambiarAltura(self,altura):
        self.altura_Steve = altura

    def __prohibidoAcceso(self):    #encapsulamiento
        pass

    def cambiarColorCabello(self,color):
        self.color_cabello = color

    def getAltura(self):
        return self.altura_Steve

# altura = 2.5
# steve = Minecraft(altura)
# steve.cambiarAltura(3.4)
# print(str(steve.getAltura()))

class Papu(Minecraft):  #herencia
    pass


