import abc

#Superclase
class PersonaEquipo(metaclass=abc.ABCMeta):
    __metaclass__ = abc.ABCMeta
    def __init__(self, nom):
        self.nombre = nom
    def agregar_nombre(self, nom):
            self.nombre = nom

    def obtener_nombre(self):
        return self.nombre

    @abc.abstractmethod
    def entrenar(self):
        pass
#Clase Hija que herada de la clase padre Persona equipo
class Futbolista(PersonaEquipo):
    def __init__(self, n):
        super(Futbolista, self).__init__(n)
        self.posicion_campo=""

    def agregar_posicion(self, pos):
        self.posicion_campo =pos
    def obtener_posicion(self):
        return self.posicion_campo

    def entrenar(self):
        print("Yo " +self.nombre +", futbolista, hago practica en el entrenamiento")
#Clase Hija que herada de la clase padre Persona equipo
class Entrenador(PersonaEquipo):
    def __init__(self, n):
        super(Entrenador, self).__init__(n)
        self.cargo_entrenador=""

    def agregar_cargo_entrenador(self, pos):
        self.cargo_entrenador =pos
    def obtener_posicion(self):
        return self.cargo_entrenador
    def entrenar(self):
        print("Yo " +self.nombre +", entrenador, soy el director del entrenamiento")
#Clase Hija que herada de la clase padre Persona equipo
class Medico_Equipo(PersonaEquipo):
    def __init__(self, n):
        super(Medico_Equipo, self).__init__(n)
        self.titulo=""

    def entrenar(self):
        print("Yo " +self.nombre +", medico, atiendo a los jugadores  en el entrenamiento")

#Clase Hija que herada de la clase padre Persona equipo
class Presidente_Equipo(PersonaEquipo):
    def __init__(self, n):
        super(Presidente_Equipo, self).__init__(n)
        self.num_prpidedades=""

    def entrenar(self):
        print("Yo " +self.nombre +", presidente, pongo el dinero en el entrenamiento")


#Run
f= Futbolista("Antonio")
e=Entrenador("Jose")
m=Medico_Equipo("Ramon")
p=Presidente_Equipo("Francisco")

Lista =[ f,m,p,e]
for l in Lista:
    l.entrenar()


