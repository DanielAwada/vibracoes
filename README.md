Um dos primeiros softwares que criei utilizando a biblioteca Tkinter do Python, aplicado às disciplinas da minha universidade.

![Screenshot](https://i.imgur.com/mJ445n6.png)

# Modelamento matemático de um sistema Massa-Mola-Amortecedor com 1 G.L.
### Cálculo para a posição do centro de massa de um sistema mck 
Sendo conhecida a Frequência Natural (ωn) e o Coeficiente de Amortecimento (ζ), é conveniente criar mais uma variável dependente desses 2 para facilitar os cálulos, essa variável será δ, sendo ela dada por:
![Sistema de equações 1](https://i.imgur.com/p3u1Ttg.png)

O modelamento matemático de um sistema mck irá depender do seu valor de ζ, que pode ser dividido em 3 casos. O sistema de equações para cada caso está mostrado abaixo:

## Amortecimento Subcrítico (ζ<1)
![Sistema de equações 2](https://i.imgur.com/SJTDwsN.png)

## Amortecimento Crítico (ζ=1)
![Sistema de equações 3](https://i.imgur.com/WR3c9ZI.png)

## Amortecimento Supercrítico (ζ>1)
![Sistema de equações 4](https://i.imgur.com/HT1twwr.png)

O valor de x(t) é mostrado em um gráfico em função do tempo no output do programa
