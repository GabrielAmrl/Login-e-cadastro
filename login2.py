import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import webbrowser

# Dicionário para armazenar os dados dos usuários
usuarios = {}

def cadastrar_usuario():
    nome = cadastro_nome_entry.get()
    email = cadastro_email_entry.get()
    senha = cadastro_senha_entry.get()

    # Verifica se o e-mail já está cadastrado
    if email in usuarios:
        messagebox.showerror("Erro", "E-mail já cadastrado. Tente fazer login.")
    else:
        usuarios[email] = {'nome': nome, 'senha': senha}
        messagebox.showinfo("Sucesso", "Cadastro realizado com sucesso!")
        # Limpa os campos após o cadastro
        cadastro_nome_entry.delete(0, tk.END)
        cadastro_email_entry.delete(0, tk.END)
        cadastro_senha_entry.delete(0, tk.END)
        # Muda para a tela de login
        mostrar_tela_login()

def fazer_login():
    email = login_email_entry.get()
    senha = login_senha_entry.get()

    # Verifica se o e-mail está cadastrado e se a senha está correta
    if email in usuarios and usuarios[email]['senha'] == senha:
        messagebox.showinfo("Bem-vindo", f"Bem-vindo, {usuarios[email]['nome']}!")

        # Abrir o link da web após o login
        webbrowser.open("https://solidcon.com.br")

    else:
        messagebox.showerror("Erro", "E-mail ou senha incorretos. Tente novamente.")

def mostrar_tela_cadastro():
   
    tela_login.pack_forget()
    
    tela_cadastro.pack()

def mostrar_tela_login():
    
    tela_cadastro.pack_forget()
 
    tela_login.pack()


root = tk.Tk()
root.title("Cadastro de Usuário")


icone_path = "images.png"
icone = ImageTk.PhotoImage(Image.open(icone_path))

root.iconphoto(True, icone)

cor_de_fundo = "#8B0000"  
root.configure(bg=cor_de_fundo)

tela_login = tk.Frame(root, bg=cor_de_fundo)

tk.Label(tela_login, text="Login", bg=cor_de_fundo, fg="white", font=("Helvetica", 16)).grid(row=0, column=0, columnspan=2, pady=10)

tk.Label(tela_login, text="E-mail:", bg=cor_de_fundo, fg="white").grid(row=1, column=0, padx=10, pady=5)
login_email_entry = tk.Entry(tela_login)
login_email_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(tela_login, text="Senha:", bg=cor_de_fundo, fg="white").grid(row=2, column=0, padx=10, pady=5)
login_senha_entry = tk.Entry(tela_login, show='*')
login_senha_entry.grid(row=2, column=1, padx=10, pady=5)

login_button = tk.Button(tela_login, text="Login", command=fazer_login, bg="#5D0000", fg="white")  # Cor mais escura do vinho
login_button.grid(row=3, column=0, columnspan=2, pady=10)

cadastro_button = tk.Button(tela_login, text="Cadastrar", command=mostrar_tela_cadastro, bg="#5D0000", fg="white")  # Cor mais escura do vinho
cadastro_button.grid(row=4, column=0, columnspan=2, pady=10)

tela_cadastro = tk.Frame(root, bg=cor_de_fundo)

tk.Label(tela_cadastro, text="Cadastro de Usuário", bg=cor_de_fundo, fg="white", font=("Helvetica", 16)).grid(row=0, column=0, columnspan=2, pady=10)

tk.Label(tela_cadastro, text="Nome:", bg=cor_de_fundo, fg="white").grid(row=1, column=0, padx=10, pady=5)
cadastro_nome_entry = tk.Entry(tela_cadastro)
cadastro_nome_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(tela_cadastro, text="E-mail:", bg=cor_de_fundo, fg="white").grid(row=2, column=0, padx=10, pady=5)
cadastro_email_entry = tk.Entry(tela_cadastro)
cadastro_email_entry.grid(row=2, column=1, padx=10, pady=5)

tk.Label(tela_cadastro, text="Senha:", bg=cor_de_fundo, fg="white").grid(row=3, column=0, padx=10, pady=5)
cadastro_senha_entry = tk.Entry(tela_cadastro, show='*')
cadastro_senha_entry.grid(row=3, column=1, padx=10, pady=5)

cadastrar_button = tk.Button(tela_cadastro, text="Cadastrar", command=cadastrar_usuario, bg="#5D0000", fg="white")  # Cor mais escura do vinho
cadastrar_button.grid(row=4, column=0, columnspan=2, pady=10)

mostrar_tela_login()


root.mainloop()
