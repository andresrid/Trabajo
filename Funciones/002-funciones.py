# Escriba un programa para calcular las áreas de las figuras geométricas utilizando una función para cada área
import math


def area_cuadrado(lado):
    return lado * lado


def area_circulo(radio):
    return math.pi * radio**2


def area_triangulo(base, altura):
    return (base * altura) / 2


figura = input("Escoja la figura que deseas (cuadrado, circulo, triangulo): ")

if figura == "cuadrado":
    lado = float(input("Ingrese la longitud del lado del cuadrado: "))
    print("El área del cuadrado es:", area_cuadrado(lado))
elif figura == "circulo":
    radio = float(input("Ingrese el radio del círculo: "))
    print("El área del círculo es:", area_circulo(radio))
elif figura == "triangulo":
    base = float(input("Ingrese la longitud de la base del triángulo: "))
    altura = float(input("Ingrese la altura del triángulo: "))
    print("El área del triángulo es:", area_triangulo(base, altura))
else:
    print("Figura no reconocida. Por favor, ingrese 'cuadrado', 'circulo' o 'triangulo'.")