# -*- coding: utf-8 -*-
from pizza import Pizza

pizza1 = Pizza()
# print(pizza1.tamano)

pizza1.pedido()
#print (pizza1.pizza_valida)

if pizza1.pizza_valida == True:
    print (f""" 
            Su Pedido está correcto y este es el detalle:
                Pizza tamaño {pizza1.tamano}
                Ingrediente Protéico: {pizza1.proteicos}
                Ingrediente Vegetal 1: {pizza1.vegetal_1}
                Ingrediente Vegetal 2: {pizza1.vegetal_2}
                Tipo de Masa: {pizza1.tipo_masa}
                Precio: {pizza1.precio}
            """)




