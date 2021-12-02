from pytube import YouTube
from tkinter import *
import tkinter.messagebox as tkMessageBox
import os
import tkinter.filedialog as fdlg
from tkinter import ttk
import youtube_dl



def saindo():
	result = tkMessageBox.askquestion("", "Confirma a saída?", icon='question')
	if result=='yes':
		os._exit(1)
	else:
		pass
def limpar():
	txtLink.delete(0,"end")

def baixadormp3():
	progress1['value']+=10
	tela.update()

	video_url = txtLink.get()
	video_info = youtube_dl.YoutubeDL().extract_info(
	url = video_url,download=False
	)
	filename = f"{video_info['title']}.mp3"
	options={
		'format':'bestaudio/best',
		'keepvideo':False,
		'outtmpl':filename,
	}

	with youtube_dl.YoutubeDL(options) as ydl:
		ydl.download([video_info['webpage_url']])

	tkMessageBox.showinfo("Download complete... {}".format(filename))

def baixadormp4():
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

def progresso(escolhido):
	site = txtLink.get()
	if site == "":
		tkMessageBox.showinfo("Erro", message= "Favor preencher o site!!")
	else:
		if escolhido =="mp4":
			progress1.start(10)
			baixadormp4()
		else:
			progress1.start(10)
			baixadormp3()


tela = Tk()
tela.title("Download De Videos")
tela.geometry("800x500+400+0")
tela['bg'] = "OrangeRed"
tela.iconphoto(True, PhotoImage(file='./arquivos/foto.png'))
image=PhotoImage(file='./arquivos/foto2.png')

campointervalo = tk.Label(tela, width=800,height=500,image=image, bd=3,fg='black',bg = 'white', font=('arial',10,'bold'))
campointervalo.grid(rowspan=16,columnspan =5)

lblLink = Label(tela, bg="DarkOrange", text = "Site: ",font=('arial',14,'bold'))
lblLink.place(relx = 0.2, rely = 0.2)

txtLink = Entry(tela, font=('arial',14, 'bold'))
txtLink.place(relx=0.3, rely=0.2)



btinicio = Button(tela, text = " Baixar MP4  ",bg="DarkOrange", font=('arial',14,'bold'),command=lambda: progresso('mp4'))
btinicio.place(relx = 0.1, rely = 0.5)

btimusica = Button(tela, text = " Baixar MP3  ",bg="DarkOrange", font=('arial',14,'bold'),command=lambda: progresso('mp3'))
btimusica.place(relx = 0.3, rely = 0.5)

btilimpa = Button(tela, text = " Limpar  ",bg="DarkOrange", font=('arial',14,'bold'),command=limpar)
btilimpa.place(relx = 0.5, rely = 0.5)

btsair = Button(tela, text = "   Sair   ",bg="DarkOrange", font=('arial',14,'bold'),command=saindo)
btsair.place(relx = 0.7, rely = 0.5)

#importante para progressbar
s = ttk.Style() 
s.theme_use('default') 
s.configure("SKyBlue1.Horizontal.TProgressbar", foreground='DarkSeaGreen3', background='white')

progress1 =ttk.Progressbar(tela, orient=VERTICAL, length=450, style="SKyBlue1.Horizontal.TProgressbar",mode='determinate')
progress1.place(relx=0.005, rely = 0)

tela.mainloop()


