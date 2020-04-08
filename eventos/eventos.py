from rx.subject import Subject
from dataclasses import dataclass, field

# subject_test = Subject()
# subject_test.subscribe(
#    lambda x: print("PRIMERO  {0}".format(x))
# )
# subject_test.subscribe(
#    lambda x: print("SEGUNDO {0}".format(x))
# )

# subject_test.on_next("A")
# subject_test.on_next("B")

# cambioTurno = Subject()
# cambioTurno.subscribe(lambda x: print("Ahora tiene el turno el jugador  {}".format(x)))
# cambioTurno.subscribe(lambda x: print("dale apurate  {}".format(x)))

# cambioTurno.on_next("mauro")
# cambioTurno.on_next("ale")
# cambioTurno.on_next("yaco")

class Equipo:
   def __init__(self, jugador, cartero):
      self.Jugadores = jugador
      cartero.subscribe(lambda cantante: self.tecantotruco(cantante))
      
   def tecantotruco(self, cantante):
      if(cantante == self.Jugadores):
         pass
      else:
         print("{} canto truco".format(cantante))

@dataclass
class Puntaje:
   PuntajeEquipo1: int = 2
   PuntajeEquipo2: int = 4

   def iniciar(self, mostrarpuntaje):
      mostrarpuntaje.subscribe(self.mostrarPuntajes())

   def mostrarPuntajes(self):
      print("Puntaje Equipo1: {}".format(self.PuntajeEquipo1))
      print("Puntaje Equipo2: {}".format(self.PuntajeEquipo2))

class Ronda:
   def __init__(self):
      cartero = Subject()
      puntajeRonda = Puntaje()

      Equipo("mauro", cartero)
      Equipo("yaquin", cartero)
      puntajeRonda.iniciar(cartero)

      # Ronda 1
      cartero.on_next("yaquin")


ronda = Ronda()



   
