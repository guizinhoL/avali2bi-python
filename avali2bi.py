"""Faça um único programa na linguagem Python para calcular o lucro que um salão de festas tem durante
 um mês de funcionamento. Considere que o salão de festas funciona apenas aos sábados e domingos, 
 portanto abre apenas 8 vezes em um mês, e todas as noites sempre acontece um evento. 

Para cada evento (utilizando bloco(s) de repetição) solicite as seguintes informações: (2.0)
a. O dia no mês em que vai acontecer o evento;
b. O número de pessoas que estarão no evento;
 
Calcule e mostre:
a. Considerando a tabela abaixo, defina e mostre o valor da locação. (2.0)
+----------------------------------+--------------------+
| Número de pessoas                | Valor da locação   |
+----------------------------------+--------------------+
| Caso não ultrapasse 1000 pessoas |    R$ 4500,00      |
+----------------------------------+--------------------+
|  Caso ultrapasse 1000 pessoas    |  R$ 5,00 reis      |
|                                  |  por pessoa        |
+----------------------------------+--------------------+

b. Qual a média do valor da locação (considerando todas as locações). (2.0)

c. Quantos eventos não ultrapassaram 1000 pessoas? (2.0)

d. Qual o dia do mês onde ocorreu o evento com o maior número de 
pessoas, e qual o dia do mês onde ocorreu o evento com o menor número de pessoas.(2.0)"""



medlo = 0
media = float(8)
numeve = 0
maior = 0
menor = 100000
qdimeno = 0
qdiamaior = 0
tot = 0
vlra = 0
vlr = 4500

for cont in range(8):
    print("digite o  mes do  evento sendo '1' janeiro e '12'dezembro")

    dimes = int(input())

    print("digite o dia do mes que ira contecer o evento")
    dia = int(input())
    print("digite quantas pessoas estarao no evento")
    pess = int(input())
    
    if maior < pess:
        maior = pess
        qdiamaior = dia
        diamaior = dia

    else:
        if pess < menor:
            diameno = dia
            menor = pess
            qdimeno = dia
    
    if pess <= 1000:
            tot += vlr
    else:
        if pess > 1000:
            pess *= 5
            vlra = pess
            numeve += 1

    medlo += pess
    media /= medlo
print("media", media)
print("valor da locação ate 1000 pessoas é", tot)
print("valor da locação acima 1000 pessoas é", vlra)
print("o dia que teve o menor nuemro de pessoas é:",diameno,"ovalor é ", qdimeno)
print("o dia que teve o maior nuemro de pessoas é:",diamaior, "o valor é ", qdiamaior)