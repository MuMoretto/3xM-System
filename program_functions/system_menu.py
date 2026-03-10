import customtkinter as ctk
from program_functions.system_vendas import abrir_vendas
from program_functions.system_clientes import abrir_clientes
from program_functions.system_produtos import abrir_produtos

def showMenu(mainWindow):

    # esconder login
    mainWindow.withdraw()

    menuWindow = ctk.CTkToplevel()
    menuWindow.title("3xM System - Menu")
    menuWindow.state("zoomed")

    # CARD CENTRAL
    card = ctk.CTkFrame(
        menuWindow,
        width=800,
        height=500,
        corner_radius=25
    )
    card.place(relx=0.5, rely=0.5, anchor="center")

    card.grid_propagate(False)

    # TÍTULO
    titulo = ctk.CTkLabel(
        card,
        text="Menu Principal",
        font=("Arial", 32, "bold")
    )
    titulo.pack(pady=40)

    # BOTÕES DO SISTEMA
    botao_clientes = ctk.CTkButton(
        card,
        text="🧍 Clientes", font=("Arial", 25, "bold"),
        width=250,
        height=40,
        command=lambda: abrir_clientes(menuWindow)
    )
    botao_clientes.pack(pady=10)

    botao_produtos = ctk.CTkButton(
        card,
        text="🎲 Produtos", font=("Arial", 25, "bold"),
        width=250,
        height=40,
        command=lambda: abrir_produtos(menuWindow)
    )
    botao_produtos.pack(pady=10)

    botao_vendas = ctk.CTkButton(
        card,
        text="💲 Vendas", font=("Arial", 25, "bold"),
        width=250,
        height=40,
        command=lambda: abrir_vendas(menuWindow)
    )
    botao_vendas.pack(pady=10)

    # BOTÃO SAIR
    botao_sair = ctk.CTkButton(
        card,
        text="↩️ Sair", font=("Arial", 25, "bold"),
        width=250,
        height=40,
        fg_color="#c0392b",
        hover_color="#922b21",
        command=lambda: fechar(menuWindow, mainWindow)
    )
    botao_sair.pack(pady=30)


def fechar(menuWindow, mainWindow):
    menuWindow.destroy()
    mainWindow.deiconify()