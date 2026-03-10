import customtkinter as ctk
from program_functions.system_dados import produtos


def abrir_vendas(janela_principal):

    janela_principal.withdraw()

    vendas = ctk.CTkToplevel()
    vendas.title("3xM System - Vendas")
    vendas.state("zoomed")

    itens_venda = []
    total_venda = 0

    def atualizar_lista():

        lista_produtos.delete("1.0", "end")

        for item in itens_venda:
            texto = f"{item['codigo']} | {item['nome']} | R$ {float(item['preco']):.2f}\n"
            lista_produtos.insert("end", texto)

    def atualizar_total():

        nonlocal total_venda

        total_venda = sum(float(item["preco"]) for item in itens_venda)

        label_total.configure(text=f"Total: R$ {total_venda:.2f}")

    def adicionar_produto():

        busca = entry_produto.get()

        for produto in produtos:

            if busca == produto["codigo"] or busca.lower() == produto["nome"].lower():

                itens_venda.append(produto)

                atualizar_lista()
                atualizar_total()

                entry_produto.delete(0, "end")

                return

    def finalizar_venda():

        if len(itens_venda) == 0:
            return

        itens_venda.clear()

        atualizar_lista()
        atualizar_total()

        label_total.configure(text="Total: R$ 0,00")

    def cancelar_venda():

        itens_venda.clear()

        atualizar_lista()
        atualizar_total()

        label_total.configure(text="Total: R$ 0,00")

    container = ctk.CTkFrame(vendas, corner_radius=0)
    container.pack(fill="both", expand=True, padx=20, pady=20)

    titulo = ctk.CTkLabel(
        container,
        text="🛒 Nova Venda",
        font=("Segoe UI", 28, "bold")
    )
    titulo.pack(pady=20)

    frame_busca = ctk.CTkFrame(container)
    frame_busca.pack(fill="x", padx=50, pady=10)

    entry_produto = ctk.CTkEntry(
        frame_busca,
        placeholder_text="🔎 Digite o código ou nome do produto",
        height=40,
        font=("Segoe UI", 14)
    )
    entry_produto.pack(side="left", fill="x", expand=True, padx=10, pady=10)

    botao_adicionar = ctk.CTkButton(
        frame_busca,
        text="Adicionar",
        width=140,
        height=40,
        font=("Segoe UI", 14, "bold"),
        command=adicionar_produto
    )
    botao_adicionar.pack(side="left", padx=10)

    frame_lista = ctk.CTkFrame(container)
    frame_lista.pack(fill="both", padx=50, pady=20)

    label_lista = ctk.CTkLabel(
        frame_lista,
        text="Produtos da Venda",
        font=("Segoe UI", 18, "bold")
    )
    label_lista.pack(pady=10)

    lista_produtos = ctk.CTkTextbox(
        frame_lista,
        height=250,
        font=("Consolas", 14)
    )
    lista_produtos.pack(fill="x", padx=20, pady=10)

    frame_total = ctk.CTkFrame(container)
    frame_total.pack(fill="x", padx=50, pady=20)

    label_total = ctk.CTkLabel(
        frame_total,
        text="Total: R$ 0,00",
        font=("Segoe UI", 24, "bold")
    )
    label_total.pack(side="left", padx=20)

    frame_botoes = ctk.CTkFrame(container)
    frame_botoes.pack(pady=20)

    botao_finalizar = ctk.CTkButton(
        frame_botoes,
        text="Finalizar Venda",
        width=180,
        height=45,
        font=("Segoe UI", 16, "bold"),
        command=finalizar_venda
    )
    botao_finalizar.pack(side="left", padx=10)

    botao_cancelar = ctk.CTkButton(
        frame_botoes,
        text="Cancelar",
        width=140,
        height=45,
        fg_color="#E53935",
        hover_color="#C62828",
        font=("Segoe UI", 16, "bold"),
        command=cancelar_venda
    )
    botao_cancelar.pack(side="left", padx=10)

    botao_voltar = ctk.CTkButton(
        frame_botoes,
        text="Voltar",
        width=140,
        height=45,
        font=("Segoe UI", 16, "bold"),
        command=lambda: voltar(vendas, janela_principal)
    )
    botao_voltar.pack(side="left", padx=10)


def voltar(vendas, janela_principal):
    vendas.destroy()
    janela_principal.deiconify()
    janela_principal.state("zoomed")