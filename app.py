import tkinter as tk
import ttkbootstrap as ttk
import steps.SystemCreationFrame as s1

class App(ttk.Window):
    def __init__(self):
        super().__init__(themename='darkly', title='System Generator')
        self.create_widgets()
        
    def create_widgets(self):
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        
        ttk.Label(text='40K RPG System Generator', font='Calibri 24 bold').grid(column=0, row=0)
        s1.SystemCreationFrame(self).grid(column=0, row=1, padx=5, pady=5, sticky='nsew')
        
    
if __name__ == '__main__':
    app = App()
    app.mainloop()