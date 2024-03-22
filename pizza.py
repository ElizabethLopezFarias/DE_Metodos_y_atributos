# -*- coding: utf-8 -*-
#importa listas de ingredientes desde ingredientes.py para facilitar variedad de stock
from ingredientes import tipos_masas, proteicos, vegetales
# Se crea la clase de tipo pizza con los atributos correspondientes
class Pizza():
    precio = 10000
    tamano = "Familiar"

#método para validar un elemento dentro de una lista
    @staticmethod
    def validar_elemento(elemento, valores):
        while elemento.lower() not in valores:
            print("La respuesta es incorrecta. Por favor, seleccione una opción válida.")
            print("Opciones válidas:", ", ".join(valores))
            elemento = input("Ingrese una opción válida: ")
        return elemento  
    
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

        # Validar si la pizza es válida        
        self.pizza_valida = all([
            self.proteicos,
            self.vegetal_1,
            self.vegetal_2,
            self.tipo_masa
        ])

    # def pedido(self):
    #     self.pizza_valida = False
    #     self.proteicos = input(f""" Elija Proteina:
    #                       - Pollo
    #                       - Vacuno
    #                       - NotCarne
    #                       """)
    #     valida_proteico = self.validar_elemento(self.proteicos, proteicos)
    #     #print(valida_proteico)

    #     self.vegetal_1 = input(f""" Elija Primer Vegetal:
    #                         - Tomate
    #                         - Aceitunas
    #                         - Champiñones
    #                       """)
    #     valida_vegetal_1 = self.validar_elemento(self.vegetal_1, vegetales)
    #     #print(valida_vegetal_1)


    #     self.vegetal_2 = input(f""" Elija Segundo Vegetal:
    #                         - Tomate
    #                         - Aceitunas
    #                         - Champiñones
    #                       """)
    #     valida_vegetal_2 = self.validar_elemento(self.vegetal_2, vegetales)
    #             #print(valida_vegetal_2)        
        
    #     self.tipo_masa = input(f""" Elija el Tipo de Masa:
    #                         - Delgada
    #                         - Tradicional
    #                        """)
    #     valida_masa = self.validar_elemento(self.tipo_masa, tipos_masas)

    #     #Valida si la pizza es válida        
    #     self.pizza_valida = all([
    #         self.validar_elemento(self.proteicos, proteicos),
    #         self.validar_elemento(self.vegetal_1, vegetales),
    #         self.validar_elemento(self.vegetal_2, vegetales),
    #         self.validar_elemento(self.tipo_masa, tipos_masas)
    #     ])

    



 
        