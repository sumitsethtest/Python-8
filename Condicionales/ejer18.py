#-*-coding:utf-8-*-
 

'''Leer un número entero de tres dígitos y determinar si algún dígito es múltiplo de los otros'''

try:
 	numero = int(raw_input("Ingrese un numero entero de tres digitos :"))
 	digito1 = numero/100
 	digito2 = (numero%100) /10
 	digito3 = numero/10
 	

 	if numero>99 and numero <=999:

 		if digito1%digito2== 0:
 			print "el digito 1 es multiplo del digito 2"

 		elif digito1%digito3==0:
 			print " el digito 1 es multiplo del digito 3"

 		elif digito2&digito3==0:
 			print " el digito 2 es multiplo del digito 3"

 		elif digito2%digito1==0: 
 			print " el digito 2 es multiplo del digito 1"

 		elif digito3%digito2==0:
 			print "el digito 3 es multiplo del digito 2"

 		elif digito3%digito1==0:
 			print "el digito 3 es multiplo del digito 1"

	else: 
		print "el numero ingresado debe ser de tres digitos"


 		


except ValueError: 
	print " la cantidad ingresada debe ser un valor numerico"	
 	

