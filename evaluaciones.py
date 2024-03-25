# -*- coding: utf-8 -*-
# Importa la clase
from pizza import Pizza
# Asigna los atributos de la clase
pizza1 = Pizza()

pizza1.pedido()
#print (pizza1.pizza_valida)
#Muestra los atributos si la pizza es validada
if pizza1.pizza_valida == True:
    print (f""" 
            Su Pedido está correcto y este es el detalle:
                Pizza tamaño {pizza1.tamano}
                Ingrediente Protéico: {pizza1.proteicos}
                Ingrediente Vegetal 1: {pizza1.vegetal_1}
                Ingrediente Vegetal 2: {pizza1.vegetal_2}
                Tipo de Masa: {pizza1.tipo_masa}
                Tipo de Salsa: {pizza1.salsa}
                Precio: {pizza1.precio}
            """)




