# Descripcion del juego
# Hay dos jugadores, por ronda cada jugar recibe 3 cartas y mediante el truco y el envido puede obtener puntos. Por ronda los jugadores pueden obtener entre entre 1 y 15 puntos. En caso de que no se halla utilizado ni el truco ni el envido, el jugador que gano 2 de tres jugadas obtiene un punto.

# Parte Envido:
    # Si en una mano hay 2 o más cartas del mismo palo, se contabiliza el envido regular, en el cual se cuentan los valores de las dos cartas mayores con palo comun y a ese total, se le suman 20 puntos. El resultado final (suma de valores de cartas de palo comun +20) es el valor del envido de cada jugador 
    # En caso de no haber cartas con palo comun, se contabiliza el valor de la carta mas alta en numero (Sabiendo que para los 10, 11 y 12 solose cuenta la unidad).
    # En caso de que una o ambas cartas del envido tengan valores de 2 cifras, se suman los valores correspondiente a la unidad de esas dos cifras y se le suman 20
    
#############################################
# Parte Truco:
    # Las cartas tienen jerarquias, por cada jugada gana la de mayor jerarquia o empate. En caso de que halla un ganador comienza en el siguiente turno, en caso de empate comienza el primer jugador de la ronda. La jerarquia se define con un numero, siendo de mayor jerarquia el numero mas grande. Los valores son: [1,2,3,4,5,6,7,8,9,10,11,12,13,14].
    # El truco lo gana el que gane 2 de las 3 jugadas. En caso de empate gana el primer jugador de la ronda.

# Elementos del juego
# - mazo -> total de cartas del juego
# - carta
# - jugador -> nombre, equipo (en caso de jugar en un equipo de 2 o 3)
# - mano -> conjunto de tres cartas de un jugador
# - jugada -> una carta de cada jugador (la primera, segunda o tercera)
# - cantar y responder -> el turno donde uno puede cantar un juego (truco o envido) y/o responder a un juego cantado
# - ronda -> las tres o dos jugadas, finalizada la ronda se continua con una nueva ronda
# - partida -> dos jugadores y un mazo, lleva tambien la puntuacion

# Tareas:

# [x] Crear una funcion MostrarScore en la clase partida que muestre el score del jugador 1 y el score del jugador 2
# [x] Crear una funcion CrearPartida en la clase partida que le permita al usuario ingresar el nombre del jugador 1 y el nombre del jugador 2
# [x] Crear una funcion Comenzar en la clase ronda que devuelva 3 cartas del mazo y las quite del mazo
# [] Crear una funcion MostrarCartas (en la clase partida, o jugador, o ronda, hay que ver donde la ponemos) que muestres las cartas de ambos jugadores    
# [] Crear la clase ronda, para generar una ronda nueva y repartir las cartas, tambien al comienzo de la ronda se genera un mazo nuevo. Hay que sacar la propiedad mazo de la clase partida y llevarla a la clase ronda.



# Lo que importemos va aca arriba
from dataclasses import dataclass, field
from typing import List
from random import sample, choice
from enum import IntEnum
import argparse

parser = argparse.ArgumentParser(description='Juego Truco, Peron vs Evita.')
parser.add_argument('--test', action='store_true', help='ejecuta los tests automaticos')
args = parser.parse_args()

class EstadoTruco(IntEnum):
    nosecanto = 1
    truco = 2
    retruco = 3
    valecuatro = 4
class EstadoMano(IntEnum):
    primera = 1
    segunda = 2
    tercera = 3

class RespuestaSiNo(IntEnum):
    si = 1
    no = 2

def printOrNotPrint(*objects):
    if logs:
        print(*objects)

def make_french_deck():
    return [Carta(14, "Espada", "Uno de"), Carta(9, "Espada", "Dos de"),Carta(10, "Espada", "Tres de"), Carta(1, "Espada", "Cuatro de"), Carta(2, "Espada", "Cinco de"), Carta(3, "Espada", "Seis de"),Carta(12, "Espada", "Siete de"), Carta(5, "Espada", "Sota de"), Carta(6, "Espada", "Caballo de"), Carta(7, "Espada", "Rey de"), Carta(13, "Basto", "Uno de"), Carta(9, "Basto", "Dos de"),Carta(10, "Basto", "Tres de"), Carta(1, "Basto", "Cuatro de"), Carta(2, "Basto", "Cinco de"), Carta(3, "Basto", "Seis de"),Carta(4, "Basto", "Siete de"), Carta(5, "Basto", "Sota de"), Carta(6, "Basto", "Caballo de"), Carta(7, "Basto", "Rey de"), Carta(8, "Copa", "Uno de"), Carta(9, "Copa", "Dos de"),Carta(10, "Copa", "Tres de"), Carta(1, "Copa", "Cuatro de"), Carta(2, "Copa", "Cinco de"), Carta(3, "Copa", "Seis de"),Carta(4, "Copa", "Siete de"), Carta(5, "Copa", "Sota de"), Carta(6, "Copa", "Caballo de"), Carta(7, "Copa", "Rey de"), Carta(8, "Oro", "Uno de"), Carta(9, "Oro", "Dos de"),Carta(10, "Oro", "Tres de"), Carta(1, "Oro", "Cuatro de"), Carta(2, "Oro", "Cinco de"), Carta(3, "Oro", "Seis de"),Carta(4, "Oro", "Siete de"), Carta(5, "Oro", "Sota de"), Carta(6, "Oro", "Caballo de"), Carta(7, "Oro", "Rey de") ]


@dataclass
class Carta:
    Valor: int
    Palo: str
    Nombre: str

    # STR y REPR son cuando alguien hace printOrNotPrint(carta) se muestre solo el nombre y el palo (con un espacio en el medio)
    def __str__(self):
        return "{} {}".format(self.Nombre, self.Palo)
    
    def __repr__(self):
        return "{} {}".format(self.Nombre, self.Palo)

    # GT, GE, LT, LE, son las comparaciones >,>=,<,<=, asi podemos comparar matematicamente dos cartas (ej, carta1 > carta 2)

    # Mayor
    def __gt__(self, other):
        return self.Valor > other.Valor
    # Mayor o igual
    def __ge__(self, other):
        return self.Valor >= other.Valor
    # Menor o igual
    def __lt__(self, other):
        return self.Valor < other.Valor
    # Menor o igual
    def __le__(self,other):
        return self.Valor <= other.Valor

@dataclass
class Mazo:
    Cartas: List[Carta] = field(default_factory=make_french_deck)

@dataclass
class Jugador:
    Nombre: str
    Equipo: str
    Mano: "Mano"
    PuntajeRonda: int = 0
    # - Crear una funcion MostrarCartas que muestres las cartas de la mano
    def mostrarCartas(self):
        printOrNotPrint(self.Nombre)
        printOrNotPrint(self.Mano.Cartas)

@dataclass
class Mano:
    Cartas: List[Carta] = field(default_factory=list)
    TantosDelIpa: int = 0

@dataclass
class Partida:
    Jugador1: "Jugador" = None
    Jugador2: "Jugador" = None
    PuntuacionJugador1:  int = 0
    PuntuacionJugador2:  int = 0
    Rondas: ["Ronda"] = field(default_factory=list)
    # - Crear una funcion CrearPartida en la clase partida que le permita al usuario ingresar el nombre del jugador 1 y el nombre del jugador 2
    def crear(self):
        printOrNotPrint("Estas creando una partida nueva")
        printOrNotPrint("Ingresa el nombre del jugador 1")
        nombreJugador1 = input()
        printOrNotPrint("Ingresa el nombre del jugador 2")
        nombreJugador2 = input()

        self.Jugador1 = Jugador(nombreJugador1, "Azul", Mano())
        self.Jugador2 = Jugador(nombreJugador2, "Rojo",  Mano())

        self.Rondas.append(self.crearronda())

    def crearTesting(self, jugador1: "Jugador", jugador2: "Jugador"):
        self.Jugador1 = jugador1
        self.Jugador2 = jugador2
        self.Rondas.append(self.crearronda())

    # - Crear una funcion que actualice los puntajes de los jugadores
    def puntajes(self, puntosPrimerJugador, puntosSegundoJugador):
        self.PuntuacionJugador1 += puntosPrimerJugador
        self.PuntuacionJugador2 += puntosSegundoJugador
        self.mostrarscore()
    
    # - Crear una funcion MostrarScore en la clase partida que muestre el score del jugador 1 y el score del jugador 2
    def mostrarscore(self):
        printOrNotPrint("Puntuacion {}: {}".format(self.Jugador1.Nombre, self.PuntuacionJugador1))
        printOrNotPrint("Puntuacion {}: {}".format(self.Jugador2.Nombre, self.PuntuacionJugador2))
        pass
  
    # - Crear una ronda
    def crearronda(self) -> "Ronda":
        if (self.PuntuacionJugador1 <= 30 and self.PuntuacionJugador2 <= 30):
            ronda = Ronda()
            ronda.iniciar(self.Jugador1, self.Jugador2)
            return ronda

@dataclass
class Truco:
    EstadoTruco: "EstadoTruco" = EstadoTruco.nosecanto
    QuienCanta: "jugador" = None
    SiloSabeCante: "jugador" = None
    ElQueAcepta: "jugador" = None
    NoSeAceptoElTruco: bool = False
    
    # la idea seria que al comienzo de la ronda se cree un objeto truco para que valla llevando la gestion del truco durante toda la ronda
    def cantarTruco(self, cantante: "jugador", aceptante: "jugador"):
        #Primero fijarse si se puede cantar truco y si el que canta puede cantarlo
        if(ambienteProduccion):
            if(not self.NoSeAceptoElTruco and (self.SiloSabeCante == cantante or self.SiloSabeCante == None) and (self.EstadoTruco != EstadoTruco.valecuatro)):
                siguienteNivelTruco = Truco.nextEstadoTruco(self.EstadoTruco)
                printOrNotPrint("{} queres cantar {}? 1/si 2/no".format(cantante.Nombre, siguienteNivelTruco.name))
                aceptoCantarTruco = RespuestaSiNo(int(input()))

                if(aceptoCantarTruco == RespuestaSiNo.si): # Aca se esta queriendo cantar el truco
                    self.EstadoTruco = siguienteNivelTruco # Actualizo el valor de EstadoTruco al nivel que se esta cantando
                    self.QuienCanta = cantante # Guardo al que canto el truco
                    self.ElQueAcepta = aceptante # Guardo al que acepto el truco
                    self.SiloSabeCante = aceptante # Le doy la potestad al que acepto al truco para retrucar
                
                    # Muestro el canto
                    printOrNotPrint("{} canto {}".format(cantante.Nombre, self.EstadoTruco.name)) #Ej: Mauro canto retruco

                    # Pregunto al otro jugador si acepta
                    printOrNotPrint("{} aceptas? 1/si 2/no".format(aceptante.Nombre))
                    aceptoTruco = RespuestaSiNo(int(input())) # transformo el input del usuario en un numero, y despues en un objeto RespuestaSiNo
                    
                    if(aceptoTruco == RespuestaSiNo.si): # Si el aceptante acepta
                        printOrNotPrint("quiero") # Muestro que se quiso
                        self.cantarTruco(aceptante, cantante) # aca hacemos una funcion recursiva, es decir una funcion que se llama a si misma
                    else: # Si no acepta el truco
                        printOrNotPrint("NO quiero") # Muestro que no se quiso
                        self.EstadoTruco = Truco.previousEstadoTruco(self.EstadoTruco) # Actualizo el Estado del Truco a un nivel anterior, ya que lo que se canto no se quiso, ej si no queres valecuatro, se pasa a retruco.
                        self.NoSeAceptoElTruco = True # Siempre que no se quiera el truco, el truco se termina
        else: # solo para testing, modo croto
            self.EstadoTruco = EstadoTruco.valecuatro
            self.NoSeAceptoElTruco = False
            self.QuienCanta = cantante
            self.ElQueAcepta = aceptante
            self.SiloSabeCante = aceptante
            
    #Sube un estaado de del IntEnum "estadoTruco"     
    @staticmethod
    def nextEstadoTruco(estadoTruco):
        proximoNivelDeTruco= {
            EstadoTruco.nosecanto: EstadoTruco.truco,
            EstadoTruco.truco: EstadoTruco.retruco,
            EstadoTruco.retruco: EstadoTruco.valecuatro
        }
        return proximoNivelDeTruco.get(estadoTruco, "Ese estado de truco no existe")
    #Baja un estado del IntEnum "estadoTruco"
    @staticmethod
    def previousEstadoTruco(estadoTruco):
        anteriorNivelDeTruco= {
            EstadoTruco.truco: EstadoTruco.nosecanto,
            EstadoTruco.retruco: EstadoTruco.truco,
            EstadoTruco.valecuatro: EstadoTruco.retruco,    
        }
        return anteriorNivelDeTruco.get(estadoTruco, "Ese estado de truco no existe ñery")

@dataclass
class EvaluacionCarta:
    ManoSiguienteTurno: "Jugador" = None
    NoManoSiguienteTurno: "Jugador" = None
    cartaJugMano: "Carta" = None
    cartaJugNoMano: "Carta" = None
    EstadoMano: "EstadoMano" = EstadoMano.primera
    GanadorRonda: "Jugador" = None
    GanadorPrimera: "Jugador" = None
    
    def evaluarCarta(self, jugadorMano: "Jugador", jugadorNoMano: "Jugador", cartaJugMano: "Carta", cartaJugNoMano: "Carta"):
            if(cartaJugMano > cartaJugNoMano): 
                jugadorMano.PuntajeRonda += 1  
                if(jugadorMano.PuntajeRonda >= 1.5):
                    self.GanadorRonda = jugadorMano # Gana jugador A
                else:
                    self.GanadorMano = jugadorMano
                    self.ManoSiguienteTurno = jugadorMano
                    self.NoManoSiguienteTurno = jugadorNoMano
                    if(self.EstadoMano == EstadoMano.primera):
                        self.GanadorPrimera = jugadorMano
                    self.EstadoMano =  EvaluacionCarta.nextEstadoMano(self.EstadoMano) 
                    

            
            elif(cartaJugMano < cartaJugNoMano):# Gana jugador B
                jugadorNoMano.PuntajeRonda += 1
                if(jugadorNoMano.PuntajeRonda >= 1.5):
                    self.GanadorRonda = jugadorNoMano 
                else:
                    self.GanadorMano = jugadorNoMano
                    self.ManoSiguienteTurno = jugadorNoMano
                    self.NoManoSiguienteTurno = jugadorMano
                    if(self.EstadoMano == EstadoMano.primera):
                        self.GanadorPrimera = jugadorNoMano
                    self.EstadoMano = EvaluacionCarta.nextEstadoMano(self.EstadoMano)
                    
                
            else:                                # Empate
                jugadorMano.PuntajeRonda += 0.5
                jugadorNoMano.PuntajeRonda += 0.5 
                if(self.EstadoMano == EstadoMano.primera):
                    self.GanadorPrimera = jugadorMano
                    self.ManoSiguienteTurno = jugadorMano
                    self.NoManoSiguienteTurno = jugadorNoMano
                    self.EstadoMano = EvaluacionCarta.nextEstadoMano(self.EstadoMano)
                elif(self.EstadoMano == EstadoMano.tercera):
                    self.GanadorRonda = self.GanadorPrimera
                elif(jugadorMano.PuntajeRonda >= 1.5):
                    self.GanadorRonda = jugadorMano
                elif(jugadorNoMano.PuntajeRonda >= 1.5):
                    self.GanadorRonda = jugadorNoMano
                else:        
                    self.ManoSiguienteTurno = jugadorMano
                    self.NoManoSiguienteTurno = jugadorNoMano
                    self.EstadoMano = EvaluacionCarta.nextEstadoMano(self.EstadoMano)
            return(self.ManoSiguienteTurno, self.NoManoSiguienteTurno)        
    
    @staticmethod
    def nextEstadoMano(EstadoMano):
        proximoNivelDeMano= {
            EstadoMano.primera: EstadoMano.segunda,
            EstadoMano.segunda: EstadoMano.tercera,
            }
        return proximoNivelDeMano.get(EstadoMano, "Ese estado de mano no existe")
    
@dataclass
class Ronda:
    Mazo: "Mazo" = None
    Truco: "Truco" = None
    RondaActiva: bool = True
    EvaluacionCarta : "EvaluacionCarta" = None
    # - Al comenzar la ronda, generar un nuevo mazo
    # - Asignarle las cartas a los jugadores
    def iniciar(self, jugador1: "Jugador", jugador2: "Jugador"):
        self.RondaActiva = True
        self.Truco = Truco() # Inicializo el truco
        self.Mazo = Mazo() # Inicializo el mazo (basicamente se crea el mazo)
        self.EvaluacionCarta = EvaluacionCarta()
        
        if(ambienteProduccion):
            jugador1.Mano.Cartas.clear() # Elimino las cartas que tenia el jugador anteriormente en la mano
            jugador2.Mano.Cartas.clear() # Elimino las cartas que tenia el jugador anteriormente en la mano
        
            # Este codigo se ejectua 3 veces. Reparte tres cartas.
            for _ in range(3):
                jugador1.Mano.Cartas.append(self.repartir()) # Le doy 1 carta al jugador 1
                jugador2.Mano.Cartas.append(self.repartir()) # Le doy 1 carta al jugador 2

        # mostar todas las cartas de cada jugador
        jugador1.mostrarCartas() # las 3 cartas del jugador 1
        jugador2.mostrarCartas() # las tres cartas del jugador 2
        
               
        # --------- PRIMER TURNO DE AMBOS JUGADORES
        while self.RondaActiva:
            # Turno Jugador A    
            self.Truco.cantarTruco(jugador1, jugador2)
            if(self.Truco.NoSeAceptoElTruco): # si no se acepto el truco se corta la ronda (es decir deja de haber turnos para los jugadores)
                self.RondaActiva = False
                break

            cartaJugadaJugadorA = Turno.iniciar(jugador1) # Inicia el turno con el jugador 1, lo cual le muestra sus cartas, le pregunta si quiere cantar truco (o retruco o valecuatro) y le pregunta cual quiere jugar. La funcion "iniciar" de Turno te devuelve la carta que se jugo.

            # Turno Jugador B
            
            self.Truco.cantarTruco(jugador2, jugador1)
            if(self.Truco.NoSeAceptoElTruco): # si no se acepto el truco se corta la ronda (es decir deja de haber turnos para los jugadores)
                self.RondaActiva = False
                break
            cartaJugadaJugadorB = Turno.iniciar(jugador2) # Inicia el turno con el jugador 2, lo cual le muestra sus cartas y le pregunta cual quiere jugar. La funcion "iniciar" de Turno te devuelve la carta que se jugo
            
            
            # Comparar las cartas jugadas para saber quien gano esa jugada
            GanadorPrimera, PerdedorPrimera = self.EvaluacionCarta.evaluarCarta(jugador1, jugador2, cartaJugadaJugadorA, cartaJugadaJugadorB)  
            

            if(self.EvaluacionCarta.GanadorRonda != None): # si alguien ganó el truco se corta la ronda (es decir deja de haber turnos para los jugadores)
                self.RondaActiva = False
                break
            
            # --------- SEGUNDO TURNO DE AMBOS JUGADORES  
            
            # Turno Jugador A
                        
            self.Truco.cantarTruco(GanadorPrimera, PerdedorPrimera)
            if(self.Truco.NoSeAceptoElTruco): # si no se acepto el truco se corta la ronda (es decir deja de haber turnos para los jugadores)
                self.RondaActiva = False
                break
            cartaJugadaJugadorA = Turno.iniciar(GanadorPrimera) # Inicia el turno con el jugador mano, lo cual le muestra sus cartas y le pregunta cual quiere jugar. La funcion "iniciar" de Turno te devuelve la carta que se jugo
            
            # Turno Jugador B
            
            self.Truco.cantarTruco(PerdedorPrimera, GanadorPrimera)
            if(self.Truco.NoSeAceptoElTruco): # si no se acepto el truco se corta la ronda (es decir deja de haber turnos para los jugadores)
                self.RondaActiva = False
                break
            cartaJugadaJugadorB = Turno.iniciar(PerdedorPrimera) # Inicia el turno con el jugador segundo en el turno, lo cual le muestra sus cartas y le pregunta cual quiere jugar. La funcion "iniciar" de Turno te devuelve la carta que se jugo
            
            # Comparar las cartas jugadas para saber quien gano esa jugada
            GanadorSegunda, PerdedorSegunda = self.EvaluacionCarta.evaluarCarta(GanadorPrimera, PerdedorPrimera, cartaJugadaJugadorA, cartaJugadaJugadorB)
            
            if(self.EvaluacionCarta.GanadorRonda != None):  # si alguien ganó el truco se corta la ronda (es decir deja de haber turnos para los jugadores)
                self.RondaActiva = False
                break
            
            # --------- TERCER TURNO DE AMBOS JUGADORES
           
                     
            # Turno Jugador A
            self.Truco.cantarTruco(GanadorSegunda, PerdedorSegunda)
            if(self.Truco.NoSeAceptoElTruco): # si no se acepto el truco se corta la ronda (es decir deja de haber turnos para los jugadores)
                self.RondaActiva = False
                break
            cartaJugadaJugadorA = Turno.iniciar(GanadorSegunda)  # Inicia el turno con el jugador segundo en el turno, lo cual le muestra sus cartas y le pregunta cual quiere jugar. La funcion "iniciar" de Turno te devuelve la carta que se jugo
            

            # Turno Jugador B
            self.Truco.cantarTruco(PerdedorSegunda, GanadorSegunda)
            if(self.Truco.NoSeAceptoElTruco): # si no se acepto el truco se corta la ronda (es decir deja de haber turnos para los jugadores)
                self.RondaActiva = False
                break
            cartaJugadaJugadorB = Turno.iniciar(PerdedorSegunda)  # Inicia el turno con el jugador segundo en el turno, lo cual le muestra sus cartas y le pregunta cual quiere jugar. La funcion "iniciar" de Turno te devuelve la carta que se jugo
        
            # Comparar las cartas jugadas para saber quien gano esa jugada
            self.EvaluacionCarta.evaluarCarta(GanadorSegunda, PerdedorSegunda, cartaJugadaJugadorA, cartaJugadaJugadorB)
            
            break
           
            
        # Se muestra el ganador
        if(self.Truco.NoSeAceptoElTruco):
            self.GanadorRonda = self.Truco.QuienCanta
        else:
            self.GanadorRonda = self.EvaluacionCarta.GanadorRonda

        printOrNotPrint("Gano la ronda {}, hizo {} puntos".format(self.GanadorRonda.Nombre, int(self.Truco.EstadoTruco))) # Mostramos quien gano la ronda, y el puntaje del estado del truco #TODO estamos dejandolo asi momentaneamente, ya que los puntos de la rondo incluirian el del envido tamb

        
    # - Crear una funcion Comenzar en la clase ronda que devuelva 3 cartas del mazo y las quite del mazo
    def repartir(self):
        carta = choice(self.Mazo.Cartas)
        self.Mazo.Cartas.remove(carta)
        if(carta in self.Mazo.Cartas):
            printOrNotPrint("Error, la carta repartida esta duplicada en el mazo o no fue removida. Carta: {}".format(carta))
            pass
        return carta
        

    def repartirJugador1(self):
        carta = choice(self.Mazo.Cartas)
        self.Mazo.Cartas.remove(carta)
        return carta
    
    def repartirJugador2(self):
        carta = choice(self.Mazo.Cartas)
        self.Mazo.Cartas.remove(carta)
        return carta

@dataclass
class Turno:
    @staticmethod
    def iniciar(jugador: "Jugador") -> "Carta":
        printOrNotPrint("                       ")
        printOrNotPrint("Jugador {} comienza tu turno".format(jugador.Nombre))
        printOrNotPrint("Jugador {} Indique que carta va a jugar? elija con el numero 1 2 o 3. ".format(jugador.Nombre))
        contador = 0
        for carta in jugador.Mano.Cartas:
            contador += 1
            printOrNotPrint("opcion {}: {}".format(contador, carta))
        if(ambienteProduccion):
            cartaAJugarIndice = int(input()) - 1
        else:
            cartaAJugarIndice = 0 # en modo testing siempre juega la primera que tenga
        cartaAJugar = jugador.Mano.Cartas[cartaAJugarIndice]
        jugador.Mano.Cartas.remove(cartaAJugar)
        printOrNotPrint("{} juega la carta {}".format(jugador.Nombre, cartaAJugar))
        printOrNotPrint("                       ")

        return cartaAJugar

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

imagen = r"""#####Ql,VBBB########################BBBBBBB##########BBBB#BBBBBBBBBBQ
#####~ "rQj Q#########################################BBB#B#BBQV]QQBQ
###O``rwr^(_#########################################BBBB###Bl   rQBQ
###r },V r l###########################################BB##BB`    |bB
###l'~`    (###############################################BB      ,Q
BB#B*       O##Q?-"D#################################BBBB#BBE      `8
QBBB$        :'   p######BBBB8DQ###BBBB#######BB#B##BBO  JQQ       ]Q
B#BBQ?          rB####BQDj?:_`  *E8##B#####BB######BBBBu  `       rQQ
###BBW*     - !8####Bg^          ',d########B#####BBBBBQV         8QQ
####B"`]q,_`m$#####BB?              B#############B###BBQ        ?QBB
B###K  ~z= q#######BBO"      'Vmw_  !##################BBQx    : QBBB
B##n   _r=*8#########g?JpR$Q* xji_   5####################Be ^<` ,wBB
B#Zv       m###@@##BB0~(]=!*-  -     v#####################p`"-~= *QB
Q8$DOO$W   g#######BOO ` rnWrllvih}   8B#BBB#####BB#######B?!      '6
Q$EWO8Q`   Q########mG  `0EJKObnit}  -W#B#####BBBBBBB#BQBBB|^,     -"
ggq5$Q?    B########Q^!rJzj2V^~~=    p###########BBBBBBQQQQhe]nj](}  
8OZW8h     ##########BQQ6P],<r,``    ~8BB##B#############BOlsWpO$$D  
8$DQBu,<=*K############B8Zx}?::,=` `]_ WBB####B#######B#BBUnVPRDg0D  
ggQQBQQQQQQ###########BQQQgzVPKW6q2(xWr szOQBBBB#B###BBB##mtKZO08Q8? 
8QQBBBBQBBQ##g6DQB###BQQQD(:^*^Wr    `rdW$Gvr!~?x:-pB#B#BQ]sZb6D0Q8d 
QBB#BB#BBBB006wznhODWQBBJ  ``_",`   '''_z85?~?`     !=?h0iP6WWd$DQQg^
QBQBBQBBQ0Zd5DU}n]|Ebntwluwx^!"_-`.,rV}eK! -l<-,`  .``  'VD8D6dED0Q8e
QBBQ8QQ0Oh5WgEbz}nutdQgt*=rn2-`!lqer,^v!`-<lJ".`.``!u?:n]<|mO$DD8g88D
"""
imagen2 = r"""/__   \_ __ _   _  ___ ___     / _ \___ _ __ ___  _ __ (_)___| |_ __ _ 
  / /\/ '__| | | |/ __/ _ \   / /_)/ _ \ '__/ _ \| '_ \| / __| __/ _` |
 / /  | |  | |_| | (_| (_) | / ___/  __/ | | (_) | | | | \__ \ || (_| |
 \/   |_|   \__,_|\___\___/  \/    \___|_|  \___/|_| |_|_|___/\__\__,_|"""

##########################  TESTS  #############################################

def testingSeguro(testACorrer):
    try:
        print(testACorrer.__name__)
        return testACorrer()
    except Exception as err:
        return "False, {}".format(err)

def testGanaMano(cartasMano, cartasNoMano):
    try:
        manoDePeron = Mano([Carta(cartasMano[0], "Uno de", "Espada"), Carta(cartasMano[1], "Uno de", "Palo"), Carta(cartasMano[2], "Siete de", "Espada") ])
        manoDeEvita = Mano([Carta(cartasNoMano[0], "Espada", "Dos de"),Carta(cartasNoMano[1], "Espada", "Tres de"), Carta(cartasNoMano[2], "Oro", "Seis de")])
        jugadorMano = Jugador("mano", "Mano", manoDePeron)
        jugadorNoMano = Jugador("noMano", "NoMano", manoDeEvita)
        partida = Partida()
        partida.crearTesting(jugadorMano, jugadorNoMano)
        return partida.Rondas[0].GanadorRonda == jugadorMano # lo que cambia es el jugador que tiene que ganar
    except Exception as err:
        return "False, {}".format(err)

def testGanaNoMano(cartasMano, cartasNoMano):
    try:
        manoDePeron = Mano([Carta(cartasMano[0], "Uno de", "Espada"), Carta(cartasMano[1], "Uno de", "Palo"), Carta(cartasMano[2], "Siete de", "Espada") ])
        manoDeEvita = Mano([Carta(cartasNoMano[0], "Espada", "Dos de"),Carta(cartasNoMano[1], "Espada", "Tres de"), Carta(cartasNoMano[2], "Oro", "Seis de")])
        jugadorMano = Jugador("mano", "Mano", manoDePeron)
        jugadorNoMano = Jugador("noMano", "NoMano", manoDeEvita)
        partida = Partida()
        partida.crearTesting(jugadorMano, jugadorNoMano)
        return partida.Rondas[0].GanadorRonda == jugadorNoMano
    except Exception as err:
        return "False, {}".format(err)

def ejecutarTestGanaMano(coleccionDeCasos):
    fallaron = []
    for x in coleccionDeCasos:
        if not testGanaMano(x[0], x[1]):
            fallaron.append("fallo, se esperaba gano mano {} {}".format(x[0], x[1]))
    return fallaron

def ejecutarTestGanaNoMano(coleccionDeCasos):
    fallaron = []
    for x in coleccionDeCasos:
        if not testGanaNoMano(x[0], x[1]):
            fallaron.append("fallo, se esperaba No mano {} {}".format(x[0], x[1]))
    return fallaron

def EsCasoExcepcionNoMano(i,j):
    return i[0] > j[0] and i[1] < j[1] and i[2] < j[2]

def EsCasoExcepcionMano(i,j):
    return i[0] < j[0] and i[1] > j[1] and i[2] > j[2]

def runTests():
    global ambienteProduccion
    global logs
    ambienteProduccion = False
    logs = False

    colección = []
    valorePosibles = range(3)
    for i in valorePosibles: # genera [i,j,g]
        for j in valorePosibles:
            for g in valorePosibles:
                listaAuxiliar = [i,j,g]
                if listaAuxiliar not in colección:
                    colección.append(listaAuxiliar)

    testsGanaMano = []
    testsGanaNoMano = []
    for i in colección:
        for j in colección:
            if j <= i or EsCasoExcepcionMano(i,j): 
                # aca encontro un conjunto de cartas, i es las cartas de mano y j las del no mano
                # la idea es guardar ese conjunto de cartas en una variable
                # creo que al final no sirve la coleccionDosD
                if EsCasoExcepcionNoMano(i,j):
                    testsGanaNoMano.append([i,j])
                else:
                    testsGanaMano.append([i,j]) # i NO ES UN ARRAY, es el indice, entonces i = 0 y j = 0 es la primer celda. Si j <= 0 entonces es que la celda es de la diagonal para abajo, si j>i entonces es la diagonal hacia arriba (sin contar la celda de la diagonal) # aca si tengo que usar coleccionDosD, antes de saber que la necesitaba la cree por las dudas
            else:
                testsGanaNoMano.append([i,j])
    
    testsSinExito = []
    testsSinExito.extend(ejecutarTestGanaMano(testsGanaMano))
    testsSinExito.extend(ejecutarTestGanaNoMano(testsGanaNoMano))
    testsSinExito.append("False, error en linea 569")
    totalTestsLen = len(testsGanaMano) + len(testsGanaNoMano)
    
    print(" ========== Tests que fallaron", len(testsSinExito), "/", totalTestsLen, "total ==========")
    for test in testsSinExito:
        print(test)
    print(" ========== Fin Tests ========== ")
    
##########################  EJECUCION DEL JUEGO  #############################################

def runProduccion():
    global ambienteProduccion   
    ambienteProduccion = True
    global logs
    logs = True
    printOrNotPrint(imagen)
    printOrNotPrint(imagen2)
    partida = Partida()
    partida.crear()

if __name__ == "__main__":
    if args.test:
        runTests()
    else:
        runProduccion()