"""
Interface gráfica da Calculadora Científica usando Tkinter
Inclui operações básicas e científicas
Projeto didático com explicações para aprendizado
"""

import tkinter as tk
from tkinter import messagebox
import math
import calculator_full as calc

class CalculatorGUI:
    def __init__(self, master):
        self.master = master
        master.title("Calculadora Científica")

        # Campo de entrada e exibição do resultado
        self.display = tk.Entry(master, width=30, font=("Arial", 16), borderwidth=2, relief="groove")
        self.display.grid(row=0, column=0, columnspan=5, padx=5, pady=5)

        # Botões da calculadora
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('+', 1, 3), ('-', 1, 4),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3), ('/', 2, 4),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('^', 3, 3), ('√', 3, 4),
            ('0', 4, 0), ('.', 4, 1), ('log', 4, 2), ('sin', 4, 3), ('cos', 4, 4),
            ('tan', 5, 0), ('C', 5, 1), ('=', 5, 2, 3)
        ]

        for (text, row, col, cs) in [(b[0], b[1], b[2], 1) if len(b) == 3 else b for b in buttons]:
            button = tk.Button(master, text=text, width=5, height=2, font=("Arial", 14),
                               command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col, columnspan=cs, padx=2, pady=2)

    def on_button_click(self, char):
        if char == 'C':
            self.display.delete(0, tk.END)
        elif char == '=':
            self.calculate()
        elif char in ['sin', 'cos', 'tan', 'log', '√', '^']:
            self.display.insert(tk.END, f' {char} ')
        else:
            self.display.insert(tk.END, char)

    def calculate(self):
        expression = self.display.get()
        try:
            # Substituir operadores e funções para avaliação segura
            expression = expression.replace('^', '**')
            expression = expression.replace('√', 'raiz')
            # Tokenizar a expressão para tratar funções científicas
            tokens = expression.split()
            stack = []
            i = 0
            while i < len(tokens):
                token = tokens[i]
                if token == 'raiz':
                    # raiz deve ser seguida pelo número e opcionalmente pelo grau
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
                else:
                    stack.append(token)
                i += 1
            final_expr = ' '.join(stack)
            # Avaliar expressão final com funções básicas e operadores
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
