import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model

#reading .cvs with pandas
df = pd.read_csv("pizzas.csv")
#print(df)

#transform in scatter plotter
df.plot(kind="scatter", x="diametro", y="preco")
#plt.show()

#saving graphic
#plt.savefig("C:/Users/aliss/PycharmProjects/projeto-ml/pizzas_plotter.png")

model = linear_model.LinearRegression()
x = df[["diametro"]]
y = df[["preco"]]
model.fit(x, y)

predict_1 = model.predict([[7]])[0][0]
print(predict_1)