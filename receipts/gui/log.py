import threading
import time
import logging
import tkinter as tk 
import tkinter.scrolledtext as ScrolledText
import tkinter.ttk as ttk

class TextHandler(logging.Handler):
    # This class allows you to log to a Tkinter Text or ScrolledText widget

    def __init__(self, text):
        # run the regular Handler __init__
        logging.Handler.__init__(self)
        # Store a reference to the Text it will log to
        self.text = text

    def emit(self, record):
        msg = self.format(record)
        def append():
            self.text.configure(state='normal')
            self.text.insert(tk.END, msg + '\n')
            self.text.configure(state='disabled')
            # Autoscroll to the bottom
            self.text.yview(tk.END)
        # This is necessary because we can't modify the Text from other threads
        self.text.after(0, append)

class ScrolledTextLog(ttk.Frame):
    def __init__(self, master, *args, **kwargs):
        ttk.Frame.__init__(self, master, *args, **kwargs)
        self.master = master
        self.build_gui()

    def build_gui(self):                    
        #self.master.title('TEST')
        #self.master.option_add('*tearOff', 'FALSE')
        #self.grid(column=0, row=0, sticky='ew')
        self.columnconfigure(0, weight=1, uniform='a')
        self.columnconfigure(1, weight=1, uniform='a')
        self.columnconfigure(2, weight=1, uniform='a')
        self.columnconfigure(3, weight=1, uniform='a')

        # Add text widget to display logging info
        self.label = ttk.Label(self,
                                 text='Log:')
        self.label.grid(row=0, column=0, padx=(10,10), sticky='nsew')

        st = ScrolledText.ScrolledText(self, state='disabled')
        st.configure(font='TkFixedFont')
        st.grid(column=0, row=1, sticky='nsew', columnspan=4)

        # Create textLogger
        text_handler = TextHandler(st)

        # Logging configuration

        logging.basicConfig(filename='test.log',
            level=logging.INFO, 
            format='%(asctime)s - %(levelname)s - %(message)s')        

        # Add the handler to logger
        logger = logging.getLogger()        
        logger.addHandler(text_handler)

def worker():
    # Skeleton worker function, runs in separate thread (see below)   
    while True:
        # Report time / date at 2-second intervals
        time.sleep(2)
        timeStr = time.asctime()
        msg = 'Current time: ' + timeStr
        logging.info(msg) 

def main():
    root = tk.Tk()
    ScrolledTextLog(root)

    t1 = threading.Thread(target=worker, args=[])
    t1.start()

    root.mainloop()
    t1.join()

if __name__ == '__main__':
    main()
