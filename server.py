from tkinter import*
import re, time, socket, sys

time.sleep(1)
soc = socket.socket()
host_name = socket.gethostname()
ip = socket.gethostbyname(host_name)
port = 1234
soc.bind((host_name, port))
direccionn=("El servidor está hospedado en", '({})'.format(ip))
#Fin servidor
stringx=""
root = Tk()
root.title("Servidor")
root.geometry("600x600")
root.resizable(False, False)

texto= Label(root, text="Ingrese su mensaje")
texto.place(x=0, y=400,width=100, height=50)

Entrada = Entry(root)
Entrada.place(x=100, y=400,width=400, height=50)

Enviar=Button(root, text="Enviar", command=lambda:enviarmensaje())
Enviar.place(x=500, y=400,width=100, height=50)

direccionn= Label(root, text=direccionn)
direccionn.place(x=0, y=500,width=300, height=50)


Nombre = Entry(root, text="Ingrese el nombre de su usuario")
Nombre.place(x=300, y=500,width=200, height=50)

Labelnombre=Label(root)

salida=Label(root, background="red")
salida.place(x=100, y=25, width=400, height=350)


obtenernombre=Button(root, text="Definir nombre", command=lambda:iniciochido())
obtenernombre.place(x=500, y=500,width=100, height=50)
name=""
stringx=""
connection=""
client_name=""
def iniciar():
	global stringx
	global connection
	global client_name
	global name
	soc.listen(1)
	stringx="Esperando conexiones \n"
	salida.configure(text=stringx)
	connection, addr = soc.accept()
	stringx=stringx,"Conexion recibida de ", addr[0], "(", addr[1], ")\n"
	salida.configure(text=stringx)
	stringx=stringx,'Connexión establecida con: {}, ({})'.format(addr[0], addr[0]),"\n"
	salida.configure(text=stringx)
	#get a connection from client side
	client_name = connection.recv(1024)
	client_name = client_name.decode()
	stringx=stringx,client_name + ' Se ha conectado.',"\n"
	salida.configure(text=stringx)
	connection.send(name.encode())
def Recibir():
	global client_name
	global stringx
	message = connection.recv(1024)
	message = message.decode()
	stringx="\n",stringx,(client_name, '>', message),"\n"
	salida.configure(text=stringx)

def enviarmensaje():
	global stringx
	global connection
	global client_name
	global name

	message = Entrada.get()
	stringx="\n",stringx, name,message,"\n"
	salida.configure(text=stringx)
	connection.send(message.encode())
	Recibir()
def iniciochido():
	global name
	name=Nombre.get()
	Labelnombre.configure(text=("Nombre del usuario: ",name))
	Labelnombre.place(x=300, y=500,width=200, height=50)
	iniciar()
root.mainloop()


	