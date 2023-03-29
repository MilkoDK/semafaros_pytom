#Primero, se importan los módulos necesarios: 
# "threading" para la implementación de hilos y "sleep" del módulo 
# "time" para introducir pausas en la ejecución.
import threading
from time import sleep

# Se crea un objeto semáforo con un valor de 2, 
# lo que significa que sólo dos hilos pueden acceder al recurso compartido al mismo tiempo.

semaforo = threading.Semaphore(2)

n=0

# Se define la clase "hilo" que hereda de la clase "Thread" de "threading".
# Esta clase tiene un constructor que toma un parámetro "id" que identifica al hilo.

class hilo(threading.Thread):
    def __init__(self, id):
        threading.Thread.__init__(self)
        self.id = id
        
# El método "run" de la clase "hilo" es donde se define la lógica del hilo. En primer lugar, 
# se adquiere el semáforo con el método "acquire", lo que significa que el hilo espera si no hay 
# semáforos disponibles. Luego, el hilo espera por una cantidad de tiempo igual a 3 menos el valor
# de "id" utilizando el método "sleep". Finalmente, se añade el valor de "id" a una lista compartida 
# llamada "d" y se libera el semáforo con el método "release".

    def run(self):
        semaforo.acquire()
        sleep(3-self.id)
        d.append(self.id)
        semaforo.release()

d=[]; # Se crea una lista vacía "d" que va a ser compartida por los hilos.
hilos = [hilo(1), hilo(2), hilo(3)] # Se crea una lista de tres objetos "hilo" con identificadores 1, 2 y 3.

#Se inician los hilos con el método "start" de cada objeto "hilo". 
# Cada hilo ejecutará el método "run".

for h in hilos:
    h.start()

# Después de 4 segundos de ejecución, se adquiere el semáforo y se imprime la lista 
# "d" que contiene los valores añadidos por los hilos.

sleep(4)
semaforo.acquire()
print (d)

# Finalmente, se libera el semáforo.

semaforo.release()