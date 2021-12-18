import tkinter as tk
from tkinter import OptionMenu, Place, StringVar, ttk
from tkinter.constants import COMMAND
from tkinter.font import names
from typing import ValuesView
import pymysql

class App(ttk.Frame):   

        
    def __init__(self, parent):
        ttk.Frame.__init__(self)
       

        # Make the app responsive
        for index in [0, 1, 2]:
            self.columnconfigure(index=index, weight=1)
            self.rowconfigure(index=index, weight=1)

        # Create value lists
        # self.option_menu_list = ["", "Placa", "Nombre", "Email"]
        self.option_menu_list={1:"",2:"Placa",3:"Nombre",4:"Email"}
     

        # Create control variables
        self.var_4 = tk.StringVar(value=self.option_menu_list[2])

        # Create widgets :)
        self.setup_widgets()   
   

    def setup_widgets(self): 
        global Placa
        global Nombre
        global Email
        class DataBase:            
            
            def __init__(self):
                self.connection=pymysql.connect(
                    host='MYSQL5034.site4now.net',
                    user='a7df43_atzel09',
                    password='1q2w3e4r',
                    db='db_a7df43_atzel09'
                )
                self.cursor = self.connection.cursor()
                print("--------------")
                print("Conexion Exitosa!!!")
                print("#################")

            def show_one_record(self,valor,nombre):
                if (valor=="Placa"):
                    sql="select * from vehiculos where Placa LIKE '%{}%'".format(nombre)
                    try:
                        self.cursor.execute(sql)
                        Autos = self.cursor.fetchone()                    
                        Placa = Autos[0]
                        Nombre = Autos[1]                    
                        Email = Autos[2]
                        ShowPlaca.delete(0, 'end')
                        ShowPlaca.insert(1, Autos[0])
                        ShowNombre.delete(0, 'end')
                        ShowNombre.insert(1, Autos[1])
                        ShowEmail.delete(0, 'end')
                        ShowEmail.insert(1, Autos[2])
                        print("_______________")
                        print("Placa:",Placa)
                        print("Nombre:",Nombre)
                        print("Email:",Email)
                        print("_______________")
                        return
                    except Exception as e:
                        raise
                if (valor=="Nombre"):
                    sql="select * from vehiculos where Nombre LIKE '%{}%'".format(nombre)
                    try:
                        self.cursor.execute(sql)
                        Autos = self.cursor.fetchone()                    
                        Placa = Autos[0]
                        Nombre = Autos[1]                    
                        Email = Autos[2]
                        ShowPlaca.delete(0, 'end')
                        ShowPlaca.insert(1, Autos[0])
                        ShowNombre.delete(0, 'end')
                        ShowNombre.insert(1, Autos[1])
                        ShowEmail.delete(0, 'end')
                        ShowEmail.insert(1, Autos[2])
                        print("_______________")
                        print("Placa:",Placa)
                        print("Nombre:",Nombre)
                        print("Email:",Email)
                        print("_______________")
                        return
                    except Exception as e:
                        raise
                if (valor=="Email"):
                    sql="select * from vehiculos where Email LIKE '%{}%'".format(nombre)
                    try:
                        self.cursor.execute(sql)
                        Autos = self.cursor.fetchone()                    
                        Placa = Autos[0]
                        Nombre = Autos[1]                    
                        Email = Autos[2]
                        ShowPlaca.delete(0, 'end')
                        ShowPlaca.insert(1, Autos[0])
                        ShowNombre.delete(0, 'end')
                        ShowNombre.insert(1, Autos[1])
                        ShowEmail.delete(0, 'end')
                        ShowEmail.insert(1, Autos[2])
                        print("_______________")
                        print("Placa:",Placa)
                        print("Nombre:",Nombre)
                        print("Email:",Email)
                        print("_______________")
                        return
                    except Exception as e:
                        raise

        obj_db1 = DataBase()

        def llamarshow():
            name = buscar.get()
            valor = self.var_4.get()
            print("vea",valor)
            obj_db1.show_one_record(valor, name)
    
                   

        
        # Create a Frame for the Checkbuttons
        self.check_frame = ttk.LabelFrame(self, text="Buscar", padding=(20, 10))
        self.check_frame.grid(
            row=0, column=0, padx=(20, 10), pady=(20, 10), sticky="nsew"
        )
 # Entry
        buscar = self.entry = ttk.Entry(self.check_frame)
        self.entry.insert(0, "buscar...")
        self.entry.grid(row=0, column=0, padx=5, pady=10, sticky="nsew")      

        # option_menu_list={1:"",2:"Placa",3:"Nombre",4:"Email"}   
        # options = tk.StringVar(value=self.option_menu_list[2])

        # OptionMenu
        menudo = self.optionmenu = ttk.OptionMenu(
            self.check_frame, self.var_4, *self.option_menu_list.values()
        ) 
        self.optionmenu.grid(row=0, column=1, padx=5, pady=10, sticky="nsew")


        # Button
        self.button = ttk.Button(self.check_frame, text="Buscar", command=llamarshow)
        self.button.grid(row=0, column=2, padx=5, pady=10,  sticky="nsew")
 # Label
        self.label = ttk.Label(
            self.check_frame,
            text="Placa:",
            justify="center",
            font=("-size", 10, "-weight", "normal"),
        )
        self.label.grid(row=2, column=0, pady=(10, 10), columnspan=1)

 # Label
        ShowPlaca = self.entry = ttk.Entry(self.check_frame)
        self.entry.insert(0, "placa")
        self.entry.grid(row=2, column=1, padx=5, pady=10, sticky="nsew") 
 # Label
        self.label = ttk.Label(
            self.check_frame,
            text="Nombre:",
            justify="center",
            font=("-size", 10, "-weight", "normal"),
        )
        self.label.grid(row=3, column=0, pady=(10, 10), columnspan=1)

 # Label
        ShowNombre = self.entry = ttk.Entry(self.check_frame)
        self.entry.insert(0, "nombre")
        self.entry.grid(row=3, column=1, padx=5, pady=10, sticky="nsew") 
 # Label
        self.label = ttk.Label(
            self.check_frame,
            text="Email:",
            justify="center",
            font=("-size", 10, "-weight", "normal"),
        )
        self.label.grid(row=4, column=0,pady=(10, 10), columnspan=1)

 # Label
        ShowEmail = self.entry = ttk.Entry(self.check_frame)
        self.entry.insert(0, "email")
        self.entry.grid(row=4, column=1, padx=5, pady=10, sticky="nsew") 
         
    
   

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Ejercicio")

    # Simply set the theme
    root.tk.call("source", "sun-valley.tcl")
    root.tk.call("set_theme", "light")

    app = App(root)
    app.pack(fill="both", expand=True)

    # Set a minsize for the window, and place it in the middle
    root.update()
    root.minsize(root.winfo_width(), root.winfo_height())
    x_cordinate = int((root.winfo_screenwidth() / 2) - (root.winfo_width() / 2))
    y_cordinate = int((root.winfo_screenheight() / 2) - (root.winfo_height() / 2))
    root.geometry("+{}+{}".format(x_cordinate, y_cordinate))
    
    root.mainloop()