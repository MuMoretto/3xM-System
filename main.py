import customtkinter as ctk
from program_functions.system_menu import showMenu

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

def verificar_login(event=None):
    usuario = entry_usuario.get()
    senha = entry_senha.get()

    if usuario == "tester" and senha == "0123":
        label_erro.configure(text="Login realizado!")
        showMenu(janela)
    else:
        label_erro.configure(text="Usuário ou senha incorretos!")

def mostrar_senha():
    if entry_senha.cget("show") == "*":
        entry_senha.configure(show="")
    else:
        entry_senha.configure(show="*")

janela = ctk.CTk()
janela.title("3xM - Login")

largura = 900
altura = 600

screen_w = janela.winfo_screenwidth()
screen_h = janela.winfo_screenheight()

x = int((screen_w/2) - (largura/2))
y = int((screen_h/2) - (altura/2))

janela.geometry(f"{largura}x{altura}+{x}+{y}")

card = ctk.CTkFrame(
    janela,
    width=500,
    height=420,
    corner_radius=25
)

card.place(relx=0.5, rely=0.5, anchor="center")
card.pack_propagate(False)

titulo = ctk.CTkLabel(
    card,
    text="Bem-Vindo ao 3xM System",
    font=("Arial", 28, "bold")
)
titulo.pack(pady=30)

entry_usuario = ctk.CTkEntry(
    card,
    placeholder_text="👤 Usuário",
    width=300,
    height=45,
    corner_radius=15,
    font=("Arial", 14)
)
entry_usuario.pack(pady=15)

frame_senha = ctk.CTkFrame(card, fg_color="transparent")
frame_senha.pack(pady=15)

entry_senha = ctk.CTkEntry(
    frame_senha,
    placeholder_text="🔒 Senha",
    width=250,
    height=45,
    show="*",
    corner_radius=15,
    font=("Arial", 14)
)
entry_senha.pack(side="left")

botao_olho = ctk.CTkButton(
    frame_senha,
    text="👁",
    width=45,
    height=45,
    command=mostrar_senha
)
botao_olho.pack(side="left", padx=5)

botao_login = ctk.CTkButton(
    card,
    text="Entrar",
    width=300,
    height=45,
    corner_radius=15,
    font=("Arial", 15, "bold"),
    command=verificar_login
)
botao_login.pack(pady=25)

label_erro = ctk.CTkLabel(
    card,
    text="",
    text_color="red"
)
label_erro.pack()

janela.bind("<Return>", verificar_login)

janela.mainloop()