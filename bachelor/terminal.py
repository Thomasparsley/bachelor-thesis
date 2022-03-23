import tkinter as tk

class TerminalFrame(tk.Frame):
    def __init__(self, root: 'tk.Tk', db_conn: 'psycopg2.connection'):
        super().__init__(root)
        self.db_conn = db_conn

        self._terminal_output()

    def _terminal_output(self):
        self.terminal = tk.Text(self)
        self.terminal.pack()
