#!/bin/bash

echo "Inidquez votre X"
read -r X
echo "Indiquez votre Y"
read -r Y
let "c = X+Y"
echo "La somme de $X + $Y est : $c"
