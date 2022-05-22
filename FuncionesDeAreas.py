
#Gianluca de la Rosa Bandini A01736162
#Programa que calcula el área de diferentes figuras geométricas
import math

#Fórmula para calcular el círculo
def area_figura_circulo (radio):
    area = (math.pi*(radio**2)) #Operación a realizar
    return area

#Fórmula para calcular el triángulo
def area_figura_triangulo (base, altura):
    area = (base*altura)/2 #Operación a realizar
    return area

#Fórmula para calcular el rectángulo
def area_figura_rectangulo (base, altura):
    area = (base*altura) #Operación a realizar
    return area

#Fórmula para calcular el rombo
def area_figura_rombo (diametro_mayor, diametro_menor):
    area = (diametro_mayor*diametro_menor)/2 #Operación a realizar
    return area

#Fórmula para calcular el trapecio
def area_figura_trapecio (base_menor, base_mayor, altura):
    area = ((base_menor+base_mayor)(altura))/2 #Operación a realizar
    return area