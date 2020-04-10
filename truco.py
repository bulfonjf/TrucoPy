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
<<<<<<< HEAD
from rx.subject import Subject

subject_mostrarCartas = Subject()
subject_mostrarCartas.subscribe( lambda x: print("{0}".format(x)))
=======

>>>>>>> origin/master
class EstadoTruco(IntEnum):
    nosecanto = 1
    truco = 2
    retruco = 3
    valecuatro = 4
<<<<<<< HEAD
    
=======

>>>>>>> origin/master
class RespuestaSiNo(IntEnum):
    si = 1
    no = 2
    
    


def make_french_deck():
    return [Carta(14, "Espada", "Uno de", images.image1), Carta(9, "Espada", "Dos de", images.image2),Carta(10, "Espada", "Tres de", images.image3), Carta(1, "Espada", "Cuatro de", images.image4), Carta(2, "Espada", "Cinco de", images.image5), Carta(3, "Espada", "Seis de", images.image6),Carta(12, "Espada", "Siete de", images.image7), Carta(5, "Espada", "Sota de", images.image8), Carta(6, "Espada", "Caballo de", images.image9), Carta(7, "Espada", "Rey de", images.image10), Carta(13, "Basto", "Uno de", images.image11), Carta(9, "Basto", "Dos de", images.image12),Carta(10, "Basto", "Tres de", images.image13), Carta(1, "Basto", "Cuatro de", images.image14), Carta(2, "Basto", "Cinco de", images.image15), Carta(3, "Basto", "Seis de", images.image16),Carta(4, "Basto", "Siete de", images.image17), Carta(5, "Basto", "Sota de", images.image18), Carta(6, "Basto", "Caballo de", images.image19), Carta(7, "Basto", "Rey de", images.image20), Carta(8, "Copa", "Uno de", images.image21), Carta(9, "Copa", "Dos de", images.image22),Carta(10, "Copa", "Tres de", images.image23), Carta(1, "Copa", "Cuatro de", images.image24), Carta(2, "Copa", "Cinco de", images.image25), Carta(3, "Copa", "Seis de", images.image26),Carta(4, "Copa", "Siete de", images.image27), Carta(5, "Copa", "Sota de", images.image28), Carta(6, "Copa", "Caballo de", images.image29), Carta(7, "Copa", "Rey de", images.image30), Carta(8, "Oro", "Uno de", images.image31), Carta(9, "Oro", "Dos de", images.image32),Carta(10, "Oro", "Tres de", images.image33), Carta(1, "Oro", "Cuatro de", images.image34), Carta(2, "Oro", "Cinco de", images.image35), Carta(3, "Oro", "Seis de", images.image36),Carta(4, "Oro", "Siete de", images.image37), Carta(5, "Oro", "Sota de", images.image38), Carta(6, "Oro", "Caballo de", images.image39), Carta(7, "Oro", "Rey de", images.image40) ]


@dataclass
class Carta:
    Valor: int
    Palo: str
    Nombre: str
    Imagen : "imagees"
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
<<<<<<< HEAD
    PuntajeRonda = 0
    SeTerminoElTruco = False
    
    
    @classmethod
    # la idea seria que al comienzo de la ronda se cree un objeto truco para que valla llevando la gestion del truco durante toda la ronda
    def cantarTruco(cls, cantante: "jugador", aceptante: "jugador"):
        # primero fijarse si vos podes realizar alguna accion
        if(not cls.SeTerminoElTruco and (cls.SiloSabeCante == cantante or cls.SiloSabeCante == None) and (cls.EstadoTruco < 4)):

            # primero obtiene el estado actual, le suma uno y desp obtiene el texto de ese valor
            
            seEstaCantando = EstadoTruco(cls.EstadoTruco +1 ).name
            print("{} queres cantar {}? si/1 no/2".format(cantante.Nombre, seEstaCantando))
            cantoTruco = RespuestaSiNo( int( input() ) )

            if(cantoTruco == RespuestaSiNo.si):

                cls.QuienCanta = cantante    
                cls.ElQueAcepta = aceptante  
                cls.SiloSabeCante = aceptante 
                cls.EstadoTruco += 1

                # Muestro el canto
                print("{} canto {}".format(cantante.Nombre, EstadoTruco(cls.EstadoTruco).name)) #Ej: Mauro canto retruco
=======
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
>>>>>>> origin/master

                # Pregunto al otro jugador si acepta
                print("{} aceptas? 1/si 2/no".format(aceptante.Nombre))
                aceptoTruco = RespuestaSiNo(int(input())) # transformo el input del usuario en un numero, y despues en un objeto RespuestaSiNo
                
<<<<<<< HEAD
                if(respuestaAceptante == RespuestaSiNo.si):
                    print("Quiero")
                    cls.PuntajeRonda = cls.EstadoTruco
                   # Truco.sumarpuntos(self.EstadoTruco)

                elif(respuestaAceptante == RespuestaSiNo.no and (cls.EstadoTruco == 2)):
                    print("NO quieroa")
                    cls.EstadoTruco = EstadoTruco.nosecanto
                    cls.PuntajeRonda = cls.EstadoTruco 
                    cls.SeTerminoElTruco = True
                else:
                    print("NO quierob")
                    cls.PuntajeRonda = int(cls.EstadoTruco) # TODO revisasr
                    cls.SeTerminoElTruco = True
            
            elif(cantoTruco == RespuestaSiNo.no):
                cls.SeTerminoElTruco = True
                    

    
=======
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
>>>>>>> origin/master

    @staticmethod
    def previousEstadoTruco(estadoTruco):
        anteriorNivelDeTruco= {
            EstadoTruco.truco: EstadoTruco.nosecanto,
            EstadoTruco.retruco: EstadoTruco.truco,
            EstadoTruco.valecuatro: EstadoTruco.retruco,    
        }
        return anteriorNivelDeTruco.get(estadoTruco, "Ese estado de truco no existe ñery")

@dataclass
#class EstadoRonda:
# puntosWinDeTruco = Truco.PuntajeRonda2
 #puntosWinDeEnvido = EstadoEnvido = 0
 #totalWinRonda = (puntosWinDeTruco + EstadoEnvido)

@dataclass
class EstadoEnvido:
    nosecanto = 0
    envido = 2
    realenvido = 3
    envidoenvido = 4
    envidorealenvido = 5
    envidoenvidorealenvido = 7
    faltaenvido = 30
    flor = 3
@dataclass
class Ronda:
    Mazo: "Mazo" = None
    Truco: "Truco" = None
<<<<<<< HEAD
    #Jugador1: "Jugador" 
    #Jugador2: "Jugador"
    #PuntajeTruco = 0
=======
    
>>>>>>> origin/master
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
        
<<<<<<< HEAD
        # mostar las cartas de cada jugador (opcion B)
        #subject_mostrarCartas.on_next(jugador1.Cartas)
        #subject_mostrarCartas.on_next(jugador2.Cartas)
        jugador1.mostrarCartas()
        jugador2.mostrarCartas()
=======
        # mostar todas las cartas de cada jugador
        jugador1.mostrarCartas() # las 3 cartas del jugador 1
        jugador2.mostrarCartas() # las tres cartas del jugador 2
>>>>>>> origin/master

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
        
<<<<<<< HEAD
        while ( not Truco.SeTerminoElTruco):
            self.Truco.cantarTruco(jugador1, jugador2)
            self.Truco.cantarTruco(jugador2,jugador1)
        
        cartaJugadaJugadorA = Turno().iniciar(jugador1)
=======
        if(self.Truco.NoSeAceptoElTruco) #Aca hay que diferenciar si se termino el truco pq no se acepto, no se puede cantar pq se acepto el valecuatro 

        # El truco te dice por cuantos puntos es la apuesta, es decir truco = 2 o retruco = 3
        #La ronda sabe quien gano las jugadas, por lo tanto cuando termina la ronda esta asigna los puntos a los jugadores
        cartaJugadaJugadorA = Turno().iniciar(jugador1) # Inicia el turno con el jugador 1, lo cual le muestra sus cartas y le pregunta cual quiere jugar. La funcion "iniciar" de Turno te devuelve la carta que se jugo
>>>>>>> origin/master

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
<<<<<<< HEAD
            
        print("Gano la ronda {} e hizo {} puntos".format(ganadorRonda.Nombre, Truco.PuntajeRonda))
            
=======
        print("Gano la ronda {}, hizo {} puntos".format(ganadorRonda.Nombre, int(self.Truco.EstadoTruco))) # Mostramos quien gano la ronda, y el puntaje del estado del truco #TODO estamos dejandolo asi momentaneamente, ya que los puntos de la rondo incluirian el del envido tamb

       
>>>>>>> origin/master
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

<<<<<<< HEAD
          
              
   

class Turno:    
    @staticmethod
    def imprimirmano(jugador : "jugador"):
        manoimpresa = []
        contador = 0
        for carta in jugador.Mano.Cartas:
            contador += 1
            manoimpresa.append("opcion {}: {}".format(contador, carta))
        print(manoimpresa)    
=======
@dataclass
class Turno:
>>>>>>> origin/master
    @staticmethod
    def iniciar(jugador: "Jugador") -> "Carta":
        print("                       ")
        print("Jugador {} comienza tu turno".format(jugador.Nombre))
        render.imprimirmano(jugador)
        print("Jugador {} Indique que carta va a jugar? elija con el numero 1 2 o 3. ".format(jugador.Nombre))
        
        
        
        cartaAJugarIndice = int(input()) - 1
        cartaAJugar = jugador.Mano.Cartas[cartaAJugarIndice]
        jugador.Mano.Cartas.remove(cartaAJugar)
        render.dicguardador()
        render.guardar(render.contadorfila, render.contadorcaract1, render.contadorcaract2, 1, cartaAJugar.Imagen)
        render.unirdic(render.guardador["diccionario1"], render.guardador["diccionario2"], render.guardador["diccionario3"])
        render.printear(render.store)
        render.guardador = {}
        print("{} juega la carta {}".format(jugador.Nombre, cartaAJugar))
        print("                       ")

        return cartaAJugar
 

 
@dataclass
class images:
    
    imageA = """A  `-------------------------------:   B
   -:/:-.//:`     .`-----..        +`   
   --.-.yy//o:     .+//+o.         /`   
   --   yhs-:s:   `///-/:          +`   
   --   :hy/-/s.`-++oo:/+.         /`   
   --    /sy:-+o+ooos++::.         /`   
   --     :hs::yosyo+/+os/-        /`   
   --      /hs:oyyyssossys+:    `  /    
   --    `:oshs/yyysssosoy++/-.::. /`   
   --  ``:ossohyodhsss+o+sssys+/.. /    
   --  //ooo+syhsydhss+oooyyds-:   +`   
   -- `++/oosso:o+o//+o//+syy:.-   /    
   -- .sssosoh--::-+yyos/oyho-`:   +    
   --  soos/yo../dhsyy+y++sy+- -   +    
   -- `+y++os/:`:dhyhs/y+osy/..-   /`   
   -- :hoyos+.-`:hysos+s+osy+`.-   /`   
   --`oysyo/y-- -hssoy+o+o+y/.+:   /`   
   -- -soo+oy/:.:ysoos+s+o/s+s+-   /`   
   --  `-+oss////hyooy+o+o/+yo+-   /`   
   -:    `+oo:///yy++hoo/++oss:.   /`   
   .:     -ss/.-/yy++yoo++o+/:+.   /`   
   .:     `o+hs+-dhsohoo+++s/:/`   /`   
   .:      ++sosyhyyyyyhssyyo+:    /`   
   .:     -syosyhsso/++hoss+/o:    /`   
   .:   .-//+:+.:so:.:`oo/-.-:.    /`   
   .:  .//::-`..:so.+/:sso/.`      /`   
   .: `-/::+oooo+yyssssyysso/`` .::/`   
   `/.......-:o+/:-.----........::/+`   
Y   ````````````````````````````````   Z"""

    image1 = """                                        
                                       .
     ``````       `````      ` ````    -
     . /                          .    -
     - .-..-:-``   `.``.     ` `` .    -
     -  -/oo/soo:. `.-/y//++o+::: .    -
     -  -hss .+sso/`  `-:-`-sh-`` .`   -
     -  +sss  .+ooy+ ` `  ./.y`   .`   -
     .  -+/s/.--+oss/++:`.+./+    .    -
     -   `-o+/osoy++o+/../:/s/    .    -
     -     ```::-oy/h+``::-ys+.:: .    -
     .         ` -h/sy.o+.o+o++yy`.    -
     -          .oos+sh+``s-++s-o:.    -
     -        -//:+s++d.  o+://`+:.    -
     .       `//  /os+h:  +s``:/- .    -
     -       .+: `soy:ys`--- .+`  .    -
     -      `/o:.+++ssoho/`  -/`  .    -
     -     `+o-.++`-sd+y+   -y`   .    -
     .     -/- .o+  oy:ss`  :/-   .    -
     -   `/+-  `:o--yyo+y:  -o-   .    -
     -   :o+    `oo+o+sh+s-       .    -
     -   ://`    `.-` /o+-::.`    .    -
     .    `            ./+--::.   .    -
     .                  `:+//+: ``.    -
     .                    `.:-` :`.    -
     `               ``      ``````    -
                                       -
  `...................................-`"""    
    image2 = """                                        
                                       .
      ````       ``````      ``````    -
    `.`:  `.`               -     .    -
    `... -o+h+-`           :+:    .    -
    `.  `+yyho-/:`        `+/o    .`   -
    `.  `/hoy+::::        `//o    .`   -
    `.   `ysy/yo/:        `//o    .`   -
    `. `-:sssos+:`        `//+    .`   -
    `. -o+ssso:`          `//o    .`   -
    `. ```yoo-            `//+    .`   -
    `.    +//`            `//o    .`   -
    `.    +//`            `//+    .`   -
    `.    +//`            `//o    .`   -
    `.    +//`            `//o    .`   -
    `.    +//`            `//o    .`   -
     .    +//`             /:o    .`   -
    `.    +//`            `//o    .`   -
     .    +//`           `:ssh-:. .`   -
     .    +//`         `-/osos++- .`   -
     .    +//`        `/ososss-`  .`   -
    `.    +//`        :-++/soy.   .`   -
     .    +//`        .::.+yoyo.  .`   -
     .    +//`         .::/hsy/   ``   -
     .    .+-             :+//` -..`   -
     `    ``        ```      ```.`.    -
                                       -
  `...................................-`"""
    image3 = """                                        
                                       .
     ``````      ``````      ``````    -
    `-`:` ``       ``      ``     .`   -
    `.`-`:sso/`   `+o`   `:sso/`  .`   -
    `.  -sdhh//:. :/o:   -yhhh//:..`   -
    `.  -yyyy+./+`:/o:   -yyys+.++.`   -
    `.   /yysooo/.:/o:    /yyso+o+.`   -
    `. `:+syssoo- :/o:  .:+sssyoo-.`   -
    `.`/oohsso-`  :/o:  +oohss+-` ``   -
    `. .`/yoo`    :/o:  .`/yoo`   .`   -
    `.   `s:+     :/o:    .o//    ``   -
    `.   `s:+     ::o:    .o:/    ``   -
    `.   `s:/     ::o-    .o:/    .`   -
    `.   `s:/     ::o:    .o:/    ``   -
    `.   `s:/     ::o:    .o:/    .`   -
    `.   `s:/     ::o-    .o:/    ``   -
    `.   `s:/     :/o:    .o:/    ``   -
    `.   `s:/    -ssys-:` .o:/    ``   -
    `.   `s:/  -:ososo+/` .o:/    ``   -
    `.   `s:/ :soyosso.`  .o:/    .`   -
    `.   `s:/ ++:o+sso`   .o:/    ``   -
    `.   `o:/ :/.:sysh/   .o::    ``   -
     .   `s:/  .:/shyo-   .o/:    ``   -
    `.    :/     .-//.     :/   -..`   -
     .    ``   `    ```      ```.`.`   -
                                       -
  `...................................-`"""
    image4 = """                                        
                                       .
     ``````      ``````      ``````    -
    `..+ `                    `   .`   -
    `. `.+/`                 /+.  .`   -
    `.   +o/``            ``:s+   ``   -
    `.  `/oso/.          .:oso/.  .`   -
    `.  `-/+o+            :o+/-.  ``   -
    `.     -/o`           o/:`    ``   -
     .      -/+          :+:      ``   -
    `.       .+.        `+-       ``   -
     .        ./        :-        ``   -
     .         .`       .         ``   -
     .                            ``   -
     .                            ``   -
     .         ``       .         ``   -
     .        `/        :-        ``   -
     .       .+-        `+-       ``   -
     .      ./+          -+:      ``   -
     .     ./o-           o/:`    ``   -
     -  `-:+++            -o//-.  ``   -
     .  `:oso/-          `:oso/.  ``   -
     .   :o+``            ``-o+`  ``   -
     -  `++`                 :+- ```   -
     .   `                    ` ::`.   -
     `    `` ` `     ``       ``````   -
                                       -
  `...................................-`"""
    image5 = """                                        
                                       .
     ``````       `````       ``````   -
     - -. ::                 :-    .   -
     -``  yy`               .yy`   .   -
     -  `.ss.`             `-ss.`  .   -
     . `:+sy+:`           ./oyy+:` .   -
     .   :/o:               //s-   .   -
     .   ./o`               -/s`   .   -
     .    +o                `+o    .   -
     .    //                 //    .   -
     .    :-                 /.    .   -
     .    .`           ``    -     .   -
     .    ``````....--/o/-...`    `.   -
     .    `..--:::////oy+++oo:`   `.   -
     .    ``        ``.::`   .    `.   -
     .    :-                 +`   `.   -
     .    +:                 +:   `.   -
     .    ++                ./+   `.   -
     .   ./o                -/o   `.   -
     .   :/o.               //o.  `.   -
     . `-+ss/-            .:osy/- `.   -
     .  .:oo-.            `-/so:` `.   -
     .   .ss                :ss ```.   -
     .   `:-                ./: :.`.   -
     `               ``      ```````   -
                                       -
  `...................................-`"""
    image6 = """                                        
                                       .
     ``````      ``````      ``````    -
     -::``-.       ..       `-    .    -
     .`` :so      `ss`      +o-   .    -
     .  `:o+`     .oo.     `+o:`  .    -
     . ./oss/:  `/oss+/`  -+ss+/. .    -
     .  `++s`    `:/s/`   `.+++`  .    -
     .   //o      ./o.      ++:   .    -
     .   -//      `/o`      /+.   .    -
     .   `o-       /+       -o    .    -
     .    o`       ::       .+    .    -
     .    :        .`       `-    .    -
     .                            .    -
     .                            .    -
    `.    -        -`       `.    .    -
    `.    o`       /.       ./    .    -
    `.   .+.       /:       -+    .    -
    `.   :/-      `/+       /o    .    -
    ``   ///      -/o`     `/o-   .    -
    ``  `/+o      //o.     -/+/   .    -
    `` -+sso/.  ./+ss+-   :+ss+:` .    -
    ``  `+o:`    `-o+.    `.oo.`  .    -
    ``   +o:      -oo       ss    .    -
    ``   .-`      `-.       -- `--.    -
    ``    ``  ``    ``       ``````    -
                                       -
  `...................................-`"""
    image7 = """                                        
                                       .
     ``````      ``````      ``````    -
    `.:. `-`       --       `-`   -    -
    `..  +o/      .ss`      +s:   -    -
    `.  `+o/`    `-so.     `+o:`  -    -
    `. -+sys+-  `/+yyo/`  :+sso+. -    -
    `.  `o/+     `/o/:`    `s/+`  -    -
    `.   +//      -o/.      o//   -    -
    `.   //-      `o/       +/-   -    -
    `.   -+`       +:       :o`   -    -
    `.    o        /-       .+    -    -
    ``    -        .`..`     -    -    -
    ``   ```....---::oo/--:-`     -    -
    ``  ``...---:::::ss+//+:.     -    -
    ``    `        ``--`     `    -    -
    ``   `o        /-       `+    -    -
    ``   -+`       +:       -+    -    -
    ``   //-      `+/       +/.   -    -
    ``   +/:      -+/`      o::   .    -
    ``  .o/+      ++/-     .s//   -    -
    `` -+sso/.  ./oss+:`  :+yso/. .    -
    ``  `+o:`    `-oo.    ``oo:`  -    -
    ``   +o:      -oo       oo-   .    -
    ``   .-`       -.       .-  :`-    -
    ``    `         ``       `````.    -
                                       -
  `...................................-`"""
    image8 = """                                        
                                       .
                  .-```                -
    `.:-:``--`   -os//+- `````````-    -
    `...` ./o   +ssso/o:          -    -
    ``    -//   +/+:o/-           -    -
    ``    :/- `-+o:-++:.          -    -
    ``    /o-/+oyhyssys+/`        -    -
    ``   `/soo/oyyoys/y/ss`       -    -
    ``   .:sssyo/y:yy+y/hs+       -    -
    ``   -+ysyys:yyyyhyshoo.      -    -
    ``  `+ysy+osyhhhodhs/ss-      -    -
    `` -+oyoo+sssy/ssosohys/      -    -
    ``.:y/s/oos++o./o:+/ooo/      -    -
    `.  /o-`:.-/so/oo/oo/-..      -    -
    ``  ``    :hsyyysyysy/        .    -
    `.        /ysyyhyysso-        -    -
    `.         :o+osoo:o          -    -
    ``         `y+o-s++:          .    -
    `.         `y+s:y+o-          -    -
    `.         `s/s-s++.          -    -
    ``          +/+`/+/           .    -
    ``          +o: ++:           -    -
    `.         -///.:---.`        .    -
    `.  ``..-::-.:---::---..` .-:-.    -
     ````````..`   ` ``  `    ````.    -
                                       -
  `...................................-`"""
    image9 = """                                       .
      .````      `````      ``````     -
     `.+ +        `--`          `.     -
      .` -.     :+oys+`         `.     -
      -  ./:`  /yooh+.          `.     -
      -   .//. `++:y+.           .     -
      -    `-/-/hhyhyhy+-`       -     -
      -      .oyhyyyymshds:`-..` .     -
      -      .yssdhsshoydosyyssso+-    -
      -      +syohsydmhddhddhdyos+s`   -
      -     .ydhhy+hNhdyhhhyshyooo:`   -
      -  ./+yhddddyomhy+:-:/sds/+-     -
      - odhyyshhhhhyyhhso+o/yhso--     -
      -.ddhyysshyhdsyhsyhysoy+:- -     -
      -`hhhysyossyyohhsyyyy/+s   -     -
      - oyyyssysossodhsoyssyss:` -     -
      -`shhsoshsosyydmsoysoyyhs+`-     -
      - -sso++ddhssyssssyy+y+:+/.-     -
      - -/-. ./+-       `-/. -+` .     -
      - ::.  .:-`     `./:``:+`  -     -
      -  /-   `:/`    +/.  ::`   .     -
      -  .+`    -/:.             .     -
      -   /::```.-:oo....``  `-...     -
      - `.:/s:.-..``.``````  ..-`.     -
      .    ``   `           ``````     -
                                       -
  `...................................-`"""
    image10 ="""                                        
                                       .
     ``````       `````      ``````    -
     --.--   `-  `-:+://          ``   -
     ..`.`  `+/   yhsyyo          ``   -
     -      /o.  -oo++oy+         ``   -
     -     -+/ `.sso//+ho:        ``   -
     -    `:/./shmdho++oyy+:`     ``   -
     -    --/syo+yhydyssyssys-    ``   -
     -   .:+yo-:--hsyyhhysyhys`   ``   -
     -  `+o+:--s:-/++ooo+oysoh+   `.   -
     ---+yh+-:+dmhyysyhysymo:+h.  `.   -
     --+yddhy+dmhhhhh+yodyNmo-+.  `.   -
     - oydhshmdd-oyy:.:-+:+myoh.  `.   -
     - .shosyshs:sss:....::dysy+` `.   -
     -  ..`/:+o::ssy+/.-.:-hh/+y+``.   -
     -     /-/ssoyyyssoo/osds+////`.   -
     -     /-+ssshyysyososms+:-..:-.   -
     -     ::/yhydydys+sssmo----:/+.   -
     -     `//hyydyhysosssdh--:/+oo.   -
     -      :oyyhdhhyyooooyhs/++sy/.   -
     -      `syhshhysy+//+ysdooyso`.   -
     -    ``+ysdhyyshhoossdh+ooo/` .   -
     -    :+o++osys:--+hy::--  ``.`.   -
     -   ````-/+/:-...-+oo--.``-`/ .   -
     `               ``  `    ``````   -
                                       -
  `...................................-`"""
    image11 = """                                        
                                       .
    `.````    ````    ````    ````.    -
    `.:`  +-                      -    -
    `..  ody:                     -    -
    `.   +y+++.                   -    -
    `.    .s+/y+                  -    -
    `.     .yo+yo.`               -    -
    `.      os/+hss`              -    -
    `.     .sho:syyo:             -    -
    `.      /hho/oyhm:            -    -
    `.       -sh+-oy+s..          -    -
    `.      ./+do::/-soo.         -    -
    `.       /`ys--+oyys          -    -
    `.        `yys++:+hh/-        -    -
    `.         -sds+..ohdy:       -    -
    `.          `sso:.-s+/o`      -    -
    `.          `sdy+-+/.-o`.`    -    -
    `.           .ddo+o:+yyoo/`   -    -
    `.          .+osyo::-yyhs-    -    -
    ``          . `+yho--/yyhy-   -    -
    ``             `yhsoo-+yyy-   -    -
    ``              `-yhs--oys`   -    -
    ..                .os/./o-  - -    -
    `.                  .-.`   `: -    -
     `         `      ```     `````    -
                                       -
  `...................................-`"""    
    image12 = """                                        
                                       .
    `````     ````    ````    ````.    -
    ```:  .-:-`             .-    -    -
    ``.. oooshy-`         `yy.    -    -
    ``  /ys:+shh+-        /ss     -    -
    ``  yys//syd/         /sh     -    -
    `.  oys/:yyh-         ssh-    -    -
    `.  sys/+hdh`        /hsyo    -    -
    `.  :yys+yhy        `od+os    -    -
    `.  `hy//sy/        /sh/+d    -    -
    `. `:ys//sh-        `yy/+d+`  -    -
    `.`/sdy//hys        `dsssdy.  -    -
    `. `.yh//sh-        .mo:ohs   -    -
    `.  `yy+/sh         :do-/ds.` -    -
    `.  -yhossy        `yhy-/yhy/ -    -
    `.  .+h++yo         /ds-:os:  -    -
    `.   `d/+ho-        sho-:yy   -    -
    `.    h+od/`       .hdy/ssy-  -    -
    `.    yyyy-        :hmho+syo  -    -
    `.    :hh+         +hhs::oh/  -`   -
    `.    .hy-        `+dyo::oh+  -`   -
    `.    `ys-        :odho::oh-  .`   -
    `.    -yo`         `:hy//s+ .`.`   -
     .    -.             `::-. `:`.`   -
     .`               ````    `````    -
                                       -
  `...................................-`"""
    image13 = """                                        
                                       .
     .````    ````    ````    ````.    -
    `-`+``        -:::`           -`   -
    `-`./s      `yysshh:     `y-  -    -
    `-  hy:     :ms:/ydh    `sN:  -`   -
    `-  -yo/`  `ydh::hdm -.:sso`  -`   -
    `-   -soy:  shh+smds+ydy++    -`   -
    `-    :hoy:/ys+/yddshmhoo`    -`   -
     -    `:y//ydds/ydmmhohd      -`   -
     -      hh-:ydhyyhmy:odo      -`   -
     -      +sh/-+hhhd+-ommo      -`   -
     -       -ym+-oddo:ydhy+      -`   -
     -      -yys+:/dy+/ss/+.      -`   -
     -      /ds/osss+oso-.`       -`   -
     -      :dhsdshd::/s:o-       -`   -
     -      `ymho/hmdo:-syy`      -`   -
     -    `-omy+yhNhhyo--:s:      -`   -
     -  `.hmy+-+dmNdohso..-/+`    .`   -
     -`/sdhs--oh/odd+d+hs.../s:.  -`   -
     -`:hy/--ohh`/hhsdshhs-..+yy. -`   -
     -`yy:-:sy-`  -dssos:ys+..:y` .`   -
     -+ms+oyy.    `yd+.+.+sy-.-/- .`   -
     -`/+oho`       -+     -//:-``.`   -
     -                          o`.`   -
     .                ````     ```.    -
                                       -
  `...................................-`"""
    image14 = """                                        
                                       .
     `````    ````    ````     ````    -
    `.`:`                         .`   -
    `. -.://:`            .-::-.  .`   -
    `. .ysyysy/`         /so/++s. .`   -
    `. :yso+osy+        :y+-:/+y. .`   -
    `.  +yo/-oy+       +so-.-+so  .`   -
    `.  `yyy//so       -y/.:o+`   .`   -
    `.   .-/soo+       :o-/:.     .`   -
    `.      .+sy.     `o//`       .`   -
    `.        /ys-    +s+`        .`   -
    `.         :os/   +y-         .`   -
    `.           ``   `:          .`   -
    `.          `                 .`   -
    `.         :o.  .::-`         .`   -
     .         +s+   -syo`        .`   -
     .        :+s`    `+so`       .`   -
    `.      .:/+:      `yos/``    .`   -
    `-    .+/-:y        yo/ss+/   .`   -
     -  -+o/.-os:       yo/:oyy`  ``   -
     - -yo:-./y+-       oyo::oys` ``   -
     - /o+o:/so`        +ysssssh. .`   -
     . .++++o/`          .ossss/  ``   -
     .   ```               `.` `+```   -
     .`   ```   `     ````    ``.`.`   -
                                       -
  `...................................-`"""
    image15 = """                                        
                                       .
     `````     ````   ````     `````   -
     . .-        `.                .   -
     . ``        os.`/o+-          .   -
     .         `/so`  .+o/`        .   -
     .       `-oso`     ////.``    -   -
     .     -+o+os`       o-:+oo-   .   -
     -  ./ss+:+y+        ++-.:os-  .   -
     .  syo+:+ys/        `y+--:+s: -   -
     . .yssooso`          /o++o/s: .   -
     .  :/+++-`       `    `-///-  .   -
     .            ``.//+//:::-`    .   -
     .     `-/:::::::---.--:://`   .   -
     .`   `:/:-....--:----://:/    -   -
     .`              `..-//-..`    .   -
     .` -///:.            `:+oo+/` -   -
     .`.s/+++o+`         `oso+sys/ -   -
     .``so:--/s-        /oy+:/osy` -   -
     `` .+s/.-/o        /y+:+os:-  -   -
     ``  `+o+:-o`       ss+o/-     .   -
     `.     `://+`     +oo-`       -   -
     `.       `:o+-`  oy+`         -   -
     `.         ./+/. ss         ``.   -
     `.               ``        `:.-   -
      .     ``  ``     ```     `````   -
                                       -
  `...................................-`"""
    image16 = """                                        
                                       .
    `````     ````    ```     `````    -
    .:-.   `               ``     .    -
    `.` :+oo+/   -o:`    :+o+o/   .    -
    `` :s+/o/s/   syo   -s+/o/s/  .    -
    `` /s+.-:ss`  /ss   :y/.:-ss  .    -
    `` +yo../y.   +ss-  /y+..:s.  .    -
    `` :+s-.o/   -y+oy.`-/s--+/   .    -
    ``  `o::/   `yo:+ys/  +/:/    .    -
    ``   .o+.  `oyo-:oh-  .o+-    .    -
    ``    yo-  `yss+/oy:   so-    .    -
    ``    +so   -ysssso`   /oo    -    -
    ``     .-`   .:/:-`     `-`   .    -
    ``   :-`     .://:`   /-`     .    -
    ``   -ys.   :s/+o+o`  /ys`    .    -
    `.    ss/   ss:://y+  `sy-    .    -
    `.    soo   ss:.-/s-  `so+    -    -
    `.   .s+y: `os+.-o/   :soy.   -    -
    `.  .yo:sy/.`:s-//   -y+:ss+  -    -
    `. `os+-+yy.  o:o`  `ss+-oys  -    -
    `. +ys+:/oh`  :oo   oys+:oss  .    -
    `. `ysyyoss`  .ys.  .hsyyos+  -    -
    `.  .oooo+.    .//   -osoo:`.-.    -
    `.                          -..    -
     `                ````    `````    -
                                       -
  `...................................-`"""
    image17 = """                                        
                                       .
     .````     ```    ````     `````   -
     -`:` ...`    ``       `..`   `.   -
     -``.o+ooo`   .y+`    /o+oo/  `.   -
     -  /s://so    oy-   `y+:++y. `.   -
     -  +y:.:s-    os+   `yo.-+o` `.   -
     -  :o+.++    -s+h-` ./s-:s.  `.   -
     -   `s-+    .yo:sy/   +/+.   `.   -
     -    /+:   `oy+:oy/   `so    `.   -
     -    -s+    +yysoy:    ss.   `.   -
     -     ./`   `/+o+-     `::   `.   -
     -           `./++///::-`     `.   -
     -   `-/:-::::::-----:://`    `.   -
     -  `:+/--...-------://:/`    `.   -
     -            ``..://:-.`     `.   -
     -    /-     `-///.    /-`    `.   -
     -    +y/    +s/o+s.   :yo    `.   -
     -    -so    so-::y/   `yy    ``   -
     -    /oy.  `os-.+o    -ss:   `.   -
     -   :s/ss:  .o/-o`   .s/+y/` `.   -
     -  .yo:+ys`  `o/-   `ss:/yy` `.   -
     -  +yo++ss    oo.   :hs+/sh  `.   -
     -  `ssyss:    :s+    osyss+ .``   -
     -    ---`       .     .--` --``   -
     .                ````    ```..`   -
                                       -
  `...................................-`"""
    image18 = """                                        
                                       .
     `````    ````    ````     ````    -
     -`::/   :::../::`            ``   -
     -`.-`  +y:ooo////+`          ``   -
     -      os:sos:ss+o+          ``   -
     -      :h/so+:o/./o          ``   -
     -      .h/ss+so:-++:--`      ``   -
     .      `sossoyssosso/++      ``   -
     -       :yyhs+sysos+oo-      ``   -
     -      `/sohyyyyyhys::.      ``   -
     -      .s:+dyydsysyo:-.      ``   -
     .      `s+ydsoysooy+--`      ``   -
     -       -/hs+/yoooso::.      ``   -
     .        :shsshyssyh+s-      ``   -
     .        +shyshyyyys:+`      ``   -
     .        `.+:-+/::+`:-       ``   -
     .          -/./+-.:          .`   -
     .          `o//o::.          ``   -
     .           s+oyoso          .`   -
     .           /+/hs+s          .`   -
     .           `s++oo+          .`   -
     .            oo:+o:          ``   -
     .      ```.:+ssyhs+....``    .`   -
     .   `..-..:::-.`-ss:`    :.:/``   -
     .   ``` ` `      .--`    .``..`   -
                                       -
  `...................................-`"""
    image19 = """                                        
                                       .
     `.```    ````   ````    `````     -
     .-+--                      `.     -
     ..``.o++-   :-.:           `.     -
     .`  .dyyy:  .o+h:          `.     -
     .`  `hosss`-oy++s          `.     -
     .`   .ho+s+osy+yh/`        `.     -
     .`    +y/shyhyyhhdy:`      `.     -
     .`     -y+yhyssyodhho....` `.     -
     .`    `/yssmyhhyyhddyyyssoo:.     -
     .`   /ossshmmymydhdddhddhoshs     -
     .`   `//ohhoyhymdyyhdhhmhysys     -
     .`.+osyyyhmydyhmmssss+hmhss+`     -
     `+hdsyosyhdyhoydhhho//ddhy:.`     -
      ddhyyosyhys+/yhyyysyydo+- ``     -
     `yhhhyyoyyhy/yhyoysoyhho   ``     -
     -ohyyhyshhhdddhs+hyoyssh-  ``     -
     -ysdysyhhhdddysosyyoyyoys. ``     -
     -+/o/o+ymdhsoy:.:++so+--+o```     -
     .-s:/. oo+``..`    `y:  /+ ``     -
     .`o+`  :o/         `h` `o- ``     -
     - `s-   `o+`      `/s  os  ``     -
     .  :o.   `/++-````:o-  -` ```     -
     - `-+ys-----+s:.....`   /`/``     -
     `  ````` ` `    ````    .`..`     -
                                       -
  `...................................-`
"""
    image20 ="""                                        
                                       .
     `````    ````    ````    `````    -
    `.+.:..-`    . -`-```         .    -
    `.` `ohs+:   `so+oo:`         .    -
    `.   ohhy+y. `y+/oy/          -    -
    `.   -dhoo++`oo/:os+:         -    -
    `.    :yyys+dh+++o+ys/        -    -
    `.     `ohy+ymsyhysyho/`      -    -
    `.     -oddysmoosyssss/+.     .    -
    `.   -:oooydsysooyysoh+oys+o+`.    -
    `.  `+++++shdosyyhhhyddhdddy:`.    -
    `.  /+o//yy:hh/sdshysdmydm+-- .    -
    `.  :s/:+ss+smhhhoooohddyo-   -    -
    `.  :s+++hs:ydsdy+sooshy:+-   -    -
    `. :+s/ooh:/hhoso+sssyd:/o    .    -
    `. `///ooho+hhsyooyyyhd+ho    .    -
    `.   ./ooyyhhdyhsyshydhdh+    .    -
    `.     /ys:shdddodhhhdhoys    .    -
    `.     .h/:+yhhdyydysdh/os    .    -
    `.      s-:oyyhdsymyoddyms-   .    -
    `.    -/y-+ohodd+ymoohhsd++`  .    -
    `.  `+sodhyddsmmohmyhmmds+s+:..    -
    `.-/+oysso+oyys/::++oo/.-..---.    -
    `.   `....---.`           .:`/.    -
     `                ````    `.```    -
                                       -
  `...................................-`
"""
    image21 = """                                        
                                       .
    `.````    ````    ````    ````.    -
    `.:`  +-                      -    -
    `..  ody:                     -    -
    `.   +y+++.                   -    -
    `.    .s+/y+                  -    -
    `.     .yo+yo.`               -    -
    `.      os/+hss`              -    -
    `.     .sho:syyo:             -    -
    `.      /hho/oyhm:            -    -
    `.       -sh+-oy+s..          -    -
    `.      ./+do::/-soo.         -    -
    `.       /`ys--+oyys          -    -
    `.        `yys++:+hh/-        -    -
    `.         -sds+..ohdy:       -    -
    `.          `sso:.-s+/o`      -    -
    `.          `sdy+-+/.-o`.`    -    -
    `.           .ddo+o:+yyoo/`   -    -
    `.          .+osyo::-yyhs-    -    -
    ``          . `+yho--/yyhy-   -    -
    ``             `yhsoo-+yyy-   -    -
    ``              `-yhs--oys`   -    -
    ..                .os/./o-  - -    -
    `.                  .-.`   `: -    -
     `         `      ```     `````    -
                                       -
  `...................................-`"""    
    image22 = """                                        
                                       .
    `````     ````    ````    ````.    -
    ```:  .-:-`             .-    -    -
    ``.. oooshy-`         `yy.    -    -
    ``  /ys:+shh+-        /ss     -    -
    ``  yys//syd/         /sh     -    -
    `.  oys/:yyh-         ssh-    -    -
    `.  sys/+hdh`        /hsyo    -    -
    `.  :yys+yhy        `od+os    -    -
    `.  `hy//sy/        /sh/+d    -    -
    `. `:ys//sh-        `yy/+d+`  -    -
    `.`/sdy//hys        `dsssdy.  -    -
    `. `.yh//sh-        .mo:ohs   -    -
    `.  `yy+/sh         :do-/ds.` -    -
    `.  -yhossy        `yhy-/yhy/ -    -
    `.  .+h++yo         /ds-:os:  -    -
    `.   `d/+ho-        sho-:yy   -    -
    `.    h+od/`       .hdy/ssy-  -    -
    `.    yyyy-        :hmho+syo  -    -
    `.    :hh+         +hhs::oh/  -`   -
    `.    .hy-        `+dyo::oh+  -`   -
    `.    `ys-        :odho::oh-  .`   -
    `.    -yo`         `:hy//s+ .`.`   -
     .    -.             `::-. `:`.`   -
     .`               ````    `````    -
                                       -
  `...................................-`"""
    image23 = """                                        
                                       .
     .````    ````    ````    ````.    -
    `-`+``        -:::`           -`   -
    `-`./s      `yysshh:     `y-  -    -
    `-  hy:     :ms:/ydh    `sN:  -`   -
    `-  -yo/`  `ydh::hdm -.:sso`  -`   -
    `-   -soy:  shh+smds+ydy++    -`   -
    `-    :hoy:/ys+/yddshmhoo`    -`   -
     -    `:y//ydds/ydmmhohd      -`   -
     -      hh-:ydhyyhmy:odo      -`   -
     -      +sh/-+hhhd+-ommo      -`   -
     -       -ym+-oddo:ydhy+      -`   -
     -      -yys+:/dy+/ss/+.      -`   -
     -      /ds/osss+oso-.`       -`   -
     -      :dhsdshd::/s:o-       -`   -
     -      `ymho/hmdo:-syy`      -`   -
     -    `-omy+yhNhhyo--:s:      -`   -
     -  `.hmy+-+dmNdohso..-/+`    .`   -
     -`/sdhs--oh/odd+d+hs.../s:.  -`   -
     -`:hy/--ohh`/hhsdshhs-..+yy. -`   -
     -`yy:-:sy-`  -dssos:ys+..:y` .`   -
     -+ms+oyy.    `yd+.+.+sy-.-/- .`   -
     -`/+oho`       -+     -//:-``.`   -
     -                          o`.`   -
     .                ````     ```.    -
                                       -
  `...................................-`"""
    image24 = """                                        
                                       .
     `````    ````    ````     ````    -
    `.`:`                         .`   -
    `. -.://:`            .-::-.  .`   -
    `. .ysyysy/`         /so/++s. .`   -
    `. :yso+osy+        :y+-:/+y. .`   -
    `.  +yo/-oy+       +so-.-+so  .`   -
    `.  `yyy//so       -y/.:o+`   .`   -
    `.   .-/soo+       :o-/:.     .`   -
    `.      .+sy.     `o//`       .`   -
    `.        /ys-    +s+`        .`   -
    `.         :os/   +y-         .`   -
    `.           ``   `:          .`   -
    `.          `                 .`   -
    `.         :o.  .::-`         .`   -
     .         +s+   -syo`        .`   -
     .        :+s`    `+so`       .`   -
    `.      .:/+:      `yos/``    .`   -
    `-    .+/-:y        yo/ss+/   .`   -
     -  -+o/.-os:       yo/:oyy`  ``   -
     - -yo:-./y+-       oyo::oys` ``   -
     - /o+o:/so`        +ysssssh. .`   -
     . .++++o/`          .ossss/  ``   -
     .   ```               `.` `+```   -
     .`   ```   `     ````    ``.`.`   -
                                       -
  `...................................-`"""
    image25 = """                                        
                                       .
     `````     ````   ````     `````   -
     . .-        `.                .   -
     . ``        os.`/o+-          .   -
     .         `/so`  .+o/`        .   -
     .       `-oso`     ////.``    -   -
     .     -+o+os`       o-:+oo-   .   -
     -  ./ss+:+y+        ++-.:os-  .   -
     .  syo+:+ys/        `y+--:+s: -   -
     . .yssooso`          /o++o/s: .   -
     .  :/+++-`       `    `-///-  .   -
     .            ``.//+//:::-`    .   -
     .     `-/:::::::---.--:://`   .   -
     .`   `:/:-....--:----://:/    -   -
     .`              `..-//-..`    .   -
     .` -///:.            `:+oo+/` -   -
     .`.s/+++o+`         `oso+sys/ -   -
     .``so:--/s-        /oy+:/osy` -   -
     `` .+s/.-/o        /y+:+os:-  -   -
     ``  `+o+:-o`       ss+o/-     .   -
     `.     `://+`     +oo-`       -   -
     `.       `:o+-`  oy+`         -   -
     `.         ./+/. ss         ``.   -
     `.               ``        `:.-   -
      .     ``  ``     ```     `````   -
                                       -
  `...................................-`"""
    image26 = """                                        
                                       .
    `````     ````    ```     `````    -
    .:-.   `               ``     .    -
    `.` :+oo+/   -o:`    :+o+o/   .    -
    `` :s+/o/s/   syo   -s+/o/s/  .    -
    `` /s+.-:ss`  /ss   :y/.:-ss  .    -
    `` +yo../y.   +ss-  /y+..:s.  .    -
    `` :+s-.o/   -y+oy.`-/s--+/   .    -
    ``  `o::/   `yo:+ys/  +/:/    .    -
    ``   .o+.  `oyo-:oh-  .o+-    .    -
    ``    yo-  `yss+/oy:   so-    .    -
    ``    +so   -ysssso`   /oo    -    -
    ``     .-`   .:/:-`     `-`   .    -
    ``   :-`     .://:`   /-`     .    -
    ``   -ys.   :s/+o+o`  /ys`    .    -
    `.    ss/   ss:://y+  `sy-    .    -
    `.    soo   ss:.-/s-  `so+    -    -
    `.   .s+y: `os+.-o/   :soy.   -    -
    `.  .yo:sy/.`:s-//   -y+:ss+  -    -
    `. `os+-+yy.  o:o`  `ss+-oys  -    -
    `. +ys+:/oh`  :oo   oys+:oss  .    -
    `. `ysyyoss`  .ys.  .hsyyos+  -    -
    `.  .oooo+.    .//   -osoo:`.-.    -
    `.                          -..    -
     `                ````    `````    -
                                       -
  `...................................-`"""
    image27 = """                                        
                                       .
     .````     ```    ````     `````   -
     -`:` ...`    ``       `..`   `.   -
     -``.o+ooo`   .y+`    /o+oo/  `.   -
     -  /s://so    oy-   `y+:++y. `.   -
     -  +y:.:s-    os+   `yo.-+o` `.   -
     -  :o+.++    -s+h-` ./s-:s.  `.   -
     -   `s-+    .yo:sy/   +/+.   `.   -
     -    /+:   `oy+:oy/   `so    `.   -
     -    -s+    +yysoy:    ss.   `.   -
     -     ./`   `/+o+-     `::   `.   -
     -           `./++///::-`     `.   -
     -   `-/:-::::::-----:://`    `.   -
     -  `:+/--...-------://:/`    `.   -
     -            ``..://:-.`     `.   -
     -    /-     `-///.    /-`    `.   -
     -    +y/    +s/o+s.   :yo    `.   -
     -    -so    so-::y/   `yy    ``   -
     -    /oy.  `os-.+o    -ss:   `.   -
     -   :s/ss:  .o/-o`   .s/+y/` `.   -
     -  .yo:+ys`  `o/-   `ss:/yy` `.   -
     -  +yo++ss    oo.   :hs+/sh  `.   -
     -  `ssyss:    :s+    osyss+ .``   -
     -    ---`       .     .--` --``   -
     .                ````    ```..`   -
                                       -
  `...................................-`"""
    image28 = """                                        
                                       .
     `````    ````    ````     ````    -
     -`::/   :::../::`            ``   -
     -`.-`  +y:ooo////+`          ``   -
     -      os:sos:ss+o+          ``   -
     -      :h/so+:o/./o          ``   -
     -      .h/ss+so:-++:--`      ``   -
     .      `sossoyssosso/++      ``   -
     -       :yyhs+sysos+oo-      ``   -
     -      `/sohyyyyyhys::.      ``   -
     -      .s:+dyydsysyo:-.      ``   -
     .      `s+ydsoysooy+--`      ``   -
     -       -/hs+/yoooso::.      ``   -
     .        :shsshyssyh+s-      ``   -
     .        +shyshyyyys:+`      ``   -
     .        `.+:-+/::+`:-       ``   -
     .          -/./+-.:          .`   -
     .          `o//o::.          ``   -
     .           s+oyoso          .`   -
     .           /+/hs+s          .`   -
     .           `s++oo+          .`   -
     .            oo:+o:          ``   -
     .      ```.:+ssyhs+....``    .`   -
     .   `..-..:::-.`-ss:`    :.:/``   -
     .   ``` ` `      .--`    .``..`   -
                                       -
  `...................................-`"""
    image29 = """                                        
                                       .
     `.```    ````   ````    `````     -
     .-+--                      `.     -
     ..``.o++-   :-.:           `.     -
     .`  .dyyy:  .o+h:          `.     -
     .`  `hosss`-oy++s          `.     -
     .`   .ho+s+osy+yh/`        `.     -
     .`    +y/shyhyyhhdy:`      `.     -
     .`     -y+yhyssyodhho....` `.     -
     .`    `/yssmyhhyyhddyyyssoo:.     -
     .`   /ossshmmymydhdddhddhoshs     -
     .`   `//ohhoyhymdyyhdhhmhysys     -
     .`.+osyyyhmydyhmmssss+hmhss+`     -
     `+hdsyosyhdyhoydhhho//ddhy:.`     -
      ddhyyosyhys+/yhyyysyydo+- ``     -
     `yhhhyyoyyhy/yhyoysoyhho   ``     -
     -ohyyhyshhhdddhs+hyoyssh-  ``     -
     -ysdysyhhhdddysosyyoyyoys. ``     -
     -+/o/o+ymdhsoy:.:++so+--+o```     -
     .-s:/. oo+``..`    `y:  /+ ``     -
     .`o+`  :o/         `h` `o- ``     -
     - `s-   `o+`      `/s  os  ``     -
     .  :o.   `/++-````:o-  -` ```     -
     - `-+ys-----+s:.....`   /`/``     -
     `  ````` ` `    ````    .`..`     -
                                       -
  `...................................-`
"""
    image30 ="""                                        
                                       .
     `````    ````    ````    `````    -
    `.+.:..-`    . -`-```         .    -
    `.` `ohs+:   `so+oo:`         .    -
    `.   ohhy+y. `y+/oy/          -    -
    `.   -dhoo++`oo/:os+:         -    -
    `.    :yyys+dh+++o+ys/        -    -
    `.     `ohy+ymsyhysyho/`      -    -
    `.     -oddysmoosyssss/+.     .    -
    `.   -:oooydsysooyysoh+oys+o+`.    -
    `.  `+++++shdosyyhhhyddhdddy:`.    -
    `.  /+o//yy:hh/sdshysdmydm+-- .    -
    `.  :s/:+ss+smhhhoooohddyo-   -    -
    `.  :s+++hs:ydsdy+sooshy:+-   -    -
    `. :+s/ooh:/hhoso+sssyd:/o    .    -
    `. `///ooho+hhsyooyyyhd+ho    .    -
    `.   ./ooyyhhdyhsyshydhdh+    .    -
    `.     /ys:shdddodhhhdhoys    .    -
    `.     .h/:+yhhdyydysdh/os    .    -
    `.      s-:oyyhdsymyoddyms-   .    -
    `.    -/y-+ohodd+ymoohhsd++`  .    -
    `.  `+sodhyddsmmohmyhmmds+s+:..    -
    `.-/+oysso+oyys/::++oo/.-..---.    -
    `.   `....---.`           .:`/.    -
     `                ````    `.```    -
                                       -
  `...................................-`
"""
    image31 = """                                        
                                       .
    `.````    ````    ````    ````.    -
    `.:`  +-                      -    -
    `..  ody:                     -    -
    `.   +y+++.                   -    -
    `.    .s+/y+                  -    -
    `.     .yo+yo.`               -    -
    `.      os/+hss`              -    -
    `.     .sho:syyo:             -    -
    `.      /hho/oyhm:            -    -
    `.       -sh+-oy+s..          -    -
    `.      ./+do::/-soo.         -    -
    `.       /`ys--+oyys          -    -
    `.        `yys++:+hh/-        -    -
    `.         -sds+..ohdy:       -    -
    `.          `sso:.-s+/o`      -    -
    `.          `sdy+-+/.-o`.`    -    -
    `.           .ddo+o:+yyoo/`   -    -
    `.          .+osyo::-yyhs-    -    -
    ``          . `+yho--/yyhy-   -    -
    ``             `yhsoo-+yyy-   -    -
    ``              `-yhs--oys`   -    -
    ..                .os/./o-  - -    -
    `.                  .-.`   `: -    -
     `         `      ```     `````    -
                                       -
  `...................................-`"""    
    image32 = """                                        
                                       .
    `````     ````    ````    ````.    -
    ```:  .-:-`             .-    -    -
    ``.. oooshy-`         `yy.    -    -
    ``  /ys:+shh+-        /ss     -    -
    ``  yys//syd/         /sh     -    -
    `.  oys/:yyh-         ssh-    -    -
    `.  sys/+hdh`        /hsyo    -    -
    `.  :yys+yhy        `od+os    -    -
    `.  `hy//sy/        /sh/+d    -    -
    `. `:ys//sh-        `yy/+d+`  -    -
    `.`/sdy//hys        `dsssdy.  -    -
    `. `.yh//sh-        .mo:ohs   -    -
    `.  `yy+/sh         :do-/ds.` -    -
    `.  -yhossy        `yhy-/yhy/ -    -
    `.  .+h++yo         /ds-:os:  -    -
    `.   `d/+ho-        sho-:yy   -    -
    `.    h+od/`       .hdy/ssy-  -    -
    `.    yyyy-        :hmho+syo  -    -
    `.    :hh+         +hhs::oh/  -`   -
    `.    .hy-        `+dyo::oh+  -`   -
    `.    `ys-        :odho::oh-  .`   -
    `.    -yo`         `:hy//s+ .`.`   -
     .    -.             `::-. `:`.`   -
     .`               ````    `````    -
                                       -
  `...................................-`"""
    image33 = """                                        
                                       .
     .````    ````    ````    ````.    -
    `-`+``        -:::`           -`   -
    `-`./s      `yysshh:     `y-  -    -
    `-  hy:     :ms:/ydh    `sN:  -`   -
    `-  -yo/`  `ydh::hdm -.:sso`  -`   -
    `-   -soy:  shh+smds+ydy++    -`   -
    `-    :hoy:/ys+/yddshmhoo`    -`   -
     -    `:y//ydds/ydmmhohd      -`   -
     -      hh-:ydhyyhmy:odo      -`   -
     -      +sh/-+hhhd+-ommo      -`   -
     -       -ym+-oddo:ydhy+      -`   -
     -      -yys+:/dy+/ss/+.      -`   -
     -      /ds/osss+oso-.`       -`   -
     -      :dhsdshd::/s:o-       -`   -
     -      `ymho/hmdo:-syy`      -`   -
     -    `-omy+yhNhhyo--:s:      -`   -
     -  `.hmy+-+dmNdohso..-/+`    .`   -
     -`/sdhs--oh/odd+d+hs.../s:.  -`   -
     -`:hy/--ohh`/hhsdshhs-..+yy. -`   -
     -`yy:-:sy-`  -dssos:ys+..:y` .`   -
     -+ms+oyy.    `yd+.+.+sy-.-/- .`   -
     -`/+oho`       -+     -//:-``.`   -
     -                          o`.`   -
     .                ````     ```.    -
                                       -
  `...................................-`"""
    image34 = """                                        
                                       .
     `````    ````    ````     ````    -
    `.`:`                         .`   -
    `. -.://:`            .-::-.  .`   -
    `. .ysyysy/`         /so/++s. .`   -
    `. :yso+osy+        :y+-:/+y. .`   -
    `.  +yo/-oy+       +so-.-+so  .`   -
    `.  `yyy//so       -y/.:o+`   .`   -
    `.   .-/soo+       :o-/:.     .`   -
    `.      .+sy.     `o//`       .`   -
    `.        /ys-    +s+`        .`   -
    `.         :os/   +y-         .`   -
    `.           ``   `:          .`   -
    `.          `                 .`   -
    `.         :o.  .::-`         .`   -
     .         +s+   -syo`        .`   -
     .        :+s`    `+so`       .`   -
    `.      .:/+:      `yos/``    .`   -
    `-    .+/-:y        yo/ss+/   .`   -
     -  -+o/.-os:       yo/:oyy`  ``   -
     - -yo:-./y+-       oyo::oys` ``   -
     - /o+o:/so`        +ysssssh. .`   -
     . .++++o/`          .ossss/  ``   -
     .   ```               `.` `+```   -
     .`   ```   `     ````    ``.`.`   -
                                       -
  `...................................-`"""
    image35 = """                                        
                                       .
     `````     ````   ````     `````   -
     . .-        `.                .   -
     . ``        os.`/o+-          .   -
     .         `/so`  .+o/`        .   -
     .       `-oso`     ////.``    -   -
     .     -+o+os`       o-:+oo-   .   -
     -  ./ss+:+y+        ++-.:os-  .   -
     .  syo+:+ys/        `y+--:+s: -   -
     . .yssooso`          /o++o/s: .   -
     .  :/+++-`       `    `-///-  .   -
     .            ``.//+//:::-`    .   -
     .     `-/:::::::---.--:://`   .   -
     .`   `:/:-....--:----://:/    -   -
     .`              `..-//-..`    .   -
     .` -///:.            `:+oo+/` -   -
     .`.s/+++o+`         `oso+sys/ -   -
     .``so:--/s-        /oy+:/osy` -   -
     `` .+s/.-/o        /y+:+os:-  -   -
     ``  `+o+:-o`       ss+o/-     .   -
     `.     `://+`     +oo-`       -   -
     `.       `:o+-`  oy+`         -   -
     `.         ./+/. ss         ``.   -
     `.               ``        `:.-   -
      .     ``  ``     ```     `````   -
                                       -
  `...................................-`"""
    image36 = """                                        
                                       .
    `````     ````    ```     `````    -
    .:-.   `               ``     .    -
    `.` :+oo+/   -o:`    :+o+o/   .    -
    `` :s+/o/s/   syo   -s+/o/s/  .    -
    `` /s+.-:ss`  /ss   :y/.:-ss  .    -
    `` +yo../y.   +ss-  /y+..:s.  .    -
    `` :+s-.o/   -y+oy.`-/s--+/   .    -
    ``  `o::/   `yo:+ys/  +/:/    .    -
    ``   .o+.  `oyo-:oh-  .o+-    .    -
    ``    yo-  `yss+/oy:   so-    .    -
    ``    +so   -ysssso`   /oo    -    -
    ``     .-`   .:/:-`     `-`   .    -
    ``   :-`     .://:`   /-`     .    -
    ``   -ys.   :s/+o+o`  /ys`    .    -
    `.    ss/   ss:://y+  `sy-    .    -
    `.    soo   ss:.-/s-  `so+    -    -
    `.   .s+y: `os+.-o/   :soy.   -    -
    `.  .yo:sy/.`:s-//   -y+:ss+  -    -
    `. `os+-+yy.  o:o`  `ss+-oys  -    -
    `. +ys+:/oh`  :oo   oys+:oss  .    -
    `. `ysyyoss`  .ys.  .hsyyos+  -    -
    `.  .oooo+.    .//   -osoo:`.-.    -
    `.                          -..    -
     `                ````    `````    -
                                       -
  `...................................-`"""
    image37 = """                                        
                                       .
     .````     ```    ````     `````   -
     -`:` ...`    ``       `..`   `.   -
     -``.o+ooo`   .y+`    /o+oo/  `.   -
     -  /s://so    oy-   `y+:++y. `.   -
     -  +y:.:s-    os+   `yo.-+o` `.   -
     -  :o+.++    -s+h-` ./s-:s.  `.   -
     -   `s-+    .yo:sy/   +/+.   `.   -
     -    /+:   `oy+:oy/   `so    `.   -
     -    -s+    +yysoy:    ss.   `.   -
     -     ./`   `/+o+-     `::   `.   -
     -           `./++///::-`     `.   -
     -   `-/:-::::::-----:://`    `.   -
     -  `:+/--...-------://:/`    `.   -
     -            ``..://:-.`     `.   -
     -    /-     `-///.    /-`    `.   -
     -    +y/    +s/o+s.   :yo    `.   -
     -    -so    so-::y/   `yy    ``   -
     -    /oy.  `os-.+o    -ss:   `.   -
     -   :s/ss:  .o/-o`   .s/+y/` `.   -
     -  .yo:+ys`  `o/-   `ss:/yy` `.   -
     -  +yo++ss    oo.   :hs+/sh  `.   -
     -  `ssyss:    :s+    osyss+ .``   -
     -    ---`       .     .--` --``   -
     .                ````    ```..`   -
                                       -
  `...................................-`"""
    image38 = """                                        
                                       .
     `````    ````    ````     ````    -
     -`::/   :::../::`            ``   -
     -`.-`  +y:ooo////+`          ``   -
     -      os:sos:ss+o+          ``   -
     -      :h/so+:o/./o          ``   -
     -      .h/ss+so:-++:--`      ``   -
     .      `sossoyssosso/++      ``   -
     -       :yyhs+sysos+oo-      ``   -
     -      `/sohyyyyyhys::.      ``   -
     -      .s:+dyydsysyo:-.      ``   -
     .      `s+ydsoysooy+--`      ``   -
     -       -/hs+/yoooso::.      ``   -
     .        :shsshyssyh+s-      ``   -
     .        +shyshyyyys:+`      ``   -
     .        `.+:-+/::+`:-       ``   -
     .          -/./+-.:          .`   -
     .          `o//o::.          ``   -
     .           s+oyoso          .`   -
     .           /+/hs+s          .`   -
     .           `s++oo+          .`   -
     .            oo:+o:          ``   -
     .      ```.:+ssyhs+....``    .`   -
     .   `..-..:::-.`-ss:`    :.:/``   -
     .   ``` ` `      .--`    .``..`   -
                                       -
  `...................................-`"""
    image39 = """                                        
                                       .
     `.```    ````   ````    `````     -
     .-+--                      `.     -
     ..``.o++-   :-.:           `.     -
     .`  .dyyy:  .o+h:          `.     -
     .`  `hosss`-oy++s          `.     -
     .`   .ho+s+osy+yh/`        `.     -
     .`    +y/shyhyyhhdy:`      `.     -
     .`     -y+yhyssyodhho....` `.     -
     .`    `/yssmyhhyyhddyyyssoo:.     -
     .`   /ossshmmymydhdddhddhoshs     -
     .`   `//ohhoyhymdyyhdhhmhysys     -
     .`.+osyyyhmydyhmmssss+hmhss+`     -
     `+hdsyosyhdyhoydhhho//ddhy:.`     -
      ddhyyosyhys+/yhyyysyydo+- ``     -
     `yhhhyyoyyhy/yhyoysoyhho   ``     -
     -ohyyhyshhhdddhs+hyoyssh-  ``     -
     -ysdysyhhhdddysosyyoyyoys. ``     -
     -+/o/o+ymdhsoy:.:++so+--+o```     -
     .-s:/. oo+``..`    `y:  /+ ``     -
     .`o+`  :o/         `h` `o- ``     -
     - `s-   `o+`      `/s  os  ``     -
     .  :o.   `/++-````:o-  -` ```     -
     - `-+ys-----+s:.....`   /`/``     -
     `  ````` ` `    ````    .`..`     -
                                       -
  `...................................-`
"""
    image40 ="""                                        
                                       .
     `````    ````    ````    `````    -
    `.+.:..-`    . -`-```         .    -
    `.` `ohs+:   `so+oo:`         .    -
    `.   ohhy+y. `y+/oy/          -    -
    `.   -dhoo++`oo/:os+:         -    -
    `.    :yyys+dh+++o+ys/        -    -
    `.     `ohy+ymsyhysyho/`      -    -
    `.     -oddysmoosyssss/+.     .    -
    `.   -:oooydsysooyysoh+oys+o+`.    -
    `.  `+++++shdosyyhhhyddhdddy:`.    -
    `.  /+o//yy:hh/sdshysdmydm+-- .    -
    `.  :s/:+ss+smhhhoooohddyo-   -    -
    `.  :s+++hs:ydsdy+sooshy:+-   -    -
    `. :+s/ooh:/hhoso+sssyd:/o    .    -
    `. `///ooho+hhsyooyyyhd+ho    .    -
    `.   ./ooyyhhdyhsyshydhdh+    .    -
    `.     /ys:shdddodhhhdhoys    .    -
    `.     .h/:+yhhdyydysdh/os    .    -
    `.      s-:oyyhdsymyoddyms-   .    -
    `.    -/y-+ohodd+ymoohhsd++`  .    -
    `.  `+sodhyddsmmohmyhmmds+s+:..    -
    `.-/+oysso+oyys/::++oo/.-..---.    -
    `.   `....---.`           .:`/.    -
     `                ````    `.```    -
                                       -
  `...................................-`
"""

##########################  EJECUCION DEL JUEGO  #############################################
listaimag = [images.image1, images.image2, images.image3, images.image4, images.image5, images.image6, images.image7, images.image8, images.image9, images.image10]
imgcompleta = list(choice(listaimag))
imgcompleta2 =list(choice(listaimag))
imgcompleta3 = list(choice(listaimag))
@dataclass
class render:
    contadorfila = 1
    contadorcaract1 = 0
    contadorcaract2 = 40
    imagen1x = {}
    lista = []
    imagen2 = {}
    imagen3 = {}
    store = {}
    guardador = {}
    @classmethod
    def guardar (cls, contadorfila, contadorcaract1, contadorcaract2, contador, imagen):
            imagen1 = {}
            while (cls.contadorfila < 30):
                fila = imagen[cls.contadorcaract1:cls.contadorcaract2]
                cls.contadorcaract1 += 41
                cls.contadorcaract2 += 41
                imagen1["{}".format(cls.contadorfila)] = fila
                cls.contadorfila += 1
                #print(cls.imagen1)
            cls.guardador["diccionario{}".format(contador)] = imagen1
            cls.contadorfila = 1
            cls.contadorcaract1 = 0
            cls.contadorcaract2 = 40
            
    #@classmethod
    #def dicalist (cls, diccionario):
        
      #  cls.lista = list(diccionario.values())
      #  x = ''.join(str(e) for e in cls.lista)
        #print(x)
     #   makeitastring = ''.join(map(str, cls.lista))
        #print(makeitastring)
    
    @classmethod
    def unirdic(cls, diccionario1, diccionario2 , diccionario3 ):
        for valor in diccionario1.keys():
            cls.store["{}".format(valor)] = diccionario1[valor] + diccionario2[valor] + diccionario3[valor]
            #print (cls.store)
    
    @classmethod    
    def printear(cls, diccionario):
        for value in diccionario.values():
            makeitastring = ''.join(map(str, value))
            print(makeitastring)
    @classmethod
    def dicguardador(cls):
        img = "           "
        lista = img[2:5]
        diccionario1 = {}
        diccionario2 = {}
        diccionario3 = {}
        contador = 0
        while (contador < 40):
            diccionario1["{}".format(contador)] = lista

            diccionario2["{}".format(contador)] = lista
    
            diccionario3["{}".format(contador)] = lista
            contador += 1
        cls.guardador["diccionario1"] = diccionario1
        cls.guardador["diccionario2"] = diccionario2 
        cls.guardador["diccionario3"] = diccionario3 
    @staticmethod
    def imprimirmano(jugador : "jugador"):
        manoimpresa = []
        contador = 0
        render.dicguardador()
        #print(render.guardador)
        for carta in jugador.Mano.Cartas:
            contador += 1
            render.guardar(render.contadorfila, render.contadorcaract1, render.contadorcaract2, contador, carta.Imagen)
            manoimpresa.append("opcion {}:              {}".format(contador, carta))
            
        render.unirdic(render.guardador["diccionario1"], render.guardador["diccionario2"], render.guardador["diccionario3"])
        render.printear(render.store)
        print(manoimpresa)
        #print(render.guardador)
        render.guardador = {}

#render.guardar(render.contadorfila, render.contadorcaract1, render.contadorcaract2)
#render.guardar2(render.contadorfila, render.contadorcaract1, render.contadorcaract2)
#render.guardar3(render.contadorfila, render.contadorcaract1, render.contadorcaract2)
#render.dicalist(render.imagen1)
#render.unirdic(render.imagen1,render.imagen2, render.imagen3)
#render.printear(render.store)

# Partida


#render.guardar(render.contadorfila, render.contadorcaract1, render.contadorcaract2)
#render.guardar(render.contadorfila, render.contadorcaract1, render.contadorcaract2)
#render.guardar(render.contadorfila, render.contadorcaract1, render.contadorcaract2)
#render.guardar2(render.contadorfila, render.contadorcaract1, render.contadorcaract2)
#render.guardar3(render.contadorfila, render.contadorcaract1, render.contadorcaract2)
#render.dicalist(render.imagen1)
#render.unirdic(render.guardador["diccionario30"], render.guardador["diccionario30"], render.guardador["diccionario30"])
#render.printear(render.store)
#print(render.guardador)


partida = Partida()

partida.crear()


#imgcompleta2 = list(image.image1)
@dataclass
class render2:
    contadorfila2 = 1
    contadorcaract1 = 0
    contadorcaract2 = 40
    imagen1 = {}
    lista = []
    imagen2 = imagen1
    imagen3 = imagen2
    store = {}
    
    @classmethod
    def guardar (cls, imagencompleta2):
        contadorfila = 1
        contadorcaract1 = 0
        contadorcaract2 = 40
        imagen1 = {}
        while (contadorfila < 30):
            fila = imgcompleta2[contadorcaract1 : contadorcaract2]
            contadorcaract1 += 41
            contadorcaract2 += 41
            imagen1["{}".format(contadorfila)] = fila
            contadorfila += 1
        return(imagen1)
    @classmethod
    def dicalist (cls, diccionario):
        
        cls.lista = list(diccionario.values())
        x = ''.join(str(e) for e in cls.lista)
        #print(x)
        makeitastring = ''.join(map(str, cls.lista))
        #print(makeitastring)
    
    @classmethod
    def unirdic(cls, diccionario1, diccionario2, diccionario3):
        for valor in diccionario1.keys():
            cls.store["{}".format(valor)] = diccionario1[valor] + diccionario2[valor] + diccionario3[valor]
            #print (cls.store)
    
    @classmethod    
    def printear(cls, diccionario):
        for value in diccionario.values():
            makeitastring = ''.join(map(str, value))
            print(makeitastring)




 



































