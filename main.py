import time
import numpy as np
import sys


# IMPRIMIR CON RETRASO
def retrasoEscritura(s):
    # Imprime una letra a la vez
    # POR CADA LETRA QUE PASE POR PARAMETRO
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.07)


# CREAR CLASE POKEMON
class Pokemon:

    # CREAMOS UN OBJETO QUE INICIALIZARA LAS CLASES
    def __init__(self, nombre, tipo, movimientos, stats, salud=' ===================='):
        # SALVAMOS LAS VARIABLES COMO ATRIBUTOS
        self.nombre = nombre
        self.tipo = tipo
        self.movimientos = movimientos
        self.ataque = stats['ataque']
        self.defensa = stats['defensa']
        self.velocidad = stats['velocidad']
        self.salud = salud
        self.barras = 20  # Cantidad de barras de salud

        # IMPRIMIR INFORMACION DE BATALLA

    def imprimir(self, Pokemon2):
        print("   BATALLA POKEMON   ")
        # IMPRIMIMOS LA INFORMACION DEL PRIMER POKEMON
        print(f"\n{self.nombre}")
        print("Tipo - ", self.tipo)
        print("Ataque -", self.ataque)
        print("Defensa -", self.defensa)
        print("Velocidad -", self.velocidad)
        print("Nivel: ", 2 * (np.mean([self.ataque, self.defensa])))
        print("\nVS")
        # IMPRIMIMOS LA INFORMACION DEL POKEMON 2
        print(f"\n{Pokemon2.nombre}")
        print("Tipo -", Pokemon2.tipo)
        print("Ataque -", Pokemon2.ataque)
        print("Defensa -", Pokemon2.defensa)
        print("Velocidad -", Pokemon2.velocidad)
        print("Nivel: ", 2 * (np.mean([Pokemon2.ataque, Pokemon2.defensa])))
        time.sleep(2)

    # HACEMOS UN OBJETO QUE REVISE LAS VENTAJAS DE TIPO
    def Ventajas(self, Pokemon2):
        version = ['fuego', 'agua', 'planta']
        for i, k in enumerate(version):

            if self.tipo == k:
                if Pokemon2.tipo == k:
                    cadenaAtaque1 = '\nNo es muy efectivo...'
                    cadenaAtaque2 = '\nNo es muy efectivo...'

                # POKEMON2 ES FUERTE
                if Pokemon2.tipo == version[(i + 1) % 3]:
                    Pokemon2.ataque *= 2
                    Pokemon2.defensa *= 2
                    self.ataque /= 2
                    self.defensa /= 2
                    cadenaAtaque1 = '\nNo es muy efectivo...'
                    cadenaAtaque2 = '\nEs super efectivo!'

                # SI POKEMON2 ES DEBIL
                if Pokemon2.tipo == version[(i + 2) % 3]:
                    Pokemon2.ataque /= 2
                    Pokemon2.defensa /= 2
                    self.ataque *= 2
                    self.ataque *= 2
                    cadenaAtaque1 = '\nEs super efectivo!'
                    cadenaAtaque2 = '\nNo es muy efectivo...'

        return cadenaAtaque1, cadenaAtaque2

    # HACEMOS LA FUNCION DEL DESARROLLO DEL COMBATE
    def turnos(self, Pokemon2, cadenaAtaque1, cadenaAtaque2):
        while (self.barras > 0) and (Pokemon2.barras > 0):
            print(f"\n{self.nombre}\t\tPS\t{self.salud}")
            print(f"\n{Pokemon2.nombre}\t\tPS\t{Pokemon2.salud}")

            if self.velocidad >= Pokemon2.velocidad:
                print(f"ADELANTE {self.nombre}!")
                for i, x in enumerate(self.movimientos):
                    print(f"{i + 1.}", x)
                indice = int(input('Eligue un movimiento: '))
                retrasoEscritura(f"\n{self.nombre} uso {self.movimientos[indice - 1]}!")
                time.sleep(1)
                retrasoEscritura(cadenaAtaque1)

                # DETERMINAMOS EL DAMAGE
                Pokemon2.barras -= self.ataque
                Pokemon2.salud = ""

                # AGREGAMOS BARRAS ADICIONALES
                for j in range(int(Pokemon2.barras + .1 * Pokemon2.defensa)):
                    Pokemon2.salud += "="
                time.sleep(1)
                print(f"\n{self.nombre}\t\tPS:\t{self.salud}")
                print(f"\n{Pokemon2.nombre}\t\tPS:\t{Pokemon2.salud}")
                time.sleep(0.5)

                if Pokemon2.barras <= 0:
                    retrasoEscritura("\n" + Pokemon2.nombre + " se debilito.")
                    break

                print(f"\nADELANTE {Pokemon2.nombre}!")
                for i, x in enumerate(Pokemon2.movimientos):
                    print(f"{i + 1.}", x)
                indice = int(input('Eligue un movimiento: '))
                retrasoEscritura(f"\n{Pokemon2.nombre} uso {Pokemon2.movimientos[indice - 1]}!")
                time.sleep(1)
                retrasoEscritura(cadenaAtaque2)

                # DETERMINAMOS EL DAMAGE
                self.barras -= Pokemon2.ataque
                self.salud = ""

                # AGREGAMOS BARRAS ADICIONALES
                for j in range(int(self.barras + .1 * self.defensa)):
                    self.salud += "="
                time.sleep(1)
                print(f"\n{self.nombre}\t\tPS:\t{self.salud}")
                print(f"\n{Pokemon2.nombre}\t\tPS:\t{Pokemon2.salud}")
                time.sleep(0.5)

                if self.barras <= 0:
                    retrasoEscritura("\n" + self.nombre + " se debilito.")
                    break

            if self.velocidad < Pokemon2.velocidad:
                print(f"ADELANTE {Pokemon2.nombre}!")
                for i, x in enumerate(Pokemon2.movimientos):
                    print(f"{i + 1.}", x)
                indice = int(input('Eligue un movimiento: '))
                retrasoEscritura(f"\n{Pokemon2.nombre} uso {Pokemon2.movimientos[indice - 1]}!")
                time.sleep(1)
                retrasoEscritura(cadenaAtaque2)

                # DETERMINAMOS EL DAMAGE
                self.barras -= Pokemon2.ataque
                self.salud = ""

                # AGREGAMOS BARRAS ADICIONALES
                for j in range(int(self.barras + .1 * self.defensa)):
                    self.salud += "="
                time.sleep(1)
                print(f"\n{self.nombre}\t\tPS:\t{self.salud}")
                print(f"\n{Pokemon2.nombre}\t\tPS:\t{Pokemon2.salud}")
                time.sleep(0.5)

                if self.barras <= 0:
                    retrasoEscritura("\n" + self.nombre + " se debilito.")
                    break
                print(f"ADELANTE {self.nombre}!")
                for i, x in enumerate(self.movimientos):
                    print(f"{i + 1.}", x)
                indice = int(input('Eligue un movimiento: '))
                retrasoEscritura(f"\n{self.nombre} uso {self.movimientos[indice - 1]}!")
                time.sleep(1)
                retrasoEscritura(cadenaAtaque1)

                # DETERMINAMOS EL DAMAGE
                Pokemon2.barras -= self.ataque
                Pokemon2.salud = ""

                # AGREGAMOS BARRAS ADICIONALES
                for j in range(int(Pokemon2.barras + .1 * Pokemon2.defensa)):
                    Pokemon2.salud += "="
                time.sleep(1)
                print(f"\n{self.nombre}\t\tPS:\t{self.salud}")
                print(f"\n{Pokemon2.nombre}\t\tPS:\t{Pokemon2.salud}")
                time.sleep(0.5)

                if Pokemon2.barras <= 0:
                    retrasoEscritura("\n" + Pokemon2.nombre + " se debilito.")
                    break

    # DEFINIMOS LAS CARACTERISTICAS DE LA LUCHA
    def lucha(self, Pokemon2):

        # IMPRIMIR INFORMACION DE LA LUCHA
        self.imprimir(Pokemon2)
        # CONSIDERAR LA VENTAJA DE TIPO
        cadenaAtaque1, cadenaAtaque2 = self.Ventajas(Pokemon2)

        # LUCHA REAL MIENTRA HAYA LUCHA REAL
        self.turnos(Pokemon2, cadenaAtaque1, cadenaAtaque2)

        # RECIBIMOS PREMIO
        dinero = np.random.choice(1000000)
        retrasoEscritura(f"\nEl oponente dio: ${dinero}")


if __name__ == '__main__':
    # CREAMOS POKEMONES
    Charizard = Pokemon('Charizard', 'fuego', ['Lanzallamas', 'Garra Dragon', 'Volar', 'Giro Fuego'],
                        {'ataque': 12, 'defensa': 8, 'velocidad': 10})
    Blastoise = Pokemon('Blastoise', 'agua', ['Hidro Bomba', 'Pistola de Agua', 'Burbujas', 'Surf'],
                        {'ataque': 10, 'defensa': 10, 'velocidad': 9})
    Venasaur = Pokemon('Venasaur', 'planta', ['Rayo Solar', 'Latigo Cepa', 'Hojas Navaja', 'Atrapar'],
                       {'ataque': 8, 'defensa': 12, 'velocidad': 5})

    Charmeleon = Pokemon('Charmeleon', 'fuego', ['Llamarada', 'Arañazo', 'Tacleada', 'Giro Fuego'],
                         {'ataque': 6, 'defensa': 4, 'velocidad': 7})
    Warturle = Pokemon('Warturtle', 'agua', ['Rayo Burbuja', 'Pistola de Agua', 'Cabezazo', 'Surf'],
                       {'ataque': 5, 'defensa': 5, 'velocidad': 8})
    Ivysaur = Pokemon('Ivysaur', 'planta', ['Latigo Cepa', 'Hojas Navaja', 'Tacleada', 'Atrapar'],
                      {'ataque': 4, 'defensa': 6, 'velocidad': 6})

    Charmander = Pokemon('Charmander', 'fuego', ['Ascuas', 'Arañazo', 'Tacleada'],
                         {'ataque': 3, 'defensa': 2, 'velocidad': 6})
    Squirtle = Pokemon('Squirtle', 'agua', ['Burbujas', 'Tacleada', 'Arañazo'],
                       {'ataque': 3, 'defensa': 4, 'velocidad': 5})
    Bulbasaur = Pokemon('Bulbasaur', 'planta', ['Latigo Cepa', 'Hojas Navaja', 'Tacleada'],
                        {'ataque': 2, 'defensa': 3, 'velocidad': 4})

    print("SELECCION DE POKEMON 1: ")
    a = int(input("1.-Charizard, 2.- Blastoise, 3.-Venasaur \n4.-Charmeleon, 5.-Warturtle, 6.-Ivysaur \n7.-Charmander, 8.-Squirtle, 9.- Bulbasaur \n"))
    print("SELECCION DE POKEMON 2: ")
    b = int(input("1.-Charizard, 2.- Blastoise, 3.-Venasaur \n4.-Charmeleon, 5.-Warturtle, 6.-Ivysaur \n7.-Charmander, 8.-Squirtle, 9.- Bulbasaur \n"))

    # CONDICIONALES DE CHARIZARD
    if a == 1:
        if b == 2:
            Charizard.lucha(Blastoise)
        elif b == 3:
            Charizard.lucha(Venasaur)
        elif b == 4:
            Charizard.lucha(Charmeleon)
        elif b == 5:
            Charizard.lucha(Warturle)
        elif b == 6:
            Charizard.lucha(Ivysaur)
        elif b == 7 :
            Charizard.lucha(Charmander)
        elif b == 8 :
            Charizard.lucha(Squirtle)
        elif b == 9 :
            Charizard.lucha(Bulbasaur)

    # CONDICIONALES BLASTOISE
    if a == 2 :
        if b == 1 :
            Blastoise.lucha(Charizard)
        elif b == 3 :
            Blastoise.lucha(Venasaur)
        elif b == 4 :
            Blastoise.lucha(Charmeleon)
        elif b == 5 :
            Blastoise.lucha(Warturle)
        elif b == 6 :
            Blastoise.lucha(Ivysaur)
        elif b == 7 :
            Blastoise.lucha(Charmander)
        elif b == 8 :
            Blastoise.lucha(Squirtle)
        elif b == 9 :
            Blastoise.lucha(Bulbasaur)

    # CONDICIONALES DE VENASAUR
    if a == 3 :
        if b == 1 :
            Venasaur.lucha(Charizard)
        elif b == 2 :
            Venasaur.lucha(Blastoise)
        elif b == 4 :
            Venasaur.lucha(Charmeleon)
        elif b == 5 :
            Venasaur.lucha(Warturle)
        elif b == 6 :
            Venasaur.lucha(Ivysaur)
        elif b == 7 :
            Venasaur.lucha(Charmander)
        elif b == 8 :
            Venasaur.lucha(Squirtle)
        elif b == 9 :
            Venasaur.lucha(Bulbasaur)

    # CONDICIONALES DE CHARMELEON
    if a == 4 :
        if b == 1 :
            Charmeleon.lucha(Charizard)
        elif b == 2 :
            Charmeleon.lucha(Blastoise)
        elif b == 3 :
            Charmeleon.lucha(Venasaur)
        elif b == 5 :
            Charmeleon.lucha(Warturle)
        elif b == 6 :
            Charmeleon.lucha(Ivysaur)
        elif b == 7 :
            Charmeleon.lucha(Charmander)
        elif b == 8 :
            Charmeleon.lucha(Squirtle)
        elif b == 9 :
            Charmeleon.lucha(Bulbasaur)

    # CONDICIONALES DE WARTURTLE
    if a == 5 :
        if b == 1 :
            Warturle.lucha(Charizard)
        elif b == 2 :
            Warturle.lucha(Blastoise)
        elif b == 3 :
            Warturle.lucha(Venasaur)
        elif b == 4 :
            Warturle.lucha(Charmeleon)
        elif b == 6 :
            Warturle.lucha(Ivysaur)
        elif b == 7 :
            Warturle.lucha(Charmander)
        elif b == 8 :
            Warturle.lucha(Squirtle)
        elif b == 9 :
            Warturle.lucha(Bulbasaur)

    # CONDICIONALES DE IVYSAUR
    if a == 6 :
        if b == 1 :
            Ivysaur.lucha(Charizard)
        elif b == 2 :
            Ivysaur.lucha(Blastoise)
        elif b == 3 :
            Ivysaur.lucha(Venasaur)
        elif b == 4 :
            Ivysaur.lucha(Charmeleon)
        elif b == 5 :
            Ivysaur.lucha(Warturle)
        elif b == 7 :
            Ivysaur.lucha(Charmander)
        elif b == 8 :
            Ivysaur.lucha(Squirtle)
        elif b == 9 :
            Ivysaur.lucha(Bulbasaur)

    # CONDICIONALES DE CHARMANDER
    if a == 7 :
        if b == 1 :
            Charmander.lucha(Charizard)
        elif b == 2 :
            Charmander.lucha(Blastoise)
        elif b == 3 :
            Charmander.lucha(Venasaur)
        elif b == 4 :
            Charmander.lucha(Charmeleon)
        elif b == 5 :
            Charmander.lucha(Warturle)
        elif b == 6 :
            Charmander.lucha(Ivysaur)
        elif b == 7 :
            Charmander.lucha(Squirtle)
        elif b == 8 :
            Charmander.lucha(Bulbasaur)

    # CONDICIONALES DE SQUIRTLE
    if a == 8 :
        if b == 1 :
            Squirtle.lucha(Charizard)
        elif b == 2 :
            Squirtle.lucha(Blastoise)
        elif b == 3 :
            Squirtle.lucha(Venasaur)
        elif b == 4 :
            Squirtle.lucha(Charmeleon)
        elif b == 5 :
            Squirtle.lucha(Ivysaur)
        elif b == 6 :
            Squirtle.lucha(Warturle)
        elif b == 7 :
            Squirtle.lucha(Charmeleon)
        elif b == 9 :
            Squirtle.lucha(Bulbasaur)

    # CONDICIONALES BULBASAUR
    if a == 9 :
        if b == 1 :
            Bulbasaur.lucha(Charizard)
        elif b == 2 :
            Bulbasaur.lucha(Blastoise)
        elif b == 3 :
            Bulbasaur.lucha(Venasaur)
        elif b == 4 :
            Bulbasaur.lucha(Charmeleon)
        elif b == 5 :
            Bulbasaur.lucha(Warturle)
        elif b == 6 :
            Bulbasaur.lucha(Ivysaur)
        elif b == 7 :
            Bulbasaur.lucha(Charmander)
        elif b == 8 :
            Bulbasaur.lucha(Squirtle)
