import logging
import tkinter as tk
import tkinter.ttk as ttk
from receipts.gui.log import ScrolledTextLog
from receipts.gui.widgets import \
    SpreadsheetSelector, FolderSelector, TemplateSelector
from receipts.inputs import Inputs
from receipts.printer import Printer

class MainWindow(ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master, width=600, height=600)
        self.master = master
        self.build_gui()

    def build_gui(self):
        self.master.title('Tax Receipts')
        w = 700   # width of window
        h = 700   # height of window
        self.master.minsize(w, h)
        ws = self.master.winfo_screenwidth()
        hs = self.master.winfo_screenheight()
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        self.master.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(4, weight=1)
        self.rowconfigure(5, weight=1)
        self.grid(column=0, row=0, rowspan=1, columnspan=1, sticky='nsew')

        self.create_widgets()

    def create_widgets(self):
        self.label = ttk.Label(self, text='SELECT FILES AND DESTINATION FOLDER', font='bold')
        self.label.config(anchor='center')
        self.label.grid(row=0, column=0, columnspan=2, padx=(10, 10), pady=(10,10), sticky='nsew')

        self.spreadsheet_frame = SpreadsheetSelector(self) 
        self.spreadsheet_frame.grid(row=1, column=0, rowspan=1, columnspan=2, sticky='nsew')

        self.destination_frame = FolderSelector(self)
        self.destination_frame.grid(row=2, column=0, rowspan=1, columnspan=2, sticky='nsew')

        self.template_frame =  TemplateSelector(self)
        self.template_frame.grid(row=3, column=0, rowspan=1, columnspan=2, sticky='nsew')

        self.log_frame = ScrolledTextLog(self)
        self.log_frame.grid(row=4, column=0, columnspan=2, sticky='nsew')

        self.create = ttk.Button(self, text='Create Receipts', command=self.create_receipts)
        self.create.grid(row=5, column=0, columnspan=2, sticky='nsew')

    def create_receipts(self):
        logging.info('Printing receipts:')
        inputs = Inputs(self.spreadsheet_frame.get_file_path(), 
                        self.spreadsheet_frame.get_sheet_name(),
                        self.template_frame.get_receipt_start())
        printer = Printer(self.template_frame.get_file_path(), self.destination_frame.get_directory())

        inputs.to_csv()
        printer.from_csv()

        logging.info('DONE')
