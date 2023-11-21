import tkinter as tk

# Formulário Simples criado com TKinter
# Função para calcular a Média de 3 números
def exibirmedia():
    a = float(a_entry.get())
    b = float(b_entry.get())
    c = float(c_entry.get())
    
    if a < 0 or b < 0 or c < 0:
        print('ERRO: Não é possível calcular a média de números negativos.')
    elif a == b == c:
        print(f'Os 3 números têm os mesmos valores, portanto a média é {a}.')
    else:
        media = (a + b + c) / 3
        print(f'A média dos números é {media:.2f}.')

# Criação da Janela Principal
janela = tk.Tk()
janela.title("Cálculo de Médias")

# Criação dos widgets do formulário
a_label = tk.Label(janela, text="Digite o 1º Número:")
a_label.pack()
a_entry = tk.Entry(janela)
a_entry.pack()

b_label = tk.Label(janela, text="Digite o 2º Número:")
b_label.pack()
b_entry = tk.Entry(janela)
b_entry.pack()

c_label = tk.Label(janela, text="Digite o 3º Número:")
c_label.pack()
c_entry = tk.Entry(janela)
c_entry.pack()

# Botão de Enviar
enviar_button = tk.Button(janela, text="Calcular", command=exibirmedia)
enviar_button.pack()

# Iniciar o loop de eventos da janela
janela.mainloop()