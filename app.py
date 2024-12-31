import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.read_csv("pizzas.csv")
model = LinearRegression()
x = df[["diameter"]]
y = df[["price"]]
model.fit(x, y)

df_1 = pd.read_csv("mozzarella.csv")
model_1 = LinearRegression()
x = df_1[["quantity"]]
y = df_1[["value"]]
model_1.fit(x, y)

df_2 = pd.read_csv("prosciutto.csv")
model_2 = LinearRegression()
x = df_2[["quantity"]]
y = df_2[["value"]]
model_2.fit(x, y)

def calculate_pizza_price(diameter, model):

    if diameter:
        return model.predict([[diameter]])[0][0]
    else:
        return 0.0

def calculate_mozzarella_price(mozzarella, model_1):

    if mozzarella:
        return model_1.predict([[mozzarella]])[0][0]
    else:
        return 0.0

def calculate_prosciutto_price(prosciutto, model_2):

    if prosciutto:
        return model_2.predict([[prosciutto]])[0][0]
    else:
        return 0.0

st.title("Pizza Prize Predictor")
st.divider()

diameter = st.number_input("Enter pizza diameter (cm):")
mozzarella = st.number_input("Enter mozzarella weight (grams):")
prosciutto = st.number_input("Enter prosciutto weight (grams):")

pizza_price = calculate_pizza_price(diameter, model)
mozzarella_price = calculate_mozzarella_price(mozzarella, model_1)
prosciutto_price = calculate_prosciutto_price(prosciutto, model_2)

if pizza_price > 0:
    st.write(f"A pizza with {diameter:.2f} cm of diameter is R${pizza_price:.2f}.")
if mozzarella_price > 0:
    st.write(f"{mozzarella:.2f} grams of cheese is R${mozzarella_price:.2f}.")
if prosciutto_price > 0:
    st.write(f"{prosciutto:.2f} grams of prosciutto is R${prosciutto_price:.2f}.")

st.divider()

total_value = (pizza_price + mozzarella_price + prosciutto_price)
st.write(f"The total price of your order is R${total_value:.2f}")

