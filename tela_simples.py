import tkinter as tk
import webbrowser

# Função para abrir o primeiro link no navegador
def abrir_primeiro_link():
    url = "https://www.yout-ube.com/watch?v=dQw4w9WgXcQ"
    webbrowser.open(url)

# Função para abrir o segundo link no navegador
def abrir_segundo_link():
    url = "https://www.yout-ube.com/watch?si=YmiH2ANnW1yTrG6A&v=TZEijhxnXm4&feature=youtu.be"
    webbrowser.open(url)

# Criação da janela principal
root = tk.Tk()
root.title("Tela Simples")

# Criação de um rótulo
label = tk.Label(root, text="Olá, Mundo!")
label.pack(pady=20)

# Criação do primeiro botão
button1 = tk.Button(root, text="Clique Aqui", command=abrir_primeiro_link)
button1.pack(pady=10)

# Criação do segundo botão
button2 = tk.Button(root, text="Outro Link", command=abrir_segundo_link)
button2.pack(pady=10)

# Execução do loop principal da interface gráfica
root.mainloop()
