#-*-coding:utf-8-*-




'''leer un numero entero y mostrar todos los multiplos de 5 entre 1 y el numero leido'''



try: 
	numero = int(raw_input("Ingrese un numero entero: "))


	for a in range (1,numero+1):
		if a%5==0:
			print "%d"%a



except ValueError:
	print " La cantidad ingresada debe ser un valor numerico "
