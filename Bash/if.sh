#!/bin/bash

echo "Veuillez indiquer un nombre"
read -r nombre

if [ "$nombre" -le 9 ]
then
	echo "Votre nombre possède un seul chiffre"
elif [ "$nombre" -le 99 ]
then
	echo "Votre nombre possède 2 chiffres"
elif [ "$nombre" -le 999 ]
then
	echo "Votre nombre possède 3 chiffres"
else
	echo "Veuillez saisir un nombre entre 1 et 999"
fi

