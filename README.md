# StockPulse – Stock Trend Prediction Platform

## 📌 Overview
StockPulse is a machine learning-based web application that predicts short-term stock price trends using historical and real-time market data. The platform helps users analyze stock movement patterns through predictive modeling and visual insights.

## 🚀 Problem Statement
Stock market trends are volatile and difficult to interpret using raw data alone. This project aims to assist users in making informed decisions by predicting stock price direction based on historical trends.

## 🧾 Dataset
- Source: Financial market APIs (historical + live data)
- Size: Varies by stock symbol and time range
- Features: Open, Close, High, Low, Volume
- Target Variable: Price Trend (Up / Down)

## 🛠️ Tech Stack
- Programming Language: Python
- Libraries: Pandas, NumPy, Scikit-learn, Matplotlib
- Tools: Streamlit, APIs

## 🧠 Model & Approach
- Cleaned and preprocessed historical stock data
- Performed feature selection and scaling
- Implemented Logistic Regression for binary trend classification
- Evaluated model using train-test split

## 📊 Evaluation Metrics
- Accuracy: ~74%
- Confusion Matrix
- Precision & Recall

## 📈 Results
The model demonstrates reasonable trend prediction capability for short-term movements, highlighting the challenges of financial forecasting while providing useful directional insights.

## 🌐 Deployment
The application is deployed locally using Streamlit, enabling interactive stock selection and real-time visualization.

## ▶️ How to Run
1. Clone the repository  
2. Install dependencies  
   `pip install -r requirements.txt`  
3. Run the app  
   `streamlit run app.py`

## 🔮 Future Scope
- Incorporate advanced models (LSTM, Random Forest)
- Add technical indicators (RSI, MACD)
- Improve accuracy through feature engineering

## 👤 Author
Twinkle Handa  
GitHub: https://github.com/twinklehandaa

## 📸 Snapshots 

![image](https://github.com/user-attachments/assets/fb2236eb-9be5-4949-a5dc-8eaeb7f05fb8)

Fig1: Main menu showcasing the navigation bar to access other pages and the buttons for accessing the site's core functionalities: 'Analysis' and 'Prediction'.


      
![image](https://github.com/user-attachments/assets/4ffd7f72-376b-4971-a82e-ed9be09b90da)

Fig2: The ‘Stock Forecast’ page displays the predicted future closing price for shares with a graph illustrating the 'Best Fit Line' based on historical data."

                  
 
     
![image](https://github.com/user-attachments/assets/88dc44f5-217a-4d99-93c3-cea6e99ee9a9)

Fig3: The 'Stock Analyzer’ page showcases an interactive chart of stocks closing prices with customizable date ranges for analysis.



                                          
![image](https://github.com/user-attachments/assets/d5bdf08a-61df-4572-962c-afade203e0ac)

Fig4: The ‘Fundamental Data’ tab of the ‘Stock Analyzer’ page displays financial statements for a specific company. It includes detailed tables for the Balance Sheet, Income Statement, and Cash Flow Statement.
