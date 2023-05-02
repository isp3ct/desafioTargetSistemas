distanciaTotal = 100  # km
velocidadeCarro = 110  # km/h
velocidadeCaminhao = 80  # km/h
tempoPedagio_Caminhao = 5  # minutos

#Convertendo o tempo em Horas
tempoPedagio_CaminhaoHoras = tempoPedagio_Caminhao / 60

# Calculo de distância percorrida p/veículo
distanciaCarro = distanciaTotal / 2
distanciaCaminhao = distanciaTotal / 2

# Tempo dos pedágios
distanciaCaminhao -= (velocidadeCaminhao * tempoPedagio_CaminhaoHoras) * 2

#Calculo para saber o tempo de cada veículo até o local
tempoCarro = distanciaCarro / velocidadeCarro
tempoCaminhao = distanciaCaminhao / velocidadeCaminhao

if tempoCarro < tempoCaminhao:
    print("O caminhão estará mais próximo de Ribeirão Preto.")
else:
    print("O carro estará mais próximo de Ribeirão Preto.")



#  O carro e o caminhão saem de cidades opostas. Eles vão se cruzar no meio do caminho e como a questão é: Qual veículo está mais próximo de Ribeirão Preto quando isso acontecer. Precisei fazer o seguinte: 
#  Calcular a distancia entre as cidades, sabendo que é 100km. Dividi pela metade e então teremos a distância percorrida p/veículo.
#  Após isso, calculei a velocidade de ambos os veículos mais o pedágio do caminhão, para saber o tempo que cada veículo leva para percorrer o trajeto até o ponto de encontro.
#  Depois de calcularmos esses tempos e compara-los, podemos ver que o carro tem um tempo de viagem menor que o do caminhão. Isso significa que o carro já percorreu uma distância maior em direção a Franca. Portanto o caminhão estará mais proximo de Ribeirão Preto. E se o tempo de viagem do caminhão for menor que o tempo de viagem do carro, então o caminhão estará mais próximo de Ribeirão Preto do que o carro estará de Franca.