#colores
Rojo='\033[31m'
Verde='\033[32m'
Amarillo='\033[33m'
Azul=('\033[34m')
Morado='\033[35m'
Blanco=('\033[37m')
printf $Rojo"(ruta)"$Azul"Krypton >> "$Blanco
read ruta
printf $Azul"Puerto: "
read puerto
cd $ruta
php -S localhost:$puerto

