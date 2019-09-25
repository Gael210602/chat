from tkinter import *
import time, socket, sys

soc = socket.socket()
shost = socket.gethostname()
ip = socket.gethostbyname(shost)
#get information to connect with the server
direccionn=("Cliente en: ",'({})'.format(ip))
stringx=""

root = Tk()
root.title("Cliente")
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

servidor= Label(root, text="Ip del servidor")
servidor.place(x=0, y=550,width=100, height=50)

servidorr= Entry(root)
servidorr.place(x=100, y=550,width=200, height=50)

obtenerserver=Button(root, text="Enviar ip y nombre", command=lambda:ipdelservidor())
obtenerserver.place(x=300, y=550, width=100,height=50)

Labelnombre=Label(root, text="Nombre de usuario")
Labelnombre.place(x=300, y=500,width=100, height=50)
Nombre = Entry(root)
Nombre.place(x=400, y=500,width=200, height=50)

salida=Label(root, background="red")
salida.place(x=100, y=25, width=400, height=350)

Nombreestatico=Label(root)
ipestatica=Label(root)

salida=Label(root, background="red")
salida.place(x=100, y=25, width=400, height=350)

name=""
server_name=""

def ipdelservidor():
   global server_name
   global stringx
   global soc
   global name
   server_host = servidorr.get()
   name = Nombre.get()
   Nombreestatico.configure(text=name)
   Nombreestatico.place(x=400, y=500,width=200, height=50)
   ipestatica.configure(text=server_host)
   ipestatica.place(x=100, y=550,width=200, height=50)

   port = 1234
   stringx=stringx,('Conectando al servidor: {}, ({})'.format(server_host, port)),"\n"
   salida.configure(text=stringx)
   soc.connect((server_host, port))
   stringx=stringx,("Conectado...\n")
   salida.configure(text=stringx)
   soc.send(name.encode())
   server_name = soc.recv(1024)
   server_name = server_name.decode()
   stringx=stringx,('{} se ha unido...'.format(server_name))
   salida.configure(text=stringx)

def recibir():
   global server_name
   global name
   global stringx
   global soc
   message = soc.recv(1024)
   message = message.decode()
   stringx=stringx,(server_name, ">", message),"\n"
   salida.configure(text=stringx)

def enviarmensaje():
   global server_name
   global stringx
   global soc
   message = Entrada.get()
   stringx="\n",stringx,name,">",message,"\n"
   salida.configure(text=stringx)
   soc.send(message.encode())
   recibir()





root.mainloop()








