import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Mariano
apellido: García Novak
---
Ejercicio: while_10
---
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el usuario 
quiera hasta que presione el botón Cancelar (en el prompt). 
Luego calcular:
    A. La suma acumulada de los negativos
    B. La suma acumulada de los positivos
    C. Cantidad de números positivos ingresados
    D. Cantidad de números negativos ingresados
    E. Cantidad de ceros
    F. Diferencia entre la cantidad de los números positivos ingresados y los negativos

Informar los resultados mediante alert()

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
    
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):
        numero = 0
        suma_negativos = 0
        suma_positivos = 0
        cantidad_positivos = 0
        cantidad_negativos = 0
        cantidad_ceros = 0
        diferencia_cantidad_positivos_negativos = 0

        while True:
            aux = prompt("Ingreso", "Ingrese un número")
            if(aux == None):
                break
            numero = int(aux)

            if(numero > 0):
                suma_positivos += numero
                cantidad_positivos += 1
            elif(numero < 0):
                suma_negativos += numero
                cantidad_negativos += 1
            else:
                cantidad_ceros += 1

        diferencia_cantidad_positivos_negativos = cantidad_positivos - cantidad_negativos

        alert("Resultado", f"Suma de negativos: {suma_negativos}\nSuma de positivos: {suma_positivos}\nCantidad de negativos: {cantidad_negativos}\nCantidad de positivos: {cantidad_positivos}"+
              f"\nCantidad de ceros: {cantidad_ceros}\nDiferencia de cantidad de positivos con respecto a cantidad de negativos: {diferencia_cantidad_positivos_negativos}")

    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
