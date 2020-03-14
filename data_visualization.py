import matplotlib.pyplot as plt


class Graph(object):

    def graphic(self, diameters, prices):
        plt.figure()
        plt.xlabel('Diameter')
        plt.ylabel('Price')
        plt.title('Diameter x Price')
        plt.plot(diameters, prices, 'k.')
        plt.axis([0, 60, 0, 60])
        plt.grid(True)
        plt.show()

    def scatter(self, model, x, y):
        plt.scatter(x, y, color='black')
        plt.plot(x, model.predict(x), color='blue', linewidth=3)
        plt.xlabel('x')
        plt.ylabel('y')
        plt.xticks(())
        plt.yticks(())
        plt.show()

