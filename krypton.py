import os
import time
#####################################
#colores
Rojo='\033[31m'
Verde='\033[32m'
Amarillo='\033[33m'
Azul=('\033[34m')
Morado='\033[35m'
Blanco=('\033[37m')
#####################################
#banner
print Azul
os.system('clear')
os.system('figlet -f smblock "        Krypton Security"')
#####################################
#HERRAMIENTA
os.system('bash name.sh')
print Blanco+"                      ["+Azul+"+"+Blanco+"]""HACKING ETICO"
print Azul+"         -----------------------------------------"
def option():
	print Blanco+"["+Azul+"1"+Blanco+"]""MENU "+Blanco+"["+Azul+"2"+Blanco+"]""FANPAGE "+Blanco+"["+Azul+"3"+Blanco+"]""GRUPO "+Blanco+"["+Azul+"4"+Blanco+"]""EXIT"
######################################
def link():
	print Blanco+"["+Azul+"1"+Blanco+"]""Ngrok "+Blanco+"["+Azul+"2"+Blanco+"]""Run "+Blanco
	xx=raw_input(Azul+"Krypton >> "+Blanco)
	if xx == "1":
		os.system('ngrok http 3333')
	elif xx == "2":
		os.system('ssh -R localhost:80:localhost:8080 localhost.run')
	else:
		pass
def local():
	print(Amarillo+"Coloque la ruta de los archivos")
	os.system('bash local.sh')
######
def ngrok():
	print Amarillo+"""Te redireccionare a mega para 
la descarga de la version
de ngrok compatible con termux"""
	time.sleep(0.9)
	os.system('xdg-open https://mega.nz/file/cclRBCYb#DLxyZS_CUTvmBZKieQchSK3CADJZTuRnvdOKnuhjk5U')
	print ""
	print """Una vez descargado aparecera en la siguente ruta
/data/data/com.termux/files/home/storage/downloads

Si lo descargo desde la app es la siguiente ruta
/data/data/com.termux/files/home/storage/shared/Mega/'MEGA Downloads'

Ahora ya que estemos en la ruta donde esta ngrok lo moveremos con 
mv ngrok $HOME

Abrimos nueva pestana y colocamos los siguientes comandos 
cp -r ngrok /data/data/com.termux/files/usr/bin

Ya despues nos registraremos en ngrok copeamos 
los comandos que nos dio la pagina al resgistrarnos
y listo ya tendras ngrok'"""
	option()
	menu()
#######
def inpum():
        rout = raw_input(Azul+"Krypton >> "+Blanco)
	if rout == 'local':
                local()
	elif rout == 'ngrok':
		ngrok()
	elif rout == 'link':
		link()
	else:
		pass
#########
def opciones():
        print Verde+"local - subir archivos php,html al localhost"
	print Verde+"ngrok - pasos para configurarlo en termux"
	print Verde+"link - soluciona el error de algun link de algun script  "
	inpum()
######################################
def menu():
	usuario=raw_input(Azul+'COLOQUE LA OPCION: '+Blanco)
	if usuario == '3':
		os.system('xdg-open https://t.me/joinchat/OxC4BVYylMVPMqEAvHZsDw')
	elif usuario == '2':
 		os.system('xdg-open https://m.facebook.com/Krypt%C3%B3n-Security-106630810838763/?ref=bookmarks')
	elif usuario == '4':
		print Amarillo+'Ha salido con exito'
	elif usuario == '1':
		opciones()
	else:
		pass
option()
menu()
