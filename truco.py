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
        print("Ingresa el nombre del jugador 2. No seas pete y pone un nombre distinto, sino va a fallar")
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
class Ronda:
    Mazo: "Mazo" = Mazo()
    # Jugador1: "Jugador" 
    # Jugador2: "Jugador"

    # - Al comenzar la ronda, generar un nuevo mazo
    # - Asignarle las cartas a los jugadores
    def iniciar(self, jugador1: "Jugador", jugador2: "Jugador"):
        
        self.Mazo = Mazo()
        
        jugador1.Mano.Cartas.clear()
        jugador2.Mano.Cartas.clear()
        
        # Este codigo se ejectua 3 veces
        for _ in range(3):
            # opcion A
            # self.repartirJugador1(jugador1)
            # o, la opcion B    
            jugador1.Mano.Cartas.append(self.repartir())
            jugador2.Mano.Cartas.append(self.repartir())
        
        # mostar las cartas de cada jugador (opcion B)
        jugador1.mostrarCartas()
        jugador2.mostrarCartas()
    
        # creamos dos variables de tipo entero (int), ambas inicializadas en 0
        contadortrucojugador1, contadortrucojugador2 = 0,0
        
    # --------- PRIMER TURNO DE AMBOS JUGADORES
        # Turno Jugador A
        cartaJugadaJugadorA = Turno().iniciar(jugador1)

        # Turno Jugador B
        cartaJugadaJugadorB = Turno().iniciar(jugador2)

        # Comparar las cartas jugadas para saber quien gano esa jugada
        ganadorJugada1 = None
        perdedorJugada1 = None
        
        hayGanador = False

        if(cartaJugadaJugadorA > cartaJugadaJugadorB):
            ganadorJugada1 = jugador1
            perdedorJugada1 = jugador2
            contadortrucojugador1 += 1
        elif(cartaJugadaJugadorA < cartaJugadaJugadorB):
            ganadorJugada1 = jugador2
            perdedorJugada1 = jugador1
            contadortrucojugador2 += 1
        else:
            ganadorJugada1 = jugador1
            perdedorJugada1 = jugador2
            
        print("Gano {}".format(ganadorJugada1.Nombre))
      
    # --------- SEGUNDO TURNO DE AMBOS JUGADORES  
        # Turno Jugador A
        cartaJugadaJugadorA = Turno().iniciar(ganadorJugada1)

        # Turno Jugador B
        cartaJugadaJugadorB = Turno().iniciar(perdedorJugada1)
        
        # Comparar las cartas jugadas para saber quien gano esa jugada
        ganadorJugada2 = None
        perdedorJugada2 = None

        if(cartaJugadaJugadorA > cartaJugadaJugadorB):
            ganadorJugada2 = ganadorJugada1
            perdedorJugada2 = perdedorJugada1
            contadortrucojugador1 += 1
        elif(cartaJugadaJugadorA < cartaJugadaJugadorB):
            ganadorJugada2 = perdedorJugada2
            perdedorJugada2 = ganadorJugada2
            contadortrucojugador2 += 1
        else:
            ganadorJugada2 = ganadorJugada1
            perdedorJugada2 = perdedorJugada1

        # 0 0 se juega tercera
        # 1 1 se juega tercera
        # 1 0 hay un ganador
        # 2 0 hay un ganador
        # Si los contadores son distintos hay un ganador
        # Si los contadores son iguales hay empate y por lo tanto se juega tercera
        if(contadortrucojugador1 != contadortrucojugador2):
            hayGanador = True
            
        if((contadortrucojugador1 == 1 and contadortrucojugador2 == 0)
        or (contadortrucojugador2 == 1 and contadortrucojugador1 == 0)
        or contadortrucojugador1 == 2
        or contadortrucojugador2 == 2):
            hayGanador = True

        print("Gano {}".format(ganadorJugada2.Nombre))

    
    # --------- TERCER TURNO DE AMBOS JUGADORES
        # Verificar, si hubo un jugador que ya gano dos turnos entonces el tercer turno no se realiza
        if(not HayGanador):
            # Turno Jugador A
            cartaJugadaJugadorA = Turno().iniciar(ganadorJugada2)

            # Turno Jugador B
            cartaJugadaJugadorB = Turno().iniciar(perdedorJugada2)
        
            # Comparar las cartas jugadas para saber quien gano esa jugada
            ganadorJugada3 = None

            if(cartaJugadaJugadorA > cartaJugadaJugadorB):
                ganadorJugada3 = ganadorJugada2
                contadortrucojugador1 += 1
            elif:(cartaJugadaJugadorB > cartaJugadaJugadorA)
                ganadorJugada3 = perdedorJugada2
                contadortrucojugador2 += 1
            else:
                ganadorJugada3 = ganadorJugada1
                contadortrucojugador1 += 1
            
                        
            print("Ganó la partida {}".format(ganadorJugada3.Nombre))
            
        # Fin de tercero turno de ambos jugadores
        else:
        # Mostrar el ganador
            if(contadortrucojugador1 >= contadortrucojugador2):
                print("Ganó la partida {}".format(jugador1.Nombre))
            else:
                print("Ganó la partida {}".format(jugador2.Nombre))
        
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
        print("que carta desea jugar? eliga con el numero 1 2 o 3")
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
