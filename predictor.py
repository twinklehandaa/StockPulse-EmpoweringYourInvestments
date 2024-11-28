import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error
import matplotlib.pyplot as plt
import streamlit as st

st.set_page_config(layout="wide")

st.markdown(
    """
    <style>
    .main > div {
            padding-top: 0rem !important;
    }
    .main .block-container { 
    padding-top: 0rem; 
    }
    body {
       font-family: sans-serif;
       margin: 0; 
       padding:0;
    }
    .stButton>button {
        background-color: #3a3f86;
        color: white;
        border: none;
        padding: 10px 20px;
        margin-top:20px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        border-radius: 5px;  

    }
    .stTextInput>div>div>input {
        color: #444; /* Dark gray text */
    }
    
    footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #333; 
        color: white;
        text-align: center;
        padding: 10px 0;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Load the data
df = pd.read_csv("C:/Users/hp/mp/FINAL_FROM_DF.csv")

# Preprocess the data
df.drop(columns=['OPEN', 'HIGH', 'LOW', 'LAST', 'PREVCLOSE', 'TOTTRDQTY', 'TOTTRDVAL', 'TOTALTRADES', 'ISIN'], inplace=True)
df.dropna(inplace=True)
df['TIMESTAMP'] = pd.to_datetime(df['TIMESTAMP'])

# Streamlit app
st.title("Stock Forecast")

# Get the stock name from the user
stock_name = st.sidebar.text_input('Ticker')

if st.button("Let's Predict!"):
    if stock_name in df['SYMBOL'].unique():
        # Filter and preprocess data
        df_stock = df[df['SYMBOL'] == stock_name]
        df_stock = df_stock.sort_values('TIMESTAMP')
        df_stock.reset_index(drop=True, inplace=True)
        df_stock.drop(columns=['SYMBOL'], inplace=True)
        df_stock['PREVIOUS_CLOSE'] = df_stock['CLOSE'].shift(1)
        df_stock.drop(index=df_stock.index[0], axis=0, inplace=True)
        df_stock.drop(columns=['TIMESTAMP'], inplace=True)

        # Split data
        X = df_stock[['PREVIOUS_CLOSE']]
        y = df_stock['CLOSE']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Train the model
        model = LinearRegression()
        model.fit(X_train, y_train)

        # Make predictions
        y_pred = model.predict(X_test)

        # Evaluate the model
        r2 = r2_score(y_test, y_pred)
        mse = mean_squared_error(y_test, y_pred)
        
        last_close = df_stock['PREVIOUS_CLOSE'].iloc[-1]  # Get the last closing price
        future_price = model.predict([[last_close]]) 
    
        
        st.markdown(f"<h3 style='color: #333;'>Predicted future closing price for {stock_name}: {future_price[0]:.2f}</h3>", unsafe_allow_html=True)

        # # Display results
        # st.write(f'R-squared: {r2:.4f}')
        # st.write(f'Mean Squared Error: {mse:.4f}')

        # # Display model information
        # st.write(f"Model intercept: {model.intercept_:.4f}")
        # st.write(f"Model coefficient: {model.coef_[0]:.4f}")

        # # Display prediction results
        # results = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
        # results['Difference'] = results['Actual'] - results['Predicted']
        # st.write("\nPrediction Results:")
        # st.write(results.head())

        # # Display average difference
        # avg_diff = results['Difference'].mean()
        # st.write(f"\nAverage difference between actual and predicted values: {avg_diff:.4f}")

        # Plot the best fit line
        fig, ax = plt.subplots()
        ax.scatter(X_test, y_test, color='blue')
        ax.plot(X_test, y_pred, color='red')
        ax.set_xlabel('PREVIOUS_CLOSE')
        ax.set_ylabel('CLOSE')
        ax.set_title('Best Fit Line')
        st.pyplot(fig)

    else:
        st.write(f"The stock symbol \"{stock_name}\" does not exist in the dataset.")

st.markdown("<footer><p>&copy; 2024 StockPulse</p></footer>", unsafe_allow_html=True) 