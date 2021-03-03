import tkinter as tk
import tkinter.filedialog as filedialog
import tkinter.ttk as ttk
from receipts.inputs import SUPPORTED_FILETYPES
from receipts.printer import PSUPPORTED_FILETYPES

class TemplateSelector(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master

        self.columnconfigure(0)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2)
        self.rowconfigure(0)
        self.rowconfigure(1)

        self.file_path = tk.StringVar()
        self.file_label = ttk.Label(self,
                                 text='Select Template:')
        self.file_label.grid(row=0, column=0, padx=(10,10), sticky='nsew')
        self.file_entry = ttk.Entry(self,
                                    textvariable = self.file_path,
                                    state = 'disabled')
        self.file_entry.grid(row=0, column=1, sticky='nsew')
        self.browse = ttk.Button(self, 
                                text='Browse', 
                                command=self.browse_button)
        self.browse.grid(row=0, column=2, sticky='nsew')

        self.receipt_start = tk.IntVar()
        self.start_label = ttk.Label(self, text='Start at receipt number:')
        self.start_label.grid(row=1, column=0, padx=(10,10), sticky='nsew')
        self.start_entry = ttk.Entry(self, textvariable = self.receipt_start)
        self.start_entry.grid(row=1, column=1)
 
    def browse_button(self):
        self.file_path.set(
            filedialog.askopenfilename(filetypes=PSUPPORTED_FILETYPES))

    def get_file_path(self):
        return self.file_path.get()
    
    def get_receipt_start(self):
        return self.receipt_start.get()

class FolderSelector(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master

        self.columnconfigure(0)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2)
        self.rowconfigure(0)

        self.destination = tk.StringVar()
        self.destination_label = ttk.Label(self,
                                 text='Select Destination:')
        self.destination_label.grid(row=0, column=0, padx=(10,10), sticky='nsew')
        self.destination_entry = ttk.Entry(self,
                                    textvariable = self.destination,
                                    state = 'disabled')
        self.destination_entry.grid(row=0, column=1, sticky='nsew')
        self.browse = ttk.Button(self, 
                                text='Browse', 
                                command=self.browse_button)
        self.browse.grid(row=0, column=2, sticky='nsew')
 
    def browse_button(self):
        self.destination.set(filedialog.askdirectory()) 

    def get_directory(self):
        return self.destination.get()

class SpreadsheetSelector(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.build_frame()

    def build_frame(self):
        self.columnconfigure(0)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2)
        self.rowconfigure(0)
        self.rowconfigure(1)
        self.rowconfigure(2)
        self.create_widgets()

    def create_widgets(self):
        self.file_path = tk.StringVar()
        self.file_label = ttk.Label(self,
                                 text='Select Spreadsheet:')
        self.file_label.grid(row=0, column=0, padx=(10,10), sticky='nsew')
        self.file_entry = ttk.Entry(self,
                                    textvariable = self.file_path,
                                    state = 'disabled')
        self.file_entry.grid(row=0, column=1, sticky='nsew')
        self.browse = ttk.Button(self, 
                                text='Browse', 
                                command=self.browse_button)
        self.browse.grid(row=0, column=2, sticky='nsew')

        self.sheet_name = tk.StringVar()
        self.sheet_label = ttk.Label(self,
                                    text='Sheet Name:')
        self.sheet_label.grid(row=1, column=0, padx=(10,10), sticky='nsew')
        self.sheet_entry = ttk.Entry(self,
                                     textvariable = self.sheet_name)
        self.sheet_entry.grid(row=1, column=1, sticky='nsew')
 
    def browse_button(self):
        self.file_path.set(
            filedialog.askopenfilename(filetypes=SUPPORTED_FILETYPES))

    def get_file_path(self):
        return self.file_path.get()

    def get_sheet_name(self):
        return self.sheet_name.get()
