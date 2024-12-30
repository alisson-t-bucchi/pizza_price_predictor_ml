import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model

#reading .cvs with pandas
df_1 = pd.read_csv("mozzarella.csv")
#print(df)

#transform in scatter plotter
df_1.plot(kind="scatter", x="quantia", y="valor")
plt.show()

#saving graphic
#plt.savefig("C:/Users/aliss/PycharmProjects/projeto-ml/pizzas_plotter.png")

model_1 = linear_model.LinearRegression()
x = df_1[["quantia"]]
y = df_1[["valor"]]
model_1.fit(x, y)

predict_2 = model_1.predict([[8]])[0][0]
print(predict_2)