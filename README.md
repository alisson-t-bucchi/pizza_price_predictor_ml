# 🍕 Pizza Price Predictor using Machine Learning. 

This is an interactive application developed with **Streamlit**, **Scikit-learn** and **Matplotlib** libraries and .csv files. 

The objective is predict the price of a pizza based on its diameter and calculate the cost of the required mozzarella cheese using linear regression.  

## 📝 Features

- **Pizza price prediction**: Based on the diameter (in centimeters).
- **Mozzarella cost calculation**: Based on the weight of mozzarella (in grams).
- **Total order value calculation**: Sum of the pizza price and the mozzarella cost.

## Requirements

Make sure you have the following installed on your machine:

- Python 3.8 or higher
- Libraries listed in `requirements.txt`

## 🚀 Installation

1. Clone the repository or download the files.
   ```bash
   git clone <repository-url>
   cd <repository-name>
   ```

2. Install the dependencies.
   ```bash
   pip install -r requirements.txt
   ```

3. Ensure that the `pizzas.csv` and `mozzarella.csv` files are in the same directory as the code.

## 📊 Data Structure

### pizzas.csv
The `pizzas.csv` file should contain the following columns:
- **diameter**: Pizza diameter in centimeters.
- **price**: Corresponding price in currency.

### mozzarella.csv
The `mozzarella.csv` file should contain the following columns:
- **quantity**: Weight of mozzarella in grams.
- **value**: Corresponding price in currency.

## 🛞 Usage

1. Run the Streamlit application.
   ```bash
   streamlit run <file-name>.py
   ```

2. Enter the following data into the application:
   - **Pizza diameter (in cm):** To calculate the pizza price.
   - **Mozzarella weight (in grams):** To calculate the cheese cost.

3. View the estimated pizza price, cheese cost, and total order value.

## Main Code

```python
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

def calculate_pizza_price(diameter, model):

    if diameter:
        return model.predict([[diameter]])[0][0]
    else:
        return 0.0

#see the full code in this repository! 
```

## ⚠️ Notes

- Ensure that the CSV files contain enough data to train the linear regression models.
- The application uses the `scikit-learn` library to build and utilize the predictive models.

## 🗒️ License

This project is licensed under the MIT License. See the `LICENSE` file for more information.
