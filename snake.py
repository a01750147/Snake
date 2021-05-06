#Codigo modificado por:
#Autor: Arturo Cuauhtemoc Ruiz Leyva
#Autor: Andrea Vianey Diaz Alvarez

"""Se importan las librerías que se usan en el código"""
import random
from turtle import *
from random import randrange
from freegames import square, vector


food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

#Definir el color de la comida y de la serpiente cada vez que se reinicia el juego
color = ['orange', 'blue','black', 'green', 'grey']
colorSerpiente = random.choice(color)
colorComida = random.choice(color)

#Condicion para que los colores de la comida y de la serpiente sean diferentes
while colorComida == colorSerpiente:
    colorComida = random.choice(color)


def change(x, y):
    """Change snake direction."""
    aim.x = x
    aim.y = y


def inside(head):
    """Return True if head inside boundaries."""
    return -200 < head.x < 190 and -200 < head.y < 190


def move():
    """Move snake forward one segment."""
    
    head = snake[-1].copy()
    head.move(aim)
    #aim 2 escoge una direccion en aleatorio para que se mueva la comida
    aim2 = random.choice([vector(0,10), vector(-10,0), vector(0,10), vector(0,-10)])
    food.move(aim2)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    #Condicion para que la comida no se salga del cuadro
    while inside(food)== False:
        food.x = 0
        food.y = 0
    
    
    #Condicion para saber que pasa cuando la vibora esta en la misma posicion que la comida

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)
        

    clear()
    
    #Hace que la serpiente sea mas grande
    for body in snake:
        square(body.x, body.y, 9, colorSerpiente)

    square(food.x, food.y, 9, colorComida)
    update()
    ontimer(move, 100)


setup(420, 420, 370, 100)#Define el tamaño de la ventana y donde se va a mostrar 
hideturtle() #Esconde el cursor
tracer(False) #Hace que no muestre la tortuga
listen() #Hace que acepte las direcciones que le damos a la serpiente

#Define la direccion de la serpiente
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')

move()

done()
