from pytube import YouTube
from tkinter import *
import tkinter.messagebox as tkMessageBox
import os
import tkinter.filedialog as fdlg
from tkinter import ttk

def selecionado(event,textnome):
    textnome.delete(0,'end')
    textnome.config(fg='black')

def deselecionado(event,textnome):
    if textnome.get()=="":
        textnome.insert(0,'**Site obrigatório!')
        textnome.config(fg='red')
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
	site = txtLink.get()
	progress1['value']+=10
	tela.update()
	try:
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
	if site == "" or site == '**Site obrigatório!' or site == 'Site':
		tkMessageBox.showinfo("Erro", message= "Favor preencher o site!!")
	else:
		if escolhido =="mp4":
			progress1.start(10)
			baixadormp4()
		else:
			progress1.start(10)
			baixadormp3()


tela = Tk()
tela.title("Download De Videos MP4 e MP3")
tela.geometry("800x500+400+0")
tela['bg'] = "OrangeRed"
tela.iconphoto(True, PhotoImage(file='./arquivos/foto.png'))

image=PhotoImage(file='./arquivos/foto2.png')

campointervalo = Label(tela, width=800,height=500,image=image, bd=3,fg='black',bg = 'black', font=('arial',10,'bold'))
campointervalo.grid(rowspan=10,columnspan =5)

lblLink = Label(tela, bg="DarkOrange", text = "**Site: ",font=('arial',14,'bold'))
lblLink.place(relx = 0.2, rely = 0.2)

txtLink = Entry(tela,justify='center',fg='red', font=('arial',14, 'bold'))
txtLink.place(relx=0.3, rely=0.2)
txtLink.insert(0,'Site')
txtLink.bind('<FocusIn>', lambda event=txtLink, btn=txtLink: selecionado(event,btn))
txtLink.bind('<FocusOut>', lambda event=txtLink, btn=txtLink: deselecionado(event,btn))




btinicio = Button(tela, text = " Baixar MP4  ",bg="DarkOrange", font=('arial',14,'bold'),command=lambda: progresso('mp4'))
btinicio.place(relx = 0.1, rely = 0.8)

btimusica = Button(tela, text = " Baixar MP3  ",bg="DarkOrange", font=('arial',14,'bold'),command=lambda: progresso('mp3'))
btimusica.place(relx = 0.3, rely = 0.8)

btilimpa = Button(tela, text = " Limpar  ",bg="DarkOrange", font=('arial',14,'bold'),command=limpar)
btilimpa.place(relx = 0.5, rely = 0.8)

btsair = Button(tela, text = "   Sair   ",bg="DarkOrange", font=('arial',14,'bold'),command=saindo)
btsair.place(relx = 0.7, rely = 0.8)

#importante para progressbar
s = ttk.Style() 
s.theme_use('default') 
s.configure("SKyBlue1.Horizontal.TProgressbar", foreground='red', background='white')

progress1 =ttk.Progressbar(tela, orient=VERTICAL, length=450, style="SKyBlue1.Horizontal.TProgressbar",mode='determinate')
progress1.place(relx=0.005, rely = 0)

tela.mainloop()



