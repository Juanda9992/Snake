import turtle
import time
import random

retraso = 0.1
probabilidad = random.randint(0,100)
recoger = False
contar = False


#contador
score = 0
highScore = 0
speed = 1 



#Ventana
ventana = turtle.Screen()
ventana.title("La Yinka")
ventana.bgcolor("darkblue")
ventana.setup(width= 700, height= 700)
ventana.tracer(0)
#Cabeza
cabeza = turtle.Turtle()
cabeza.speed(0)
cabeza.shape("square")
cabeza.goto(0, 0)
cabeza.penup()
cabeza.direction = "stop"
cabeza.color("white")
#Comida
comida = turtle.Turtle()
comida.shape("circle")
comida.penup()
comida.goto(0, 100)
comida.color("green")
normal = False

#ComidaEspecial
comidaEspecial = turtle.Turtle()
comidaEspecial.shape("triangle")
comidaEspecial.color("yellow")
comidaEspecial.penup()
comidaEspecial.goto(0, 1600)
especial = False

#Comida Turbo
comidaTurbo = turtle.Turtle()
comidaTurbo.shape("circle")
comidaTurbo.color("red")
comidaTurbo.penup()
comidaTurbo.goto(0,1900)
turbo = False

#Contador
marcador = turtle.Turtle()
marcador.speed(0)
marcador.color("yellow")
marcador.penup()
marcador.hideturtle()
marcador.goto(0, 280)
marcador.write("Score:0             High Score: 0     Speed: 1 m/s", align= "center", font =("Arial", 20, "normal"))

#Cuerpo
cuerpo = [ ]
hitbox = cuerpo
#Funciones
def arriba():
    cabeza.direction = "up"
def abajo():
    cabeza.direction = "down"
def izquierda():
    cabeza.direction = "left"
def derecha():
    cabeza.direction = "right"

def movimiento():
    if cabeza.direction == "up":
        y = cabeza.ycor()
        cabeza.sety(y + 20)
    if cabeza.direction == "down":
            y = cabeza.ycor()
            cabeza.sety(y + -20)
    if cabeza.direction == "left":
        x = cabeza.xcor()
        cabeza.setx(x - 20)
    if cabeza.direction == "right":
        x = cabeza.xcor()
        cabeza.setx(x + 20)

#BOTONES
ventana.listen()
ventana.onkeypress(arriba, "Up")
ventana.onkeypress(abajo, "Down")
ventana.onkeypress(izquierda, "Left")
ventana.onkeypress(derecha, "Right")
while True:
    ventana.update()
    #colisiones
    if cabeza.xcor() > 320 or cabeza.xcor() < -320 or cabeza.ycor() > 320 or cabeza.ycor() < -320:
        time.sleep(2)
        cabeza.goto(0,0)
        cabeza.direction = "stop"

        #Esconder cuerpo
        for segmento in cuerpo:
            segmento.goto(10000,10000)
        #borrar lista
        cuerpo.clear()

        #Borrar Puntaje
        score = 0
        speed = 1
        marcador.write("Score: 0             High Score: 0    Speed: 1 mt/s", align= "center", font =("Arial", 20, "normal"))
    retraso = 0.1
    marcador.clear()
    marcador.write("Score: {}            High Score: {}    Speed: {} m/s".format(score, highScore, speed),
                   align="center", font=("Arial", 20, "normal"))

    probabilidad = random.randint(0, 100)


    if cabeza.distance(comida) < 20:
        nuevoCuerpo = turtle.Turtle()
        nuevoCuerpo.speed(0)
        nuevoCuerpo.shape("square")
        nuevoCuerpo.color("grey")
        cuerpo.append(nuevoCuerpo)
        nuevoCuerpo.penup()
        comida.goto(1000,1000)
        score += 10
        probabilidad = random.randint(0, 100)
        retraso -= 0.0005
        speed += 1.0
        recoger = True


    if cabeza.distance(comidaEspecial) < 20:
        for i in range(0,3):
            nuevoCuerpo = turtle.Turtle()
            nuevoCuerpo.speed(0)
            nuevoCuerpo.shape("square")
            nuevoCuerpo.color("grey")
            cuerpo.append(nuevoCuerpo)
            nuevoCuerpo.penup()
            retraso -= 0.0007
            score += 10
        comidaEspecial.goto(1000,1000)
        probabilidad = random.randint(0,100)
        speed += 1.8
        recoger = True
    if cabeza.distance(comidaTurbo) < 20:
        for i in range(0,2):
            nuevoCuerpo = turtle.Turtle()
            nuevoCuerpo.speed(0)
            nuevoCuerpo.shape("square")
            nuevoCuerpo.color("grey")
            cuerpo.append(nuevoCuerpo)
            nuevoCuerpo.penup()
            retraso -= 0.0020
            score += 10
        speed += 4.0
        comidaTurbo.goto(1000,1000)
        probabilidad = random.randint(0,100)
        recoger = True

    if probabilidad in range(0, 40) and recoger == True:
        comidaY = random.randint(-288, 288)
        comidaX = random.randint(-288, 288)
        comida.goto(comidaX, comidaY)
        recoger = False
    elif probabilidad in range(41,70) and recoger == True:
        comidaTurbox = random.randint(-288, 288)
        comidaTruboy = random.randint(-288,288)
        comidaTurbo.goto(comidaTurbox,comidaTruboy)
        recoger = False

    elif probabilidad in range(71,100) and recoger == True:
        comidaEspecialx = random.randint(-288, 288)
        comidaEspecialy = random.randint(-288, 288)
        comidaEspecial.goto(comidaEspecialx,comidaEspecialy)
        recoger = False

    if score > highScore:
        highScore = score
        marcador.clear()
        marcador.write("Score: {}            High Score: {}    Speed: {} m/s".format(score,  highScore, speed),
                       align = "center", font =("Arial", 20, "normal"))

    #mover cuerpo

    numeroCuerpos = len(cuerpo)
    for index in range(numeroCuerpos -1 , 0, -1):
        x = cuerpo[index -1].xcor()
        y = cuerpo[index - 1].ycor()
        cuerpo[index].goto(x, y)
    if numeroCuerpos > 0:
        x = cabeza.xcor()
        y = cabeza. ycor()
        cuerpo[0].goto(x, y)
    movimiento()
    #Choques con cuerpo
    for segmento in cuerpo:
        if segmento.distance(cabeza) < 20:
            time.sleep(2)
            cabeza.goto(0, 0)
            cabeza.direction = "stop"

            for x in cuerpo:
                x.goto(100000,1000000)
            cuerpo.clear()

            retraso = 0.1
            score = 0
            speed = 1
            marcador.clear()
            marcador.write("Score: {}            High Score: {}      Speed: {} mts/s".format(score, highScore, speed), align= "center", font =("Arial", 20, "normal"))
    probabilidad = random.randint(0,100)

    time.sleep(retraso)



