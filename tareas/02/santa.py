#Tarea de administracion de procesos: Ejercicios de sincronizacion.

#Laura Denisse Reyes Salazar

#Santa Claus

import threading 
import time
import random #Para generar numeros aleatorios en el caso de los elfos y los renos

global contador_elfos
global contador_renos

contador_elfos = 0
contador_renos = 0
    
    
        mutex_contador=threading.Semaphore(1)
            
            senal_renos = threading.Semaphore(0)

            senal_santa = threading.Semaphore(0)
            
            mutex_tres_elfos = threading.Semaphore(1)
            
            senal_santa = threading.Semaphore(0)


            def descanso_renos(num):        #Los renos salen de vacaciones
                    
                print "El reno %d esta de vacaciones en Hawai." % num
                time.sleep(random.random()*10)
  
        
        
            def ayuda_elfos():  # Santa ayuda a los elfos.
            
                print "Hola!!! Que necesitan elfos."
                time.sleep(1.0)
                print "Vuelvan a su trabajo, gusto en verlos... -Los elfos salen-."

            def Hoy_es_Navidad(): # Santa sale a trabajar.
        
                print "Santa reparte juguetes."
                time.sleep(3.0)
                print "Santa regresa a descansar."

	
	
            def elfo(num):
                    
                global contador_elfos
                    
                    print "El elfo %d espera a que se junten tres elfos ..." % num  #El primer elfo que necesita ayuda espera a que se reunan tres elfos para pedir ayuda.
            
           
                mutex_tres_elfos.acquire()  #Se incrementa el contador para reunir tres elfos.
               
                mutex_contador.acquire()    #Se incrementa el contador.
                
                  contador_elfos += 1  #Una vez que ya se han juntado tres elfos pueden entrar a hablar con Santa
                    
            if contador_elfos == 3:
                    
                print "Ya somos tres elfos ... -Entran a hablar con Santa-."
                    
                senal_santa.release()  #Sino se han reunido los tres elfos el mutex sigue incrementando la cuenta hasta acompletar tres.
            
                else:
                    
                    mutex_grupo_elfos.release() #Sigue funcionando el contador.
            
                    mutex_contador.release()
            
                senal_elfos.acquire() # Santa esta hablando con los elfos.
                
                print "El elfo %d ha resuelto su duda." % num

                mutex_contador.acquire() #Disminuye el contador segun han sido atendidos los elfos.
                
                contador_elfos -= 1
            
            if contador_elfos == 0: #Una vez que ha salido el ultimo elfo se reinicia el contador.
                
                    mutex_tres_elfos.release()
           
                        mutex_contador.release()
        
        
        
        def reno(num):
            
            global contador_renos
	
                while True:
		
                    print "El reno %d esta de regreso." % num #El reno regresa de sus vacaciones.
		
                        mutex_contador.acquire() #Se incrementa el contador.
                        
		        contador_renos += 1
		
		if contador_renos == 9: #Si los 9 renos ya llegaron, despiertan a Santa para salir.
                    
			print "Ya estamos todos de regreso!!! vamos a repartir juguetes *Renos*"
			
                            senal_santa.release() #Si aun no estan completos los renos, siguen esperando.
		
                        mutex_contador.release() #contador de espera.
		
                            senal_renos.acquire() #Señal de regreso para los renos.
		
                                descanso_renos(num) #Los renos se vuelven a ir de vacaciones.

        def santa():
	
            global contador_elfos
            
            global contador_renos
	
                    while True:
		
                        senal_santa.acquire() #Santa despierta a atender a los elfos y a los renos.
		
                            mutex_contador.acquire() #Revisa los contadores.
		
                        if 
                            contador_renos == 9: #contador para los renos.
			
                                Hoy_es_Navidad()  #Sale a trabajar
			
                                    contador_renos -= 9 #Modifica el contador de los renos.
			
			for i in range(9):
                            
				senal_renos.release()
				
		
                        if contador_elfos == 3: #Para hablar con los elfo
			
                            ayuda_elfos() #HAbla con los elfos
			
			for i in range(3):
				
                                    senal_elfos.release()
		
		mutex_contador.release() #Una vez que termina regresa a descansar y comienza de nuevo el contador.


 #Se definen los hilos de los elfos y renos.
        hilos_elfos = 0
        hilos_renos = 0


            threading.Thread(target=santa, args=[]).start()


            for i in range(1,10):
            
            threading.Thread(target=reno, args=[i]).start()


                while True:
                    time.sleep(0.50)
                    if random.random() < 1.0:
                        
                        threading.Thread(target=elfo, args=[hilos_elfos]).start()
		
                            hilos_elfos += 1
