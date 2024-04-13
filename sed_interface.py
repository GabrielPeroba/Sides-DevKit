import tkinter as tk
from PIL import Image, ImageTk
from datetime import datetime
import time
import threading
import numpy as np 
from tkinter import simpledialog


class SmartphoneSimulator:
    def __init__(self, master):
        self.master = master
        self.master.title("Interface")
        self.master.geometry("400x800")

        self.contador = 0
        self.contador2 = 0
        self.contador3 = 0
        self.estado_botao = False
        self.button_id = None


        self.lista_warning = []
        self.lista_tempo = []

        # Carregando a imagem de plano de fundo
        image = Image.open("Diretorio de imagem + wallpaper_3.jpg")
        self.background_image = ImageTk.PhotoImage(image)

        # Configurando o canvas para exibir a imagem
        self.canvas = tk.Canvas(self.master, width=400, height=800)
        self.canvas.pack()
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.background_image)

        self.create_interface()
        self.update_clock()

    def create_interface(self):
        # Widgets
        self.label_text = tk.Label(self.master, text="Toque para começar!", font=("Bahnschrift SemiBold", 24), bg="black", fg="white")
        self.label_text.place(relx=0.5, rely=0.2, anchor=tk.CENTER)


        self.label_text2 = tk.Label(self.master, text="Som", font=("Bahnschrift SemiBold", 24), bg="black", fg="white")
        self.label_text2.place(relx=0.5, rely=0.8, anchor=tk.CENTER)
        self.label_text2.place_forget()
        #self.label_text2.pack_forget()
        

        # Carregando a imagem do botão
        image_button = Image.open("Diretorio de imagem + perfeito.png")
        self.image_button = self.add_transparency(image_button)


        # Usando o Canvas como um botão com fundo transparente
        self.button_id = self.canvas.create_image(200, 380, anchor=tk.CENTER, image=self.image_button, tags="button")
        self.canvas.tag_bind(self.button_id, "<Button-1>", self.button_click)





        imagem = Image.open("Diretorio de imagem + circuito2.png")
        self.image7 = self.add_transparency(imagem)
        # Usando o Canvas para exibir a imagem
        self.image_new = self.canvas.create_image(340, 630, anchor=tk.CENTER, image=self.image7)


        imagem = Image.open("Diretorio de imagem + circuito3.png")
        self.image8 = self.add_transparency(imagem)
        # Usando o Canvas para exibir a imagem
        self.image_newlado = self.canvas.create_image(60, 630, anchor=tk.CENTER, image=self.image8)

        

        




        # Barra no rodapé
        self.footer = tk.Frame(self.master, bg="white")
        self.footer.place(relx=0, rely=1, anchor=tk.SW, relwidth=1, relheight=0.1)


        # Barra no cabeçalho
        self.header = tk.Frame(self.master, bg="white", bd=0.5, relief=tk.SOLID)
        self.header.place(relx=0, rely=0.05, anchor=tk.SW, relwidth=1, relheight=0.05)


        image = Image.open("Diretorio de imagem + wifi.png")
        image = image.convert("RGBA")  # Garantindo que a imagem tenha um canal alfa

        image_imagem = ImageTk.PhotoImage(image)

        label_image = tk.Label(self.master, image=image_imagem, bg="white")
        label_image.image = image_imagem
        label_image.place(relx=0.85, rely=0.027, anchor=tk.CENTER)






        image2 = Image.open("Diretorio de imagem + bateria.png")
        image2 = image2.convert("RGBA")  # Garantindo que a imagem tenha um canal alfa

        image_imagem2 = ImageTk.PhotoImage(image2)

        label_image2 = tk.Label(self.master, image=image_imagem2, bg="white")
        label_image2.image = image_imagem2
        label_image2.place(relx=0.94, rely=0.027, anchor=tk.CENTER)



        image3 = Image.open("Diretorio de imagem + circuito1.png")
        image3 = image3.convert("RGBA")  # Garantindo que a imagem tenha um canal alfa

        image_imagem3 = ImageTk.PhotoImage(image3)






        self.message_label = tk.Message(self.master, text="00:40", font=("Helvetica", 16), bg="white", justify="center", width=200)
        self.message_label.place(relx=0.12, rely=0.027, anchor=tk.CENTER)
        
        

        

        # Carregando as imagens dos botões
        image_button1 = tk.PhotoImage(file="Diretorio de imagem + botao_home.png")
        image_button2 = tk.PhotoImage(file="Diretorio de imagem + botao_linha.png")
        
        image_button3 = tk.PhotoImage(file="Diretorio de imagem + icone_engrenagem.png")
        

        # Botões na barra do rodapé com imagens
        button1 = tk.Button(self.footer, image=image_button1, command=self.show_old_screen, borderwidth=0, bg="white")
        button1.image = image_button1  # Garantindo que a imagem seja mantida em memória
        button1.pack(side=tk.LEFT, padx=80, pady=5)
        button1.place(relx=0.2, rely=0.5, anchor=tk.CENTER)
        

        button2 = tk.Button(self.footer, image=image_button2, borderwidth=0, bg="white", command=self.show_new_screen)
        button2.image = image_button2  # Garantindo que a imagem seja mantida em memória
        button2.pack(side=tk.RIGHT, padx=50, pady=5)
        button2.place(relx=0.5, rely=0.5, anchor=tk.CENTER)


        button3 = tk.Button(self.footer, image=image_button3, borderwidth=0, bg="white", command=self.show_option_screen)
        button3.image = image_button3  # Garantindo que a imagem seja mantida em memória
        button3.pack(side=tk.RIGHT, padx=70, pady=5)
        button3.place(relx=0.78, rely=0.5, anchor=tk.CENTER)






    def button1_click(self):
        print("Botao foi clicado!")
        

    def button2_click(self):
        print("Botao foi clicado!")
        


    def add_transparency(self, image):
        

        alpha = image.split()[3]
        image = image.convert("RGBA")
        image.putalpha(alpha)
        return ImageTk.PhotoImage(image)




         

    def button_click(self, id):
        print("Botao foi clicado!")

        self.estado_botao = not self.estado_botao

        if self.estado_botao == True:
            self.update_text()
            self.label_text2.place(relx=0.5, rely=0.8, anchor=tk.CENTER)
            

        else:
            print("Botao foi clicado!")
            self.label_text2.place_forget()
       


    def show_new_screen(self):
        new_screen = SecondScreen(self.master)
        self.canvas.delete(self.button_id)
        self.label_text.destroy()
        self.canvas.delete(self.image_new)
        self.canvas.delete(self.image_newlado)

        # Widget
        self.label_text = tk.Label(self.master, text="Linha do Tempo", font=("Bahnschrift SemiBold", 24), bg="black", fg="white")
        self.label_text.place(relx=0.5, rely=0.2, anchor=tk.CENTER)


        self.image5 = Image.open("Diretorio de imagem + linha_do_tempo.png")
        self.image5 = self.add_transparency(self.image5)
        # Usando o Canvas para exibir a imagem
        self.image_id_second_screen = self.canvas.create_image(50, 400, anchor=tk.CENTER, image=self.image5)


        self.image6 = Image.open("Diretorio de imagem + linha_zoom.png")
        self.image6 = self.add_transparency(self.image6)
        # Usando o Canvas para exibir a imagem
        self.imagenova = self.canvas.create_image(50,620, anchor=tk.CENTER, image=self.image6)



        # Widget
        self.label_text3 = tk.Label(self.master, text="-  Aviso  -", font=("Bahnschrift SemiBold", 15), bg="black", fg="white")
        self.label_text3.place(relx=0.3, rely=0.363, anchor=tk.CENTER)


        # Widget
        self.label_text4 = tk.Label(self.master, text=self.lista_tempo[-1], font=("Bahnschrift SemiBold", 15), bg="black", fg="white")
        self.label_text4.place(relx=0.5, rely=0.363, anchor=tk.CENTER)


        # Widget
        self.label_text5 = tk.Label(self.master, text="Som: ", font=("Bahnschrift SemiBold", 15), bg="black", fg="white")
        self.label_text5.place(relx=0.7, rely=0.363, anchor=tk.CENTER)


        # Widget
        self.label_text5 = tk.Label(self.master, text=self.label, font=("Bahnschrift SemiBold", 15), bg="black", fg="white")
        self.label_text5.place(relx=0.9, rely=0.363, anchor=tk.CENTER)





    def show_option_screen(self):


        #Terceira tela
        new_screen = SecondScreen(self.master)
        self.canvas.delete(self.button_id)
        self.label_text.destroy()
        self.canvas.delete(self.image_new)
        self.canvas.delete(self.image_newlado)


        background_image = Image.open("Diretorio de imagem + background_image.png")
        background_image = background_image.convert("RGBA") 

        image_background = ImageTk.PhotoImage(background_image)

        image_background = tk.Label(self.master, image=image_background, bg="white")
        image_background.image = image_background
        image_background.place(relx=0.5, rely=0.475, anchor=tk.CENTER)

        



        #Imagens de botoes com texto
        image_b = Image.open("Diretorio de imagem + botao_opcoes.png")
        image_b = image_b.convert("RGBA") 

        image_imagemb = ImageTk.PhotoImage(image_b)

        label_imageb = tk.Label(self.master, image=image_imagemb, bg="white")
        label_imageb.image = image_imagemb
        label_imageb.place(relx=0.5, rely=0.3, anchor=tk.CENTER)




        image_circuito = Image.open("Diretorio de imagem + circuito_opcoes.png")
        image_circuito = image_circuito.convert("RGBA") 

        image_imagemcircuito = ImageTk.PhotoImage(image_circuito)

        label_imagecircuito = tk.Label(self.master, image=image_imagemcircuito, bg="white")
        label_imagecircuito.image = image_imagemcircuito
        label_imagecircuito.place(relx=0.93, rely=0.75, anchor=tk.CENTER)






        image_circuito = Image.open("Diretorio de imagem + circuito_opcoes2.png")
        image_circuito = image_circuito.convert("RGBA") 

        image_imagemcircuito = ImageTk.PhotoImage(image_circuito)

        label_imagecircuito = tk.Label(self.master, image=image_imagemcircuito, bg="white")
        label_imagecircuito.image = image_imagemcircuito
        label_imagecircuito.place(relx=0.07, rely=0.75, anchor=tk.CENTER)





        image_c = Image.open("Diretorio de imagem + botao_opcoes.png")
        image_c = image_c.convert("RGBA") 

        image_imagemc = ImageTk.PhotoImage(image_c)

        label_imagec = tk.Label(self.master, image=image_imagemc, bg="white")
        label_imagec.image = image_imagemc
        label_imagec.place(relx=0.5, rely=0.4, anchor=tk.CENTER)




        image_d = Image.open("Diretorio de imagem + botao_opcoes.png")
        image_d = image_d.convert("RGBA") 

        image_imagemd = ImageTk.PhotoImage(image_d)

        label_imaged = tk.Label(self.master, image=image_imagemd, bg="white")
        label_imaged.image = image_imagemd
        label_imaged.place(relx=0.5, rely=0.5, anchor=tk.CENTER)





        image_f = Image.open("Diretorio de imagem + botao_opcoes.png")
        image_f = image_f.convert("RGBA") 

        image_imagemf = ImageTk.PhotoImage(image_f)

        label_imagef = tk.Label(self.master, image=image_imagemf, bg="white")
        label_imagef.image = image_imagemf
        label_imagef.place(relx=0.5, rely=0.7, anchor=tk.CENTER)




        image_e = Image.open("Diretorio de imagem + botao_opcoes.png")
        image_e = image_d.convert("RGBA") 

        image_imageme = ImageTk.PhotoImage(image_e)

        label_imagee = tk.Label(self.master, image=image_imageme, bg="white")
        label_imagee.image = image_imageme
        label_imagee.place(relx=0.5, rely=0.6, anchor=tk.CENTER)



        image_h = Image.open("Diretorio de imagem + botao_opcoes.png")
        image_h = image_h.convert("RGBA") 

        image_imagemh = ImageTk.PhotoImage(image_h)

        label_imageh = tk.Label(self.master, image=image_imagemh, bg="white")
        label_imageh.image = image_imagemh
        label_imageh.place(relx=0.5, rely=0.8, anchor=tk.CENTER)



        image_rodape = Image.open("Diretorio de imagem + barra.png")
        image_rodape = image_rodape.convert("RGBA") 

        image_imagemrodape = ImageTk.PhotoImage(image_rodape)

        label_imagerodape = tk.Label(self.master, image=image_imagemrodape, bg="white")
        label_imagee.imagrodape = image_imagemrodape
        label_imagerodape.place(relx=0.5, rely=0.075, anchor=tk.CENTER)





        image_rodape1 = Image.open("Diretorio de imagem + barra.png")
        image_rodape1 = image_rodape1.convert("RGBA") 

        image_imagemrodape1 = ImageTk.PhotoImage(image_rodape1)

        label_imagerodape1 = tk.Label(self.master, image=image_imagemrodape1, bg="white")
        label_imagee.imagrodape1 = image_imagemrodape1
        label_imagerodape1.place(relx=0.5, rely=0.9, anchor=tk.CENTER)














        

        self.label_text = tk.Label(self.master, text="Configurações", font=("Bahnschrift SemiBold", 24), bg="white", fg="black")
        self.label_text.place(relx=0.5, rely=0.15, anchor=tk.CENTER)

        self.label_text = tk.Label(self.master, text="Edite os ajustes da detecção de sons", font=("Bahnschrift SemiBold", 16), bg="white", fg="black")
        self.label_text.place(relx=0.5, rely=0.20, anchor=tk.CENTER)



        

       

        button_rate = tk.Button(root, text="# de MFCCs", borderwidth=0, bg="white", command=self.save_text)
        button_rate.pack(side=tk.RIGHT, padx=70, pady=70)
        button_rate.place(relx=0.5, rely=0.3, anchor=tk.CENTER)

        button_rate = tk.Button(root, text="Intervalo de Detecção", borderwidth=0, bg="white", command=self.save_text)
        button_rate.pack(side=tk.RIGHT, padx=70, pady=70)
        button_rate.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

        button_rate = tk.Button(root, text="Freq. de Captação", borderwidth=0, bg="white", command=self.save_text)
        button_rate.pack(side=tk.RIGHT, padx=70, pady=70)
        button_rate.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        button_rate = tk.Button(root, text="Windowing", borderwidth=0, bg="white", command=self.save_text)
        button_rate.pack(side=tk.RIGHT, padx=70, pady=70)
        button_rate.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

        button_rate = tk.Button(root, text="Avisos", borderwidth=0, bg="white", command=self.save_text)
        button_rate.pack(side=tk.RIGHT, padx=70, pady=70)
        button_rate.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

        button_rate = tk.Button(root, text="Escolha do Modelo", borderwidth=0, bg="white", command=self.save_text)
        button_rate.pack(side=tk.RIGHT, padx=70, pady=70)
        button_rate.place(relx=0.5, rely=0.8, anchor=tk.CENTER)





       
        
        


    def show_old_screen(self):

        self.label_text.destroy()
        self.label_text3.destroy()
        #self.label_text4.destroy()
        self.label_text5.destroy()
        self.canvas.delete(self.imagenova)
        self.canvas.delete(self.image_id_second_screen)
        
        self.button_id = self.canvas.create_image(200, 400, anchor=tk.CENTER, image=self.image_button, tags="button")
        self.canvas.tag_bind(self.button_id, "<Button-1>", self.button_click)

        self.label_text = tk.Label(self.master, text="Toque para começar!", font=("Bahnschrift SemiBold", 24), bg="black", fg="white")
        self.label_text.place(relx=0.5, rely=0.2, anchor=tk.CENTER)


        imagem = Image.open("Diretorio de imagem + circuito2.png")
        self.image7 = self.add_transparency(imagem)
        # Usando o Canvas para exibir a imagem
        self.image_new = self.canvas.create_image(340, 630, anchor=tk.CENTER, image=self.image7)


        imagem = Image.open("Diretorio de imagem + circuito3.png")
        self.image8 = self.add_transparency(imagem)
        # Usando o Canvas para exibir a imagem
        self.image_newlado = self.canvas.create_image(60, 630, anchor=tk.CENTER, image=self.image8)
        


    def update_clock(self):
        # Obtemos o horário atual
        current_time = datetime.now().strftime("%H:%M:%S")

        # Atualizamos o texto do rótulo
        self.message_label.config(text=current_time)

        # Chamamos a função novamente após um intervalo (1000 milissegundos = 1 segundo)
        self.master.after(1000, self.update_clock)


    def update_text(self):


        new_text="Escutando"
        new_text1="Escutando."
        new_text2="Escutando.."
        new_text3="Escutando..."



        if(self.estado_botao == False):
            self.label_text["text"] = "Toque para começar"
            return 0
    

        elif(self.estado_botao == True):
            
            if(self.contador == 0 or self.contador == 4 ):
            
                self.label_text["text"] = new_text
                self.contador=0


            elif(self.contador == 1):
                self.label_text["text"] = new_text1


            elif(self.contador == 2):
                self.label_text["text"] = new_text2


            elif(self.contador == 3):
                self.label_text["text"] = new_text3
            


            with open("compartilhado.txt", "r") as file:
                
                data = file.read()


            with open('compartilhado2.txt', 'r') as arquivo:
                data_warning = arquivo.read()
                print(data_warning)
                

            with open("compartilhado3.txt", "r") as file:
                
                self.label = file.read()

            
            
            self.label_text2["text"] = data

            self.lista_warning.append(data_warning)


            warning=self.lista_warning[self.contador2]


            
            if(warning=="1"):

                self.contador3=1
                
                self.image6 = Image.open("Diretorio de imagem + icone_aviso.png")
                self.image6 = self.image6.convert("RGBA")
                self.image6 = self.add_transparency(self.image6)

                # Usando o Canvas para exibir a imagem
                self.image_aviso = self.canvas.create_image(360, 585, anchor=tk.CENTER, image=self.image6)

                self.lista_warning.append(data_warning)
                self.lista_tempo.append(datetime.now().strftime("%H:%M:%S"))


                

            


            elif(warning=="0" and self.contador3==1):

                self.canvas.delete(self.image_aviso)
                self.contador3=0

            

            self.contador=self.contador+1

            
                
        self.contador2=self.contador2+1

            
        self.master.after(1000, self.update_text)






    def save_text(self, event=None):
        text = simpledialog.askstring("Input", "Digite seu texto:")
        if text is not None:
            #Pop-up para atribuir parametreo
            print("Texto digitado:", text)
        else:
            print("Nenhum texto foi digitado")

        root = tk.Tk()
        root.title("Exemplo")


class SecondScreen:
    #segunda tela da interface
    def __init__(self, master):
        self.master = master
        self.master.title("Segunda Tela")
        self.master.geometry("400x800")

        self.create_widgets()



    def destroy_label_text(self):
        # Destruir o label_text
        self.label_text.destroy()




    def add_transparency(self, image):
       
        alpha = image.split()[3]
        image = image.convert("RGBA")
        image.putalpha(alpha)
        return ImageTk.PhotoImage(image)
    

    def create_widgets(self):


        print("aaaaa")







#Funcao main
if __name__ == "__main__":
    root = tk.Tk()
    app = SmartphoneSimulator(root)
    root.mainloop()
