import tkinter as tk

class TerminalFrame(tk.Frame):
    def __init__(self, root: 'tk.Tk', db_conn: 'psycopg2.connection'):
        super().__init__(root)
        self.db_conn = db_conn

        self._terminal_input()
        self._terminal_output()

    def _terminal_input(self):
        label = tk.Label(self, text=">>>")
        label.grid(row=1, column=0)

        self.entry = tk.Entry(self)
        self.entry.grid(row=1, column=1, sticky=tk.W+tk.E+tk.N+tk.S)

    def _terminal_output(self):
        self.terminal = tk.Text(self)
        self.terminal.grid(row=0, column=0, columnspan=2,
                           sticky=tk.W+tk.E+tk.N+tk.S)
