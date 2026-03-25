import tkinter as Ventana

class Formulario:
    def __init__(self):
        self.color = "rojo"
        self.entry_nombre = None
        self.label_resultado = None
        self.formulario = None
    
    def iniciar_ventana(self):
        self.formulario = Ventana.Tk()
        self.formulario.title("Registro de cliente")
        self.formulario.geometry("800x800")
        self.formulario.resizable(False, True)
        self.formulario.configure(bg="red", cursor="hand2")
        return self.formulario
    
    def iniciar_preguntas(self):
        label_nombre = Ventana.Label(self.formulario, text="Digite el nombre del cliente: ")
        label_nombre.config(padx=10, pady=10, borderwidth=2, fg="blue")
        label_nombre.pack()
        
        self.entry_nombre = Ventana.Entry(self.formulario)
        self.entry_nombre.config(bg="yellow")
        self.entry_nombre.pack()
        
        boton_enviar = Ventana.Button(self.formulario, text="Enviar", command=self.onclick)
        boton_enviar.config(bg="orange")
        boton_enviar.pack()

    def onclick(self):
        print("click . . . . ")
    
    