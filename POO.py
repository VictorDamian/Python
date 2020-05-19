class Persona:

    Sexo = ""
    Comunicacion = False

    def __init__(self, name, age):
        self.Nombre = name
        self.Edad = age

    def Caminar(self):
        print("Estoy aminando")

    def Comer(self):
        print("Estoy comiendo")

    def Hablar(self,mensaje) :
        print(mensaje)

    def Cumpleanos(self):
        self.Edad = self.Edad + 1

    def Sexo(self,sexo) :
        self.Sexo = sexo

    def Preguntar(self) :
        Persona.Comunicacion = True

    def Pensar(self):
        pensamiento = "no pienso"
        if self.Edad < 20 :
            pensamiento = "pienso en ponys"
        else:
            pensamiento = "tener trabajo"
        print(pensamiento)

class Femenino(Persona) :

    def __init__(self,name,age):
        Persona.__init__(self,name,age)
        Persona.Sexo = "femenino"

    def Preguntar(self) :
        Persona.Comunicacion = True

    def __init__(self):
        self.mujer = Persona("Lupe",22)
        self.mujer.Sexo("femenino")
        self.Preguntar

    def hablar(self,pregunta):
        if pregunta == 1 :
            print("mi nombre es "+self.mujer.Nombre)


class Masculino(Persona):

    def __init__(self,name,age):
        Persona.__init__(self,name,age)
        Persona.Sexo = "masculino"

    def Contestar(self):
        if Persona.Comunicacion :
            self.Hablar("que pasa")
         
    def Correr(self,edad):
        if edad > 5:
            self.Caminar()
        else :
            print("no puedo")

    def __init__(self):
        self.hombre = Persona("Tony", 25)
        self.hombre.Sexo("masculino")
        self.Hablar
    def contesta(self):
        if hombre.Comunicacion:
            print("hola")

humano = Femenino("juana",22)
humano2 = Masculino("juan",1)
humano.Preguntar()
humano2.Contestar()
humano2.Correr(humano2.Edad)

p1 = Femenino.Preguntar()
p2=Masculino.Hablar()