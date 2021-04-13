print("Bienvenido al juego")

movs= int(input("ingrese la cantidad de movimientos(1 movimiento es el del jugador y el del jugador 2): "))
secuencia_1=[]
contador=1

print("ingrese la secuencia")
for contador in range(movs) :
	secuencia_1.append (int(input("Ingrese el movimiento del Jugador 1:  ")))
	secuencia_1.append (int(input("Ingrese el movimiento del Jugador 2:  ")))

def tableroVacio():
	return [
			[0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0],
			]

def completarTableroEnOrden(secuencia, tablero):
	for indice, columna in enumerate(secuencia):
		if columna < 7:
			if columna >= 1:
				fichaNumero= 1+ (indice % 2)
				soltarFichaEnColumna(fichaNumero, columna, tablero)
			else:
				print("La columna debe estar entre 1-7")
				return
		else:
			print("La columna debe estar entre 1-7")
			return
	return tablero

def soltarFichaEnColumna(ficha, columna, tablero):
	for fila in range(6, 0, -1):
		if tablero[fila - 1][columna - 1] == 0:
			tablero[fila - 1][columna - 1] = ficha
			return 

def dibujarTablero(tablero):
	for fila in tablero:
		for celda in fila:
			if celda == 0:
				print(' 0 ', end=' ')
			else:
				print(' %s ' % celda, end=' ')
		print(' ')

dibujarTablero(completarTableroEnOrden(secuencia_1, tableroVacio()))