import yfinance as yf
import streamlit as st

st.write("""
# Stock Price App
""")


st.sidebar.header('Show')
graphnames = ['Open', 'Close','High', 'Low']
selected_graph = st.sidebar.selectbox('Graph', graphnames)
user_input = st.text_area("Enter the Ticker Symbol", value="Ticker")
print(selected_graph)

tickerData = yf.Ticker(user_input)
start_date = st.date_input('Start date')
end_date = st.date_input('End date')

tickerDf = tickerData.history(period='1d', start=start_date, end=end_date)

st.write("""# TICKER: """ +str(user_input)+ """\n # FROM: """ + str(start_date) + """\n # TO: """ + str(end_date))

st.write( """ # """ + str(selected_graph))

#st.line_chart(tickerDf.selected_graph.lower())
