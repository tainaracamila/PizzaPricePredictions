"""
Prevendo o Preço da Pizza

Suponha que você queira prever o preço da pizza.
Para isso, vamos criar um modelo de regressão linear para prever o preço da pizza, baseado em um atributo da pizza
que podemos observar. Vamos modelar a relação entre o tamanho (diâmetro) de uma pizza e seu preço.
Escreveremos então um programa com sckit-learn, que prevê o preço da pizza dado seu tamanho.

"""

import numpy as np
import pandas as pd
from data_visualization import Graph
from sklearn.linear_model import LinearRegression

if __name__ == '__main__':

    gp = Graph()
    model = LinearRegression()

    # Getting data
    data = pd.read_csv('dados.csv', delimiter=';')
    diameter = list(data['Diametro'])
    price = list(data['Preco'])

    # Visualizing data through a graph
    # gp.graphic(diameter, price)

    # Transforming data
    x = [[x] for x in diameter]
    y = [[x] for x in price]

    # Training model
    model.fit(x, y)

    # Diameters to predict
    pizza_20cm = 20
    pizza_50cm = 50

    # Results
    print("A pizza with 20cm should cost: R$%.2f." % model.predict([[pizza_20cm]]))
    print("A pizza with 50cm should cost: R$%.2f." % model.predict([[pizza_50cm]]))

    print('\nCoefficient: %f' % model.coef_)
    print('Mean square error: %.2f' % np.mean((model.predict(x) - y) ** 2))
    print('Variation score: %.2f' % model.score(x, y))

    #gp.scatter(model, x, y)