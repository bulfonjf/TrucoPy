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

class EstadoTruco(IntEnum):
    nosecanto = 1
    truco = 2
    retruco = 3
    valecuatro = 4

class RespuestaSiNo(IntEnum):
    si = 1
    no = 2


def make_french_deck():
    return [Carta(14, "Espada", "Uno de"), Carta(9, "Espada", "Dos de"),Carta(10, "Espada", "Tres de"), Carta(1, "Espada", "Cuatro de"), Carta(2, "Espada", "Cinco de"), Carta(3, "Espada", "Seis de"),Carta(12, "Espada", "Siete de"), Carta(5, "Espada", "Sota de"), Carta(6, "Espada", "Caballo de"), Carta(7, "Espada", "Rey de"), Carta(13, "Basto", "Uno de"), Carta(9, "Basto", "Dos de"),Carta(10, "Basto", "Tres de"), Carta(1, "Basto", "Cuatro de"), Carta(2, "Basto", "Cinco de"), Carta(3, "Basto", "Seis de"),Carta(4, "Basto", "Siete de"), Carta(5, "Basto", "Sota de"), Carta(6, "Basto", "Caballo de"), Carta(7, "Basto", "Rey de"), Carta(8, "Copa", "Uno de"), Carta(9, "Copa", "Dos de"),Carta(10, "Copa", "Tres de"), Carta(1, "Copa", "Cuatro de"), Carta(2, "Copa", "Cinco de"), Carta(3, "Copa", "Seis de"),Carta(4, "Copa", "Siete de"), Carta(5, "Copa", "Sota de"), Carta(6, "Copa", "Caballo de"), Carta(7, "Copa", "Rey de"), Carta(8, "Oro", "Uno de"), Carta(9, "Oro", "Dos de"),Carta(10, "Oro", "Tres de"), Carta(1, "Oro", "Cuatro de"), Carta(2, "Oro", "Cinco de"), Carta(3, "Oro", "Seis de"),Carta(4, "Oro", "Siete de"), Carta(5, "Oro", "Sota de"), Carta(6, "Oro", "Caballo de"), Carta(7, "Oro", "Rey de") ]


@dataclass
class Carta:
    Valor: int
    Palo: str
    Nombre: str

    # STR y REPR son cuando alguien hace print(carta) se muestre solo el nombre y el palo (con un espacio en el medio)
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

    # - Crear una funcion MostrarCartas que muestres las cartas de la mano
    def mostrarCartas(self):
        print(self.Nombre)
        print(self.Mano.Cartas)

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
    
    # - Crear una funcion CrearPartida en la clase partida que le permita al usuario ingresar el nombre del jugador 1 y el nombre del jugador 2
    def crear(self):
        print("Estas creando una partida nueva")
        print("Ingresa el nombre del jugador 1")
        nombreJugador1 = input()
        print("Ingresa el nombre del jugador 2")
        nombreJugador2 = input()

        self.Jugador1 = Jugador(nombreJugador1, "Azul", Mano())
        self.Jugador2 = Jugador(nombreJugador2, "Rojo",  Mano())

        self.crearronda()

    # - Crear una funcion que actualice los puntajes de los jugadores
    def puntajes(self, puntosPrimerJugador, puntosSegundoJugador):
        self.PuntuacionJugador1 += puntosPrimerJugador
        self.PuntuacionJugador2 += puntosSegundoJugador
        self.mostrarscore()
    
    # - Crear una funcion MostrarScore en la clase partida que muestre el score del jugador 1 y el score del jugador 2
    def mostrarscore(self):
        print("Puntuacion {}: {}".format(self.Jugador1.Nombre, self.PuntuacionJugador1))
        print("Puntuacion {}: {}".format(self.Jugador2.Nombre, self.PuntuacionJugador2))
  
    # - Crear una ronda
    def crearronda(self):
        if (self.PuntuacionJugador1 <= 30 and self.PuntuacionJugador2 <= 30):
            ronda = Ronda()
            ronda.iniciar(self.Jugador1, self.Jugador2)

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
        if(not self.NoSeAceptoElTruco and (self.SiloSabeCante == cantante or self.SiloSabeCante == None) and (self.EstadoTruco != EstadoTruco.valecuatro) ):

            siguienteNivelTruco = Truco.nextEstadoTruco(self.EstadoTruco)
            print("{} queres cantar {}? 1/si 2/no".format(cantante.Nombre, siguienteNivelTruco.name))
            aceptoCantarTruco = RespuestaSiNo(int(input()))

            if(aceptoCantarTruco == RespuestaSiNo.si): # Aca se esta queriendo cantar el truco
                self.EstadoTruco = siguienteNivelTruco # Actualizo el valor de EstadoTruco al nivel que se esta cantando
                self.QuienCanta = cantante # Guardo al que canto el truco
                self.ElQueAcepta = aceptante # Guardo al que acepto el truco
                self.SiloSabeCante = aceptante # Le doy la potestad al que acepto al truco para retrucar
               
                # Muestro el canto
                print("{} canto {}".format(cantante.Nombre, self.EstadoTruco.name)) #Ej: Mauro canto retruco

                # Pregunto al otro jugador si acepta
                print("{} aceptas? 1/si 2/no".format(aceptante.Nombre))
                aceptoTruco = RespuestaSiNo(int(input())) # transformo el input del usuario en un numero, y despues en un objeto RespuestaSiNo
                
                if(aceptoTruco == RespuestaSiNo.si): # Si el aceptante acepta
                    print("quiero") # Muestro que se quiso
                    self.cantarTruco(aceptante, cantante) # aca hacemos una funcion recursiva, es decir una funcion que se llama a si misma
                else: # Si no acepta el truco
                    print("NO quiero") # Muestro que no se quiso
                    self.EstadoTruco = Truco.previousEstadoTruco(self.EstadoTruco) # Actualizo el Estado del Truco a un nivel anterior, ya que lo que se canto no se quiso, ej si no queres valecuatro, se pasa a retruco.
                    self.NoSeAceptoElTruco = True # Siempre que no se quiera el truco, el truco se termina
           
          
    @staticmethod
    def nextEstadoTruco(estadoTruco):
        proximoNivelDeTruco= {
            EstadoTruco.nosecanto: EstadoTruco.truco,
            EstadoTruco.truco: EstadoTruco.retruco,
            EstadoTruco.retruco: EstadoTruco.valecuatro
        }
        return proximoNivelDeTruco.get(estadoTruco, "Ese estado de truco no existe")

    @staticmethod
    def previousEstadoTruco(estadoTruco):
        anteriorNivelDeTruco= {
            EstadoTruco.truco: EstadoTruco.nosecanto,
            EstadoTruco.retruco: EstadoTruco.truco,
            EstadoTruco.valecuatro: EstadoTruco.retruco,    
        }
        return anteriorNivelDeTruco.get(estadoTruco, "Ese estado de truco no existe ñery")

@dataclass
class Ronda:
    Mazo: "Mazo" = None
    Truco: "Truco" = None
    
    # - Al comenzar la ronda, generar un nuevo mazo
    # - Asignarle las cartas a los jugadores
    def iniciar(self, jugador1: "Jugador", jugador2: "Jugador"):
        
        self.Truco = Truco() # Inicializo el truco
        self.Mazo = Mazo() # Inicializo el mazo (basicamente se crea el mazo)
        
        jugador1.Mano.Cartas.clear() # Elimino las cartas que tenia el jugador anteriormente en la mano
        jugador2.Mano.Cartas.clear() # Elimino las cartas que tenia el jugador anteriormente en la mano
        
        # Este codigo se ejectua 3 veces. Reparte tres cartas.
        for _ in range(3):
            jugador1.Mano.Cartas.append(self.repartir()) # Le doy 1 carta al jugador 1
            jugador2.Mano.Cartas.append(self.repartir()) # Le doy 1 carta al jugador 2
        
        # mostar todas las cartas de cada jugador
        jugador1.mostrarCartas() # las 3 cartas del jugador 1
        jugador2.mostrarCartas() # las tres cartas del jugador 2

        # Casos de Uso
        # Primera Segunda
        # A B     A B
        # 1 0     1 0 -> ganador A   -> if jugada 2  ->no hay tercera
        # 0 0     1 0 -> ganador A   -> if jugada 2  ->no hay tercera
        # 0 1     0 1 -> ganador B   -> if jugada 2  ->no hay tercera
        # 0 0     0 1 -> ganador B   -> elif if jugada 2 ->no hay tercera
        # 1 0     0 0 -> ganador A -> else jugada 2      ->no hay tercera
        # 0 1     0 0 -> ganador B -> else jugada 2      ->no hay tercera
        # --      ---------------------------------
        # 0 1     1 0 -> empate, va a tercera elif else jugada 2
        # 1 0     0 1 -> empate, va a tercera elif else jugada 2
        # 0 0     0 0 -> empate, va a tercera segundo elif con primer empate jugada 2
        
        # --------- PRIMER TURNO DE AMBOS JUGADORES
        # Turno Jugador A
        self.Truco.cantarTruco(cantante= jugador1, aceptante= jugador2) # Le pregunta al jugador 1 si quiere cantar truco
        self.Truco.cantarTruco(cantante= jugador2, aceptante= jugador1) # Le pregunta al jugador 2 si quiere cantar truco
        
        if(self.Truco.NoSeAceptoElTruco) #Aca hay que diferenciar si se termino el truco pq no se acepto, no se puede cantar pq se acepto el valecuatro 

        # El truco te dice por cuantos puntos es la apuesta, es decir truco = 2 o retruco = 3
        #La ronda sabe quien gano las jugadas, por lo tanto cuando termina la ronda esta asigna los puntos a los jugadores
        cartaJugadaJugadorA = Turno().iniciar(jugador1) # Inicia el turno con el jugador 1, lo cual le muestra sus cartas y le pregunta cual quiere jugar. La funcion "iniciar" de Turno te devuelve la carta que se jugo

        # Turno Jugador B
        cartaJugadaJugadorB = Turno().iniciar(jugador2) # Inicia el turno con el jugador 1, lo cual le muestra sus cartas y le pregunta cual quiere jugar. La funcion "iniciar" de Turno te devuelve la carta que se jugo
       
        # Comparar las cartas jugadas para saber quien gano esa jugada
        segundoJugada1 = None
        PrimeraEmpate = None
        hayTercera = False
        ganadorRonda = None

        if(cartaJugadaJugadorA > cartaJugadaJugadorB): # Se compara el valor de las cartas para saber quien gano
            primeroJugada1 = jugador1
            segundoJugada1 = jugador2
            
        elif(cartaJugadaJugadorA < cartaJugadaJugadorB):
            primeroJugada1 = jugador2
            segundoJugada1 = jugador1
            
        else:
            primeroJugada1 = jugador1
            segundoJugada1 = jugador2
            PrimeraEmpate = True
            
        print("Continua {}".format(primeroJugada1.Nombre)) # Muestra en la consola el nombre del jugador que va a ser mano en el turno 2
      
        # --------- SEGUNDO TURNO DE AMBOS JUGADORES  
        # Turno Jugador A
        cartaJugadaJugadorA = Turno().iniciar(primeroJugada1) # Inicia el turno con el jugador mano, lo cual le muestra sus cartas y le pregunta cual quiere jugar. La funcion "iniciar" de Turno te devuelve la carta que se jugo

        # Turno Jugador B
        cartaJugadaJugadorB = Turno().iniciar(segundoJugada1) # Inicia el turno con el jugador segundo en el turno, lo cual le muestra sus cartas y le pregunta cual quiere jugar. La funcion "iniciar" de Turno te devuelve la carta que se jugo
        
        # Comparar las cartas jugadas para saber quien gano esa jugada
        primeroJugada2 = None
        segundoJugada2 = None

        # Si el ganador de la primera gano la segunda, entonces ya hay ganador
        if(cartaJugadaJugadorA > cartaJugadaJugadorB):
            primeroJugada2 = primeroJugada1
            segundoJugada2 = segundoJugada1
            ganadorRonda = primeroJugada2
            hayTercera = False
        # Si gana el que arranca segundo, hay que evaluar
        # si hubo un empate en la primera entonces ya hay un ganador 0- 1 -> if
        # si no hubo un empate en la primera, entonces hay tercera 1 - 1 -> else
        elif(cartaJugadaJugadorA < cartaJugadaJugadorB):
            primeroJugada2 = segundoJugada1
            segundoJugada2 = primeroJugada1
            if PrimeraEmpate == True: 
               hayTercera = False
               ganadorRonda = primeroJugada2
            else:
                hayTercera = True
        # En caso de que se empato la primera y la segunda hay tercera
        elif(PrimeraEmpate and cartaJugadaJugadorA.Valor == cartaJugadaJugadorB.Valor):
            primeroJugada2 = primeroJugada1
            segundoJugada2 = segundoJugada1
            hayTercera = True
        else:
            # aca gana el jugador que halla ganado en la primera jugada
            hayTercera = False
            ganadorRonda = primeroJugada1

        # --------- TERCER TURNO DE AMBOS JUGADORES
        # Verificar, si hubo un jugador que ya gano dos turnos entonces el tercer turno no se realiza
        if(hayTercera): # Si hay que jugar la tercer mano

            print("Continua {}".format(primeroJugada2.Nombre)) # Muestro en consola el nombre del jugador que es mano

            # Turno Jugador A
            cartaJugadaJugadorA = Turno().iniciar(primeroJugada2)  # Inicia el turno con el jugador segundo en el turno, lo cual le muestra sus cartas y le pregunta cual quiere jugar. La funcion "iniciar" de Turno te devuelve la carta que se jugo

            # Turno Jugador B
            cartaJugadaJugadorB = Turno().iniciar(segundoJugada2)  # Inicia el turno con el jugador segundo en el turno, lo cual le muestra sus cartas y le pregunta cual quiere jugar. La funcion "iniciar" de Turno te devuelve la carta que se jugo
        
            # Comparar las cartas jugadas para saber quien gano esa jugada

            if(cartaJugadaJugadorA > cartaJugadaJugadorB):
                ganadorRonda = primeroJugada2
                
            elif(cartaJugadaJugadorB > cartaJugadaJugadorA):
                ganadorRonda = segundoJugada2
                
            else:
                ganadorRonda = primeroJugada1 # TODO aca le estamos dando por ganado al que era mano en la primer jugada, pero habria que ver si tenemos que evaluar si el jugador segundo gano la primer jugada
              
        # Fin de tercero turno de ambos jugadores

        # Se muestra el ganador
        print("Gano la ronda {}, hizo {} puntos".format(ganadorRonda.Nombre, int(self.Truco.EstadoTruco))) # Mostramos quien gano la ronda, y el puntaje del estado del truco #TODO estamos dejandolo asi momentaneamente, ya que los puntos de la rondo incluirian el del envido tamb

       
    # - Crear una funcion Comenzar en la clase ronda que devuelva 3 cartas del mazo y las quite del mazo
    def repartir(self):
        carta = choice(self.Mazo.Cartas)
        self.Mazo.Cartas.remove(carta)
        if(carta in self.Mazo.Cartas):
            print("Error, la carta repartida esta duplicada en el mazo o no fue removida. Carta: {}".format(carta))

        return carta
        # cartas_jug = sample(self.Mazo.Cartas, 3)
        # for carta in cartas_jug:
        #     self.Mazo.Cartas.remove(carta)
        # return cartas_jug


    def repartirJugador1(self):
        carta = choice(self.Mazo.Cartas)
        self.Mazo.Cartas.remove(carta)
        return carta
        #print("Carta {}".format(self.carta))
    
    def repartirJugador2(self):
        carta = choice(self.Mazo.Cartas)
        self.Mazo.Cartas.remove(carta)
        return carta
        #print("Carta {}".format(self.carta))

@dataclass
class Turno:
    @staticmethod
    def iniciar(jugador: "Jugador") -> "Carta":
        print("                       ")
        print("Jugador {} comienza tu turno".format(jugador.Nombre))
        print("Jugador {} Indique que carta va a jugar? elija con el numero 1 2 o 3. ".format(jugador.Nombre))
        contador = 0
        for carta in jugador.Mano.Cartas:
            contador += 1
            print("opcion {}: {}".format(contador, carta))
        cartaAJugarIndice = int(input()) - 1
        cartaAJugar = jugador.Mano.Cartas[cartaAJugarIndice]
        jugador.Mano.Cartas.remove(cartaAJugar)
        print("{} juega la carta {}".format(jugador.Nombre, cartaAJugar))
        print("                       ")

        return cartaAJugar


##########################  EJECUCION DEL JUEGO  #############################################


# Partida
partida = Partida()

partida.crear()
