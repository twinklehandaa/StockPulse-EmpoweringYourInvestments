import streamlit as st
import pandas as pd
from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.fundamentaldata import FundamentalData
import plotly.express as px
from stocknews import StockNews
import openai

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

# Alpha Vantage API key
api_key = 'MWLJPQIZ9WOWECUW'

# OpenAI API key
openai.api_key = "your-openai-api-key" 

st.title('Stock Analyzer')
ticker = st.sidebar.text_input('Ticker', 'AAPL')
start_date = st.sidebar.date_input('Start Date', pd.to_datetime("2020-01-01"))
end_date = st.sidebar.date_input('End Date', pd.to_datetime('2023-01-01'))

# Convert start_date and end_date to datetime
start_date = pd.to_datetime(start_date)
end_date = pd.to_datetime(end_date)

# Initialize Alpha Vantage TimeSeries client
if ticker:
    try:
        ts = TimeSeries(key=api_key, output_format='pandas')
        data, meta_data = ts.get_daily(symbol=ticker, outputsize='full')
        data = data[(data.index >= start_date) & (data.index <= end_date)]
        if not data.empty:

            fig = px.line(data.reset_index(), x='date', y='4. close', 
                         title=f'{ticker} Closing Prices')
            st.plotly_chart(fig)
            st.write(data)
        else:
            st.error('No data available for the selected ticker and date range.')
    except Exception as e:
        st.error(f"Error loading data: {e}")
else:
    st.error('Please enter a valid ticker symbol.')

# Tabs for additional information
pricing_data, fundamental_data, openai1 = st.tabs(
    ["Pricing Data", "Fundamental data", "OpenAI ChatGPT"])

# Pricing Data Tab
with pricing_data:
    st.header("Price Movements")
    st.write(data)

# Fundamental Data Tab
fd = FundamentalData(key=api_key, output_format='pandas')

with fundamental_data:
    st.subheader('Balance Sheet')
    try:
        balance_sheet, _ = fd.get_balance_sheet_annual(ticker)
        bs = balance_sheet.T[2:]
        bs.columns = list(balance_sheet.T.iloc[0])
        st.write(bs)
    except Exception as e:
        st.error(f"Error loading balance sheet: {e}")

    st.subheader('Income Statement')
    try:
        income_statement, _ = fd.get_income_statement_annual(ticker)
        is1 = income_statement.T[2:]
        is1.columns = list(income_statement.T.iloc[0])
        st.write(is1)
    except Exception as e:
        st.error(f"Error loading income statement: {e}")

    st.subheader('Cash Flow Statement')
    try:
        cash_flow, _ = fd.get_cash_flow_annual(ticker)
        cf = cash_flow.T[2:]

        cf.columns = list(cash_flow.T.iloc[0])
        st.write(cf)
    except Exception as e:
        st.error(f"Error loading cash flow statement: {e}")

# # News Tab
# with news:
#     try:
#         st.header(f'News of {ticker}')
#         sn = StockNews(ticker, save_news=False)
#         df_news = sn.read_rss()
#         for i in range(10):
#             st.subheader(f'News {i+1}')
#             st.write(df_news['Published'][i] if 'Published' in df_news.columns else "No published date available")
#             st.write(df_news['Title'][i])
#             st.write(df_news['Summary'][i])
#             st.write(f"Title Sentiment: {df_news.get('Sentiment_title', ['No sentiment'])[i]}")
#             st.write(f"News Sentiment: {df_news.get('Sentiment_summary', ['No sentiment'])[i]}")
#     except Exception as e:
#         st.error(f"Error loading news data: {e}")

# OpenAI ChatGPT Tab
def get_chatgpt_response(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "system", "content": "You are a helpful assistant."},
                      {"role": "user", "content": prompt}]
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        return f"Error in OpenAI API: {e}"

with openai1:
    buy_reason, sell_reason, swot_analysis = st.tabs(['3 reasons to buy', '3 reasons to sell', 'SWOT Analysis'])
    with buy_reason:
        st.subheader(f'3 Reasons to Buy {ticker} Stock')
        st.write(get_chatgpt_response(f"Give 3 reasons to buy {ticker} stock"))
    with sell_reason:
        st.subheader(f'3 Reasons to Sell {ticker} Stock')
        st.write(get_chatgpt_response(f"Give 3 reasons to sell {ticker} stock"))
    with swot_analysis:
        st.subheader(f'SWOT Analysis of {ticker} Stock')
        st.write(get_chatgpt_response(f"Provide a SWOT analysis of {ticker} stock"))
        
st.markdown("<footer><p>&copy; 2024 StockPulse</p></footer>", unsafe_allow_html=True) 