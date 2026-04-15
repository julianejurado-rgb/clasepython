import tkinter as Ventana

class Formulario:

    def __init__(self):

        self.color_fondo = "gray"

        self.input_nombre = ""
        self.input_apellido = ""
        self.input_edad = ""
        self.input_correo = ""
        self.input_telefono = ""

        self.label_estado = ""
        self.ventana = ""

        self.lista_clientes = []

    def iniciar_ventana(self):

        self.ventana = Ventana.Tk()

        self.ventana.title("Registro de cliente")
        self.ventana.geometry("800x450")
        self.ventana.config(bg=self.color_fondo)

        return self.ventana

    def iniciar_preguntas(self):

        
        contenedor = Ventana.Frame(self.ventana, bg=self.color_fondo)
        contenedor.pack(pady=20)

       
        Ventana.Label(contenedor, text="Nombre:", bg=self.color_fondo).pack(pady=5)
        self.input_nombre = Ventana.Entry(contenedor)
        self.input_nombre.pack(pady=5)

        
        Ventana.Label(contenedor, text="Apellido:", bg=self.color_fondo).pack(pady=5)
        self.input_apellido = Ventana.Entry(contenedor)
        self.input_apellido.pack(pady=5)

       
        Ventana.Label(contenedor, text="Edad:", bg=self.color_fondo).pack(pady=5)
        self.input_edad = Ventana.Entry(contenedor)
        self.input_edad.pack(pady=5)

      
        Ventana.Label(contenedor, text="Correo:", bg=self.color_fondo).pack(pady=5)
        self.input_correo = Ventana.Entry(contenedor)
        self.input_correo.pack(pady=5)

        
        Ventana.Label(contenedor, text="Teléfono:", bg=self.color_fondo).pack(pady=5)
        self.input_telefono = Ventana.Entry(contenedor)
        self.input_telefono.pack(pady=5)

        self.label_estado = Ventana.Label(contenedor, text="", bg=self.color_fondo)
        self.label_estado.pack(pady=10)

       
        frame_botones = Ventana.Frame(contenedor, bg=self.color_fondo)
        frame_botones.pack(pady=10)

        boton_validar = Ventana.Button(
            frame_botones,
            text="Validar",
            width=15,
            command=self.validar_campos
        )
        boton_validar.pack(side="left", padx=10)

        boton_registrar = Ventana.Button(
            frame_botones,
            text="Registrar",
            width=15,
            command=self.funcion_principal
        )
        boton_registrar.pack(side="left", padx=10)

   
    def validar_campos(self):

        if (self.input_nombre.get() == "" or
            self.input_apellido.get() == "" or
            self.input_edad.get() == "" or
            self.input_correo.get() == "" or
            self.input_telefono.get() == ""):

            self.label_estado.config(text="Campos vacíos", fg="white")
            return False
        else:
            self.label_estado.config(text="Campos completos", fg="green")
            return True

    def obtener_datos(self):

        return [
            self.input_nombre.get(),
            self.input_apellido.get(),
            self.input_edad.get(),
            self.input_correo.get(),
            self.input_telefono.get()
        ]


    def almacenar_cliente(self, datos):
        self.lista_clientes.append(datos)

    def funcion_principal(self):

        if self.validar_campos():

            datos = self.obtener_datos()
            self.almacenar_cliente(datos)

            self.label_estado.config(text="Cliente registrado", fg="yellow")

            print("Clientes guardados:", self.lista_clientes)


if __name__ == "__main__":

    app = Formulario()
    ventana = app.iniciar_ventana()
    app.iniciar_preguntas()
    ventana.mainloop()
    
