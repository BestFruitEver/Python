#!/bin/bash


echo "Veuillez renseigner votre nom"
read nom
jour=$(date +%F)
heure=$(date +%R)
echo "Bonjour $nom ! Nous somme le $jour et il est $heure."
