import tkinter as tk
import webbrowser

# Função para abrir o link no navegador
def abrir_link():
    url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    webbrowser.open(url)

# Criação da janela principal
root = tk.Tk()
root.title("Tela Simples")

# Criação de um rótulo
label = tk.Label(root, text="Olá, Mundo!")
label.pack(pady=20)

# Criação de um botão
button = tk.Button(root, text="Clique Aqui", command=abrir_link)
button.pack(pady=10)

# Execução do loop principal da interface gráfica
root.mainloop()
