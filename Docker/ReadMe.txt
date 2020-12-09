Docker

Docker est un logiciel de conteuneurisation. Cela permet de permet de placer
nos applications dans des conteneurs. Cette conteneurisation à l'avantage,
contrairement à la virtualisation, d'être très légère et de s'adapter à l'OS
de la machine hôte, alors que la virtualisation demande de créer une VM qui
aura son propre OS et sera plus lourd.

Grâce à Docker plusieurs personnes peuvent travailler sur le même projet sans 
pour autant avoir la même version de Python par exemple.

La conteneurisation permet d'isoler les applications et ainsi de pouvoir par
exemple mettre à jour un conteneur sans que cela n'affecte les autres 
conteneurs