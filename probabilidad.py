import random
for i in range(0, 10):

    probabilidad = random.randint(0,100)
    print(probabilidad)

    perro = False
    gato = False
    conejo = False

    if probabilidad in range(0,20):
        gato = True
    elif probabilidad in range(21,50):
        perro = True
    elif probabilidad in range(51,100):
        conejo = True


    if perro == True:
        print("soy un perro")


    elif conejo == True:
        print("Soy un conejo")


    elif gato == True:
        print("soy un gato")


lista = [1,2,3,4,5,6]
del(lista[-1])
print(lista)