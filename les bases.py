Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> A = 2
>>> B = 3
>>> C = 0
>>> print (A)
2
>>> print (B)
3
>>> print (C)
0
>>> C = A
>>> A = B
>>> B = C
>>> print (A)
3
>>> print (C)
2
>>> print (B)
2
>>> def carre() :
	x = int(input("Saisissez un nombre"))
	nombre = x*x
	print (nombre)
	
>>> carre()
Saisissez un nombre5
25
		       
>>> def condition():
	x = int(input("Saisissez un nombre"))
	if x < 0 :
		print ("le nombre est négatif")
	else :
		print ("le nombre est positif")

>>> condition()
		       
Saisissez un nombre -3
le nombre est négatif
>>> condition()
		       
Saisissez un nombre5
le nombre est positif
>>> def produit() :
	x = int(input("Saissez un nombre"))
	y = int(input("Saissiez un deuxème nombre"))
	if x + y < 0 :
		print ("La somme des deux nombres est négative")
	else :
		print ("La somme des deux nombres est positive")

		       
>>> produit()
		       
Saissez un nombre5
Saissiez un deuxème nombre6
La somme des deux nombres est positive
>>> produit()
		       
Saissez un nombre5
Saissiez un deuxème nombre-7
La somme des deux nombres est négative
>>> produit()
		       
Saissez un nombre-7
Saissiez un deuxème nombre5
La somme des deux nombres est négative

>>> def calcul() :
	x = int(input("Saisissez un nombre"))
	j = x +10
	while x < j:
		print(x)
		x = x+1

	
>>> calcul()
		
Saisissez un nombre5
5
6
7
8
9
10
11
12
13
14
>>> def Additiviter() :
        b
        a = int(input("Saisissez un nombre"))
        for(i=1;i<a;a++):
                b = b+i
                print(b)



SyntaxError: invalid syntax
