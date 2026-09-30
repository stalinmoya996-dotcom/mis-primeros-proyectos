import random
secreto=random.randint(1,10)
intento=0
intentos=0
while intento != secreto:
  intento=int(input("Adivina el numero del 1 al 10\n"))
  intentos=intentos+1
  if intento < secreto:
    print("numero muy bajo")
  elif intento > secreto:
    print("Numero muy alto")
  else:
    print("Ganaste, Acertaste el numero en",intentos,"intentos")
  
