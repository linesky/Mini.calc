import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
from tkinter import font as tkFont
import subprocess
import shutil
import os
example="""a=100
b=200
$a + $b """


class BareboneBuilder:
    def __init__(self, root):
        i:int=0
        self.root = root
        self.root.title("card file")

        
        self.root.configure(bg='red')
        self.text_ = tk.Text(self.root, height=10, width=50,bg='red')
        self.text_.pack(pady=5)
        # Área de texto
        self.text_area = tk.Text(self.root, height=10, width=50,bg='red')
        self.text_area.pack(pady=5)
        

        

        # Botões
        self.copy_button = tk.Button(self.root, text="= =", command=self.selects)
        self.copy_button.pack(pady=5)
        self.text_.insert(tk.END,example)
    def selects(self):
        nnreturn=""
        nreturn=""
        rreturn:float=0.000
        n1:float=0.000
        n2:float=0.000
        parc:list=[]
        try:
            nnreturn=str(self.text_.get("1.0", "end-1c"))
            nnreturn=nnreturn.replace("\r\n","\n")
            nnreturn=nnreturn.replace("\n\r","\n")
            nnreturn=nnreturn.replace("\r","\n")
            nnreturn=nnreturn.replace("\n\n","\n")
            
            fff=nnreturn.split("\n")
            l=len(fff)
            print(l)
            if l!=1:
                ttt=fff[l-1]+" "
                print(ttt)
                for f in range(l-1):
                    print(f)
                    print(fff[f])
                    x1=fff[f].split("=")
                    x1[0]="$"+x1[0]+" "
                    ttt=ttt.replace(x1[0],x1[1])
                
            else:
                ttt=fff[0]


            rreturn=eval(ttt)
            nreturn=nnreturn + "=" + str(rreturn)+"\n"
        except:
            nreturn="error\n"
        self.text_area.insert(tk.END,nreturn)
    





if __name__ == "__main__":
    root = tk.Tk()
    builder = BareboneBuilder(root)
    root.mainloop()
