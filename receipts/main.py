from ttkthemes import ThemedStyle, ThemedTk
from receipts.gui.mainwindow import MainWindow

def main():
    root = ThemedTk(theme='yaru')
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)
    app = MainWindow(root)
    app.mainloop()

if __name__ == '__main__':
    main()
