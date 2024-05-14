class Boligrafo:

    capacidad_maxima = 100
    cantidad_tinta = 80

    def __init__(self, grosor: str, color: str) -> None:
        if color == "rojo" or color == "azul":
            self.color = color
        else:
            print(f"color: {color} no válido. Se determinó 'azul' por defecto")
            self.color = "azul"
        if grosor == "fino" or grosor == "grueso":
            self.grosor = grosor
        else:
            print(f"grosor: {grosor} no válido. Se determinó 'fijo' por defecto")
            self.grosor = "fino"
    
    # Esta función la creé para ver chequear si se creó bien el objeto
    def obtener_propiedades(self):
        message = f"color: {self.color}, grosor: {self.grosor}, capacidad maxima: {self.capacidad_maxima}, cantidad_actual: {self.cantidad_tinta}"
        return message
    
    def escribir(self, texto: str):
        largo_texto = len(texto)
        largo_texto *= 1 if self.grosor == "fino" else 2
        if largo_texto < self.cantidad_tinta:
            self.cantidad_tinta -= largo_texto
            print(texto)
        else:
            print("No alcanza la tinta")

    def recargar(self,cantidad: int):
        self.cantidad_tinta += cantidad
        resto = self.cantidad_tinta - self.capacidad_maxima
        if self.cantidad_tinta > self.capacidad_maxima:
            self.cantidad_tinta = self.capacidad_maxima

        if resto < 1:
            mensaje = "Lapicera recargada"
        else:
            mensaje = f"Se recargó la lapicera y sobro {resto}"
        print(mensaje)