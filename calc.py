import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
from tkinter import font as tkFont
import subprocess
import shutil
import os


class BareboneBuilder:
    def __init__(self, root):
        i:int=0
        self.root = root
        self.root.title("card file")

        # Janela amarela
        self.root.configure(bg='red')
        self.text_ = tk.Text(self.root, height=1, width=50)
        self.text_.pack(pady=5)
        # Área de texto
        self.text_area = tk.Text(self.root, height=10, width=50)
        self.text_area.pack(pady=5)
        

        

        # Botões
        self.copy_button = tk.Button(self.root, text="= =", command=self.selects)
        self.copy_button.pack(pady=5)
        self.text_.insert(tk.END,"1+1")
    def selects(self):
        nnreturn=""
        nreturn=""
        rreturn:float=0.000
        n1:float=0.000
        n2:float=0.000
        parc:list=[]
        try:
            nnreturn=str(self.text_.get("1.0", "end-1c"))
            nreturn=nnreturn + "=" + str(eval(nnreturn))+"\n"
        except:
            nreturn="error\n"
        self.text_area.insert(tk.END,nreturn)
    





if __name__ == "__main__":
    root = tk.Tk()
    builder = BareboneBuilder(root)
    root.mainloop()
