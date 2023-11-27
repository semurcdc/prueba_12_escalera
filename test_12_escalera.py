import random

def tirar_dado():#Función para generar el numero aleatorio del dado
  dado=random.randint(1, 6)
  return dado

def sube(pos):#Función para subir posición (escalera)
  if(pos==3):
    print("Jugador sube por escalera al cuadro 11")
    pos=11

  if(pos==6):
    print("Jugador sube por escalera al cuadro 17")
    pos=17
    
  if(pos==9):
    print("Jugador sube por escalera al cuadro 18")
    pos=18

  if(pos==10):
    print("Jugador sube por escalera al cuadro 12")
    pos=12
  return pos

def baja(pos): #Función para bajar posición (serpiente)

  if(pos==14):
    print("Jugador desciende al cuadro 4")
    pos=4
    
  if(pos==19):
    print("Jugador desciende al cuadro 8")
    pos=8

  if(pos==22):
    print("Jugador desciende al cuadro 20")
    pos=20

  if(pos==24):
    print("Jugador desciende al cuadro 16")
    pos=16
  return pos

pos=1 #Arranca en posicion 1

print("Bienvenido al juego de la escalera")

while pos<25:
  numero_dado=tirar_dado()#Llama a funcion dado
  print(f"Dado arroja {numero_dado}")#Imprime resultado del dado

  pos=pos+numero_dado#Suma la posición obtenida por el dado a la anterior

  if(pos>25):
    print("Jugador supera el cuadro 25")
    break

  print(f"Jugador avanza a cuadro {pos}")

  if(pos==3 or pos==6 or pos==9 or pos==10):#Escaleras
    pos=sube(pos)

  if(pos==14 or pos==19 or pos==22 or pos==24):#Serpientes
    pos=baja(pos)

print("Fin")