import os
import win32com.client
import pygame
import win32com.client
import time

# v1.0.1
# se adaptan las imagenes que se cargan a 500px por proporcional de alto. 

# CONFIGURACION --------------------------------------------------------
cantCarpetas= 20 # este es el nro de carpetas creadas, si la carpeta está vacía no carga la slide
fondo = (255,255,255)
velocEscala=0.0075
esperaSeleccion=0.6
# ------------------------------------------------------------------------

class slide():
	def __init__(self,numero):
		global ruta_app
		self.archivos= os.listdir(ruta_app+"/diapos/"+str(numero))
		self.rutasArchivos=[]
		self.locucionesArchivos=[]
		self.imagenes=[] #precargo las imagenes en una lista para no recargarlas cada vez qeue se muestra en gameloop
		for archivo in self.archivos:	
			locucionArchivo = (archivo[:-4:]) # corta cadena inicio : final : salto , si se deja en blanco empieza con el primero o el ultimo
			locucionArchivo = locucionArchivo.replace("_"," ")
			self.locucionesArchivos.append(locucionArchivo)
			rutaArchivo=ruta_app+"/diapos/"+str(numero)+"/"+archivo
			self.rutasArchivos.append(rutaArchivo)
			# corrijo la resolucion a 500px de ancho por proporcional y la cargo en la lista
			tempImagen= pygame.image.load(rutaArchivo).convert_alpha()
			proporcion= tempImagen.get_height()/tempImagen.get_width() #alto/ancho
			tempImagen= pygame.transform.scale(tempImagen,(300,int(300*proporcion)))
			self.imagenes.append(tempImagen)
			
def cargaSlides():
	slides= []
	for i in range (1,cantCarpetas+1):
		if slide(i).archivos: # esto es un boolaneo implicito de python, es TRUE si no es vacio
			slides.append(slide(i))
			print ("se cargó slide:",i)
	return slides

def mostrarPictogramas(nroSlide):
	# Si hay 2 archivos en la carpeta
	if len(slides[nroSlide].imagenes) == 2 :
		x= display_width/4
		for imagen in slides[nroSlide].imagenes:
			columna= slides[nroSlide].imagenes.index(imagen)
			imagen =  pygame.transform.rotozoom(imagen,0,1+escalaPictograma2[columna])
			ancho, alto = imagen.get_size()
			y=display_height/2-alto/2
			if columna == 0:
				x= display_width/4
			else:
				x= display_width*3/4
			x-=ancho/3
			gameDisplay.blit(imagen, (x,y))
	# Si hay 4 archivos en la carpeta
	elif len(slides[nroSlide].imagenes) == 4 :
		x= display_width/4
		fila=0
		for imagen in slides[nroSlide].imagenes:
			anchoOrg= imagen.get_width()
			imagen =  pygame.transform.rotozoom(imagen,0,1+escalaPictograma4[fila])
			ancho, alto = imagen.get_size()
			#imagen =  pygame.transform.scale(imagen,(int(ancho*(1+escalaPictograma[fila-1])),int(alto*(1+escalaPictograma[fila-1]))))
			#rotozoom(Surface, angle, scale)
			if fila==2: x= display_width/4
			if fila > 1: 
				y=display_height/4*3-alto/2
			else:
				y=display_height/4-alto/2
			x-=ancho/3
			#print (x,y,slides[nroSlide].archivos[fila])
			gameDisplay.blit(imagen, (x,y))
			x=display_width/2+anchoOrg
			fila+=1
	else:
		print ("nro incorrecto de pictogramas")
		
def hablar(cuadrante):
	global pausa
	pausa=True
	print (slides[slideActual].locucionesArchivos[cuadrante])
	locutor.Speak(slides[slideActual].locucionesArchivos[cuadrante])


def calculaCuadrateMouse(mouseX,mouseY):
	global escalaPictograma4
	global escalaPictograma2
	if len(slides[slideActual].imagenes) == 4:
		if mouseX<=display_width/2 and mouseY<=display_height/2:
			cuadranteMouse=0
			escalaPictograma4=[escalaPictograma4[0]+velocEscala,0,0,0]
		if mouseX>=display_width/2 and mouseY<=display_height/2:
			cuadranteMouse=1
			escalaPictograma4=[0,escalaPictograma4[1]+velocEscala,0,0]
		if mouseX<=display_width/2 and mouseY>=display_height/2:
			cuadranteMouse=2
			escalaPictograma4=[0,0,escalaPictograma4[2]+velocEscala,0]
		if mouseX>=display_width/2 and mouseY>=display_height/2:
			cuadranteMouse=3
			escalaPictograma4=[0,0,0,escalaPictograma4[3]+velocEscala]
		for i in range(0,len(escalaPictograma4)):
			if escalaPictograma4[i]>esperaSeleccion:
				hablar(cuadranteMouse)
				escalaPictograma4=[0,0,0,0]
				print("larga4")
	if len(slides[slideActual].imagenes) == 2:
		if mouseX<=display_width/2:
			cuadranteMouse=0
			escalaPictograma2=[escalaPictograma2[0]+velocEscala,0]
		if mouseX>=display_width/2:
			cuadranteMouse=1
			escalaPictograma2=[0,escalaPictograma2[1]+velocEscala]
		for i in range(0,len(escalaPictograma2)):
			if escalaPictograma2[i]>esperaSeleccion:
				hablar(cuadranteMouse)
				escalaPictograma2=[0,0,0,0]
				print("larga2")


def cambiaSlide(direccion):
	global slideActual
	global pausa
	global txtSlideActual
	pausa=False
	slideActual+=direccion
	if slideActual < 0: slideActual=0
	if slideActual > len(slides)-1: slideActual=len(slides)-1
	txtSlideActual = fuenteArial_50.render(str(slideActual+1), True, (200, 200, 200))
	escalaPictograma4=[0,0,0,0]
	escalaPictograma2=[0,0,0,0]


def game_loop():
	gameExit = False
	while not gameExit:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				gameExit = True
				pygame.quit()
				quit()
			if event.type == pygame.KEYDOWN:
				if  pygame.key.name(event.key) == "escape":
					pygame.quit()
					quit()
				if  pygame.key.name(event.key) == "left":
					print("flecha izq")
					cambiaSlide(-1)
				if  pygame.key.name(event.key) == "right":
					print("flecha der")
					cambiaSlide(1)
			if event.type == pygame.MOUSEMOTION:
				mouseX, mouseY = pygame.mouse.get_pos()
		
		gameDisplay.fill(fondo)
		
		if not pausa : calculaCuadrateMouse(mouseX,mouseY)
		mostrarPictogramas(slideActual)
		gameDisplay.blit(txtEscape,(display_width/2-txtEscape.get_width()/2,display_height-40))
		gameDisplay.blit(txtSlideActual,(display_width/2-txtSlideActual.get_width()/2,display_height-100))
		pygame.display.update()
		clock.tick(30)


locutor = win32com.client.Dispatch("SAPI.SpVoice")

# PYGAME
pygame.init()
clock = pygame.time.Clock()

# PANTALLA
infoPantalla = pygame.display.Info()
display_width = infoPantalla.current_w
display_height =infoPantalla.current_h
gameDisplay = pygame.display.set_mode((display_width,display_height),pygame.FULLSCREEN) #,pygame.RESIZABLE ,pygame.FULLSCREEN
pygame.display.set_caption('BlaBla v00')

# TTS
locutor = win32com.client.Dispatch("SAPI.SpVoice")
#locutor.Speak("¡Empecemos!")

#PRECARGO TODAS LAS slides que hay en una lista para no generar las sub-listas cada vez que se requiere (ahorro recursos)
ruta_app = os.getcwd()  # obtiene ruta del script
slides= cargaSlides()
escalaPictograma4=[0,0,0,0]
escalaPictograma2=[0,0]
slideActual=0
pausa=False

# txt
fuenteArial_15 = pygame.font.SysFont('Arial', 15)
fuenteArial_50 = pygame.font.SysFont('Arial', 50)
txtEscape = fuenteArial_15.render('ESC para salir | ← → para cambiar panel', True, (180, 180, 180))
txtSlideActual = fuenteArial_50.render(str(slideActual+1), True, (180, 180, 180))


game_loop()
pygame.quit()
quit()

# for locucion in slide(1).locucionesArchivos:
# 	locutor.Speak(locucion)