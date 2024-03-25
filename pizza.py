# -*- coding: utf-8 -*-
#importa listas de ingredientes desde ingredientes.py para facilitar variedad de stock
from ingredientes import tipos_masas, proteicos, vegetales, salsas
# Se crea la clase de tipo pizza con los atributos correspondientes
class Pizza():
    precio = 10000
    tamano = "Familiar"

    @staticmethod
    #Método para validar un elemento dentro de una lista
    def validar_elemento(elemento, valores):
        while elemento.lower() not in valores:
            print("La respuesta es incorrecta. Por favor, seleccione una opción válida.")
            print("Opciones válidas:", ", ".join(valores))
            elemento = input("Ingrese una opción válida: ")
        return elemento  
    # Método para solicitar un pedido y validar los datos ingresados por el usuario
    def pedido(self):
        self.pizza_valida = False

        # Validar y almacenar la proteína
        self.proteicos = self.validar_elemento(input("Elija Proteina:\n- Pollo\n- Vacuno\n- NotCarne\n"), proteicos)

        # Validar y almacenar el primer vegetal
        self.vegetal_1 = self.validar_elemento(input("Elija Primer Vegetal:\n- Tomate\n- Aceitunas\n- Champiñones\n"), vegetales)

        # Validar y almacenar el segundo vegetal
        self.vegetal_2 = self.validar_elemento(input("Elija Segundo Vegetal:\n- Tomate\n- Aceitunas\n- Champiñones\n"), vegetales)

        # Validar y almacenar el tipo de masa
        self.tipo_masa = self.validar_elemento(input("Elija el Tipo de Masa:\n- Delgada\n- Tradicional\n"), tipos_masas)
        
        # Validar Salsa
        self.salsa = self.validar_elemento(input("Elija una salsa:\n- Salsa de tomates\n- Salsa BBQ\n- Sin salsa\n"), salsas)


        # Validar si la pizza es válida        
        self.pizza_valida = all([
            self.proteicos,
            self.vegetal_1,
            self.vegetal_2,
            self.tipo_masa,
            self.salsas
        ])

        