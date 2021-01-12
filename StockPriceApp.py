import yfinance as yf
import streamlit as st

st.write("""
# Stock Price App
""")

user_input = st.text_area("Enter the Ticker Symbol", value="Ticker")


tickerData = yf.Ticker(user_input)
start_date = st.date_input('Start date')
end_date = st.date_input('End date')

tickerDf = tickerData.history(period='1d', start=start_date, end=end_date)

st.write("""# TICKER: """ +str(user_input)+ """\n # FROM: """ + str(start_date) + """\n # TO: """ + str(end_date))

st.write( """ # Closing Price""")
st.line_chart(tickerDf.Close)
