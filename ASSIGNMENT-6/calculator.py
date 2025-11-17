# calculator.py
import tkinter as tk
from tkinter import ttk
import re

# Allowed characters for safety when evaluating expressions
ALLOWED_RE = re.compile(r'^[0-9+\-*/().% ]+$')

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Tkinter Calculator")
        self.geometry("360x500")
        self.resizable(False, False)
        self.configure(bg="#2b2b2b")

        self._create_styles()
        self._make_widgets()
        self.expression = ""

    def _create_styles(self):
        style = ttk.Style(self)
        style.theme_use('clam')
        style.configure('TButton', font=('Helvetica', 16), padding=10)
        style.configure('Display.TEntry', font=('Helvetica', 24), padding=10)

    def _make_widgets(self):
        # Display entry (read-only)
        self.display_var = tk.StringVar()
        entry = ttk.Entry(self, textvariable=self.display_var, style='Display.TEntry', justify='right', state='readonly')
        entry.place(x=10, y=10, width=340, height=70)

        # Button layout
        btn_specs = [
            ('C', 1, 0, self.clear), ('⌫', 1, 1, self.backspace), ('%', 1, 2, lambda: self._add('%')), ('/', 1, 3, lambda: self._add('/')),
            ('7', 2, 0, lambda: self._add('7')), ('8', 2, 1, lambda: self._add('8')), ('9', 2, 2, lambda: self._add('9')), ('*', 2, 3, lambda: self._add('*')),
            ('4', 3, 0, lambda: self._add('4')), ('5', 3, 1, lambda: self._add('5')), ('6', 3, 2, lambda: self._add('6')), ('-', 3, 3, lambda: self._add('-')),
            ('1', 4, 0, lambda: self._add('1')), ('2', 4, 1, lambda: self._add('2')), ('3', 4, 2, lambda: self._add('3')), ('+', 4, 3, lambda: self._add('+')),
            ('+/-', 5, 0, self.negate), ('0', 5, 1, lambda: self._add('0')), ('.', 5, 2, lambda: self._add('.')), ('=', 5, 3, self.evaluate)
        ]

        # Create buttons
        btn_width = 80
        btn_height = 80
        start_x, start_y = 10, 100
        pad = 10

        for (text, r, c, cmd) in btn_specs:
            b = ttk.Button(self, text=text, command=cmd)
            x = start_x + c * (btn_width + 10)
            y = start_y + (r - 1) * (btn_height + 10)
            b.place(x=x, y=y, width=btn_width, height=btn_height)

        # Keyboard bindings
        self.bind_all("<Return>", lambda e: self.evaluate())
        self.bind_all("<KP_Enter>", lambda e: self.evaluate())
        self.bind_all("<BackSpace>", lambda e: self.backspace())
        for key in '0123456789+-*/().%':
            self.bind_all(key, self._keypress)
        self.bind_all('.', self._keypress)
        self.bind_all('<Escape>', lambda e: self.clear())

    def _keypress(self, event):
        # event.char might be empty for some keys — guard it
        ch = event.char
        if ch and ALLOWED_RE.match(ch):
            self._add(ch)
        elif ch in '+-*/().%':
            self._add(ch)

    def _add(self, char):
        """Add character to expression and update display."""
        # Prevent multiple dots in the same number: we keep it simple and allow the user to manage
        self.expression += str(char)
        self._update_display()

    def _update_display(self):
        self.display_var.set(self.expression)

    def clear(self):
        self.expression = ""
        self._update_display()

    def backspace(self):
        self.expression = self.expression[:-1]
        self._update_display()

    def negate(self):
        """
        Toggle sign of the last number in the expression.
        This attempts to find the last number token and negate it.
        """
        expr = self.expression.rstrip()
        if not expr:
            return
        # find last token (number or parenthesized expression)
        # simple approach: split by operators
        tokens = re.split(r'([+\-*/%])', expr)
        if not tokens:
            return
        last = tokens[-1]
        if last == '':
            # if expression ended with operator, do nothing
            return
        try:
            if last.startswith('(') and last.endswith(')'):
                # can't safely negate complex expression — wrap with -( )
                tokens[-1] = f"(-1)*{last}"
            else:
                # negate numeric token
                # if it's already negative, remove the leading '-'
                if last.startswith('-'):
                    tokens[-1] = last[1:]
                else:
                    tokens[-1] = f"(-{last})"
            self.expression = ''.join(tokens)
            self._update_display()
        except Exception:
            # fallback: just prepend a '-'
            self.expression = '-' + self.expression
            self._update_display()

    def evaluate(self):
        expr = self.expression.strip()
        if not expr:
            return
        # Safety check: only allow digits, operators, parentheses, dot, percent and spaces
        if not ALLOWED_RE.match(expr):
            self.display_var.set("Error: invalid characters")
            self.expression = ""
            return
        try:
            # Evaluate expression safely.
            # Note: % is modulo in Python; for percent-as-divide-by-100 behaviour you'd transform expressions accordingly.
            # Use eval on a restricted expression after safety check.
            result = eval(expr, {"__builtins__": None}, {})
            # Format result nicely (integers without .0)
            if isinstance(result, float) and result.is_integer():
                result = int(result)
            self.expression = str(result)
            self._update_display()
        except ZeroDivisionError:
            self.display_var.set("Error: Division by zero")
            self.expression = ""
        except Exception:
            self.display_var.set("Error")
            self.expression = ""

if __name__ == "__main__":
    app = Calculator()
    app.mainloop()
