"""
Interface gráfica da Calculadora Científica usando Tkinter e ttk
Inclui operações básicas, científicas e estatísticas
Projeto didático com explicações para aprendizado
"""

import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import math
import calculator_full as calc

class CalculatorGUI:
    def __init__(self, master):
        self.master = master
        master.title("Calculadora Científica")

        # Aplicar tema ttk moderno
        style = ttk.Style(master)
        style.theme_use('clam')  # tema moderno padrão, pode ser alterado

        # Campo de entrada e exibição do resultado
        self.display = ttk.Entry(master, width=40, font=("Arial", 16))
        self.display.grid(row=0, column=0, columnspan=7, padx=5, pady=5)

        # Botões da calculadora
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('+', 1, 3), ('-', 1, 4), ('C', 1, 5), ('⌫', 1, 6),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3), ('/', 2, 4), ('=', 2, 5), ('(', 2, 6),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('^', 3, 3), ('√', 3, 4), (')', 3, 5), ('mean', 3, 6),
            ('0', 4, 0), ('.', 4, 1), ('log', 4, 2), ('sin', 4, 3), ('cos', 4, 4), ('tan', 4, 5), ('median', 4, 6),
            ('mode', 5, 0), ('variance', 5, 1)
        ]

        for (text, row, col) in buttons:
            button = ttk.Button(master, text=text, command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col, padx=2, pady=2, sticky="nsew")

        # Configurar expansão dos botões para preencher espaço
        for i in range(6):
            master.rowconfigure(i, weight=1)
        for j in range(7):
            master.columnconfigure(j, weight=1)

    def on_button_click(self, char):
        if char == 'C':
            self.display.delete(0, tk.END)
        elif char == '⌫':
            current_text = self.display.get()
            if current_text:
                self.display.delete(len(current_text)-1, tk.END)
        elif char == '=':
            self.calculate()
        elif char in ['sin', 'cos', 'tan', 'log', '√', '^', 'mean', 'median', 'mode', 'variance']:
            self.display.insert(tk.END, f' {char} ')
        else:
            self.display.insert(tk.END, char)

    def calculate(self):
        expression = self.display.get()
        try:
            # Substituir operadores e funções para avaliação segura
            expression = expression.replace('^', '**')
            expression = expression.replace('√', 'raiz')
            # Tokenizar a expressão para tratar funções científicas e estatísticas
            tokens = expression.split()
            stack = []
            i = 0
            while i < len(tokens):
                token = tokens[i]
                if token == 'raiz':
                    n = float(stack.pop())
                    grau = 2
                    if i + 1 < len(tokens) and tokens[i+1].isdigit():
                        grau = int(tokens[i+1])
                        i += 1
                    result = calc.raiz(n, grau)
                    stack.append(str(result))
                elif token == 'sin':
                    x = float(tokens[i+1])
                    result = calc.seno(math.radians(x))
                    stack.append(str(result))
                    i += 1
                elif token == 'cos':
                    x = float(tokens[i+1])
                    result = calc.cosseno(math.radians(x))
                    stack.append(str(result))
                    i += 1
                elif token == 'tan':
                    x = float(tokens[i+1])
                    result = calc.tangente(math.radians(x))
                    stack.append(str(result))
                    i += 1
                elif token == 'log':
                    n = float(tokens[i+1])
                    result = calc.logaritmo(n)
                    stack.append(str(result))
                    i += 1
                elif token in ['mean', 'median', 'mode', 'variance']:
                    if i + 1 < len(tokens):
                        list_str = tokens[i+1]
                        list_str = list_str.strip('()')
                        # Permitir espaços e vírgulas como separadores
                        num_list = []
                        for part in list_str.split(','):
                            part = part.strip()
                            if part:
                                num_list.append(float(part))
                        if token == 'mean':
                            result = calc.media(num_list)
                        elif token == 'median':
                            result = calc.mediana(num_list)
                        elif token == 'mode':
                            result = calc.moda(num_list)
                        elif token == 'variance':
                            result = calc.variancia(num_list)
                        stack.append(str(result))
                        i += 1
                    else:
                        raise ValueError(f"Faltando lista de números para a função {token}")
                else:
                    stack.append(token)
                i += 1
            final_expr = ' '.join(stack)
            result = eval(final_expr)
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, str(result))
        except Exception as e:
            messagebox.showerror("Erro", f"Erro na expressão: {e}")

def main():
    root = tk.Tk()
    calc_gui = CalculatorGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
