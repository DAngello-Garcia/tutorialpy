class Minecraft: #No es necesario el uso de ()

    def __init__(self,altura):     #constructor
        self.altura_Steve = altura
        self.color_cabello = 'café'     
        self.__vida = True      #encapsulamiento
        self.__cabeza = "Cabeza cuadrada"

    def __str__(self):  #convertir en string legible para el humano un objeto
        return "{} {} {}".format(self.altura_Steve, self.color_cabello, self.__vida)

    def __repr__(self): #convertir en string legible para el "developer o máquina" un objeto
        return f'{self.__class__.__name__}(altura_Steve={self.altura_Steve}, color_cabello={self.color_cabello}, vida={self.__vida}'


    def cambiarAltura(self,altura):
        self.altura_Steve = altura

    def __prohibidoAcceso(self):    #encapsulamiento
        pass

    def cambiarColorCabello(self,color):        #polimorfismo
        self.color_cabello = color
        print("El nuevo color de cabello es: ",color)

    def cambiar(self, cab):
        self.__cabeza = cab

    def getAltura(self):
        return self.__cabeza

altura = 2.5
steve = Minecraft(altura)
steve.cambiarAltura(3.4)
#print(str(steve.getAltura()))

class Papu(Minecraft):  #herencia
    def __init__(self, altura, nivel):
        super().__init__(altura)
        # Minecraft.__init__(self, altura) ambas hacen lo mismo
        self.nivel_papu = nivel

    def cambiarColorCabello(self,color):        #polimorfismo
        self.color_cabello = color
        print("El nuevo color de cabello es: ",color," y es muy bonito")

    def cambiarNivel(self, nivel):
        this.nivel_papu = nivel

#steve.cambiar("False")  #El encapsulamiento no permite modificar atributos
print(str(steve))
print(repr(steve))
