import tkinter as tk
import psycopg2
import os

from editor import EditorFrame
from terminal import TerminalFrame


class Window(tk.Tk):

    def __init__(self):
        super().__init__()

        self.db_conn: psycopg2.connection = None

        if False:
            self.db_conn = psycopg2.connect(
                "host=localhost dbname=bachelor user=root password=root")

        self.title("Bachelor App")

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        self.paned_window = tk.PanedWindow(orient=tk.VERTICAL)

        self._sql_editor()
        self._terminal()
        self._footer()

        self.paned_window.grid(row=0, column=0, sticky=tk.W+tk.E+tk.N+tk.S)

        self.bind("<<RunAllSql>>", self.run_all_sql)
        self.bind("<<RunSelectedSql>>", self.run_selected_sql)

        self._main_menu()

        self.config(menu=self.main_menu_bar)

    def _sql_editor(self):
        self.editor_frame = EditorFrame(self)
        self.editor_frame.grid(row=0, column=0, sticky=tk.W+tk.E+tk.N+tk.S)
        self.paned_window.add(self.editor_frame)

    def _terminal(self):
        self.terminal_frame = TerminalFrame(self, self.db_conn)
        self.terminal_frame.grid(row=1, column=0, sticky=tk.W+tk.E+tk.N+tk.S)
        self.paned_window.add(self.terminal_frame)

    def _footer(self):
        self.footer_frame = tk.Frame(self)
        self.footer_frame.grid(row=1, column=0, sticky=tk.W+tk.E)

        info = tk.Label(self.footer_frame,
                        text="connected to: 127.0.0.1:8080    |    db server: postres    |    last query: 0ms    |    example info")
        info.pack()

    def _main_menu(self):
        self.main_menu_bar = tk.Menu(self)

        # File menu
        file_menu = tk.Menu(self.main_menu_bar, tearoff=0)
        file_menu.add_command(
            label="Novy",        accelerator="Ctrl+N", underline=1)
        file_menu.add_command(
            label="Otevrit",     accelerator="Ctrl+O", underline=1)
        file_menu.add_command(label="Ulozit",      accelerator="Ctrl+S")
        file_menu.add_command(label="Ulozit jako", accelerator="Ctrl+Shift+S")

        file_menu.add_separator()

        file_menu.add_command(
            label="Ukoncit", command=self.quit, accelerator="Ctrl+Q")

        self.main_menu_bar.add_cascade(label="Soubor", menu=file_menu)

        # SQL menu
        sql_menu = tk.Menu(self.main_menu_bar, tearoff=0)

        sql_menu.add_command(label="Run all")
        sql_menu.add_command(label="Run selected")

        sql_menu.add_separator()

        sql_menu.add_command(label="Format All")
        sql_menu.add_command(label="Format selected")

        self.main_menu_bar.add_cascade(label="SQL", menu=sql_menu)

        pass

    def execute_sql(self, data: str):
        cursor = self.db_conn.cursor()

        try:
            cursor.execute(data)
            cursor.description
            data = cursor.fetchall()

            self.terminal_frame.terminal.insert(tk.END, data)
        except psycopg2.Error as e:
            self.terminal_frame.terminal.insert(tk.END, e)
        finally:
            self.terminal_frame.terminal.insert(tk.END, os.linesep)
            self.terminal_frame.terminal.insert(tk.END, os.linesep)

            cursor.close()
            self.db_conn.commit()

    def run_all_sql(self, _: "tk.Event"):
        data = self.editor_frame.textarea_data()
        self.execute_sql(data)

    def run_selected_sql(self, _: "tk.Event"):
        data = self.editor_frame.textarea.selection_get()
        self.execute_sql(data)
