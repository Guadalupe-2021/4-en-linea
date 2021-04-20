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

tablero 1=dibujarTablero(completarTableroEnOrden(secuencia_1, tableroVacio()))

def contenidoColumna(nro_columna,tablero)
	columna=[]
	for fila in tablero:
		celda=fila[nro_columna - 1]
		columna.append(celda)
	return columna

def llamadoColumna(nro,tablero)
	if nro==0:
		contenidoColumna(6,tablero)
		contenidoColumna(5,tablero)
		contenidoColumna(4,tablero)
		contenidoColumna(3,tablero)
		contenidoColumna(2,tablero)
		contenidoColumna(1,tablero)
	else: 
		contenidoColumna(nro,tablero)

def contenidoFila(nro_fila,tablero)
	fila=[]
	for columna in tablero:
		celda=columna[nro_fila - 1]
		fila.append(celda)
	return fila

def llamadoFila(nro,tablero)
	if nro==0:
		contenidoFila(6,tablero)
		contenidoFila(5,tablero)
		contenidoFila(4,tablero)
		contenidoFila(3,tablero)
		contenidoFila(2,tablero)
		contenidoFila(1,tablero)
	else: 
		contenidoFila(nro,tablero)

ver= int(input("Para ver las filas ingrese 1, para ver las columnas ingrese 2, para saltar esto precione otro numero"))

if ver == 1:
	num1=int(input("Ingrese 0 para ver todas las filas, o un numero del 1-6 para ver una en concreto"))
	if num1 > 6:
		print("Numero invalido")
		return
	else:
		llamadoFila(num1,tablero1)
else:
	if ver == 2:
		num2=int(input("Ingrese 0 para ver todas las columnas, o un numero del 1-6 para ver una en concreto"))
		if num2 > 6:
			print("Numero invalido")
			return
		else:
			llamadoColumna(num2,tablero1)
				
	else:
		print("saltado")
