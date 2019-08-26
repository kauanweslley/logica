# Faça um programa que leia três numeros e mostre o maior e o menor deles 

numero1 = int(input("numero 1: "))
numero2 = int(input("numero 2: "))
numero3 = int(input("numero 3: "))

if numero1 < numero2 and numero1 < numero3:
    print("%d é o menor" %numero1)
elif numero2 < numero1 and numero2 < numero3:
    print("%d é o menor" %numero2)
else:
    print("%d é o menor" %numero3)

if numero1 > numero2 and numero1 > numero3:
    print("%d é o maior" %numero1)
elif numero2 > numero1 and numero2 > numero3:
    print("%d é o maior" %numero2)
else:
    print("%d é o maior" %numero3)
