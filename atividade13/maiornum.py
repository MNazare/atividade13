# Exercício Python 14: Faça um programa que leia três números e
# mostre qual é o maior e qual é o menor.

import time
print("""
Para decidir quem ficaria com o computador 
novo o professor decidiu comparar as notas dos 
três alunos que disputavam a vaga.
    """)
time.sleep(1)
print("ajude seu professor digitando a média dos alunos para ele")
med1 = float(input("média do aluno 1: "))
med2 = float(input("média do aluno 2: "))
med3 = float(input("média do aluno 3: "))
time.sleep(2)
print("agora veremos quem tem a maior e menor nota")
if med1 > med2 and med1 > med3:
    print("o primeiro aluno tem a média maior ")
if med2 > med1 and med2 > med3:
    print("segundo aluno tem a média maior")
if med3 > med2 and med3 > med1:
    print("terceiro aluno tem a média maior")
if med1 < med2 and med1 < med3:
    print("primeiro aluno tem a média menor")
if med2 < med1 and med2 < med3:
    print("segundo aluno tem a média menor")
if med3 < med2 and med3 < med1:
    print("terceiro aluno tem a média menor")