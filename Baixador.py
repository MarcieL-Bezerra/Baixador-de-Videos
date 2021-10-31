from pytube import YouTube
from tkinter import *
import tkinter.messagebox as tkMessageBox
import os
import tkinter.filedialog as fdlg
from tkinter import ttk



def saindo():
	result = tkMessageBox.askquestion("", "Confirma a saída?", icon='question')
	if result=='yes':
		os._exit(1)
	else:
		pass
def limpar():
	txtLink.delete(0,"end")

def baixardor():
	progress1['value']+=10
	tela.update()
	try:
		site = txtLink.get()
		

		#salvar = r"C:\Users\Marciel\Videos"
		progress1['value']+=10
		tela.update()

		tube = YouTube(site)
		progress1['value']+=10
		tela.update()

		'''print("Titulo : ", tube.title)
		print("Numero de views : ", tube.views)
		print("tamanho : ", tube.length)
		print("avaliação : ", tube.rating)'''


		tubes = tube.streams.get_highest_resolution()
		progress1['value']+=10
		tela.update()

		tkMessageBox.showinfo("Selecionar Pasta", message= "Selecione Pasta para salvar!")

		#aqui seleciona a pasta a ser colocada o novo arquivo
		opcoes = {}                # as opções são definidas em um dicionário
		opcoes['initialdir'] = ''    # será o diretório atual
		opcoes['parent'] = tela
		opcoes['title'] = 'Escolha a pasta para salvar'
		caminhosalvar = fdlg.askdirectory(**opcoes)

		progress1['value']+=10
		tela.update()

		tubes.download(caminhosalvar)
		progress1.stop()
		tkMessageBox.showinfo("Finalzado", message= "Finalizado verifique em : " + str(caminhosalvar))
		limpar()

	except:
		progress1.stop()
		tkMessageBox.showinfo("Erro", message= "Não foi possível finalizar!!")

def progresso():
	site = txtLink.get()
	if site == "":
		tkMessageBox.showinfo("Erro", message= "Favor preencher o site!!")
	else:
		progress1.start(10)
		baixardor()


tela = Tk()
tela.title("Download De Videos")
tela.geometry("800x500+400+0")
tela['bg'] = "OrangeRed"
tela.iconphoto(True, PhotoImage(file='./arquivos/foto.png'))

lblLink = Label(tela, bg="DarkOrange", text = "Site: ",font=('arial',14,'bold'))
lblLink.place(relx = 0.2, rely = 0.2)

txtLink = Entry(tela, font=('arial',14, 'bold'))
txtLink.place(relx=0.3, rely=0.2)



btinicio = Button(tela, text = " Iniciar  ",bg="DarkOrange", font=('arial',14,'bold'),command=progresso)
btinicio.place(relx = 0.2, rely = 0.5)

btinicio = Button(tela, text = " Limpar  ",bg="DarkOrange", font=('arial',14,'bold'),command=limpar)
btinicio.place(relx = 0.4, rely = 0.5)

btsair = Button(tela, text = "   Sair   ",bg="DarkOrange", font=('arial',14,'bold'),command=saindo)
btsair.place(relx = 0.6, rely = 0.5)

#importante para progressbar
s = ttk.Style() 
s.theme_use('default') 
s.configure("SKyBlue1.Horizontal.TProgressbar", foreground='DarkSeaGreen3', background='white')

progress1 =ttk.Progressbar(tela, orient=VERTICAL, length=450, style="SKyBlue1.Horizontal.TProgressbar",mode='determinate')
progress1.place(relx=0.005, rely = 0)

tela.mainloop()


