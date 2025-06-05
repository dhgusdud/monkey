import streamlit as st
import yfinance as yf
import plotly.graph_objects as go
import pandas as pd
from datetime import datetime, timedelta

# 글로벌 시가총액 Top 10 티커 (2025년 기준 추정)
top10_tickers = {
    "Apple": "AAPL",
    "Microsoft": "MSFT",
    "NVIDIA": "NVDA",
    "Alphabet (Google)": "GOOGL",
    "Amazon": "AMZN",
    "Meta (Facebook)": "META",
    "Berkshire Hathaway": "BRK-B",
    "Tesla": "TSLA",
    "Eli Lilly": "LLY",
    "Taiwan Semiconductor": "TSM"
}

# 스트림릿 설정
st.set_page_config(page_title="Global Top 10 Stocks", layout="wide")
st.title("📈 글로벌 시가총액 Top 10 기업의 최근 1년 주가 변화")

# 날짜 범위
end_date = datetime.today()
start_date = end_date - timedelta(days=365)

# 데이터 가져오기
@st.cache_data
def get_stock_data(tickers, start, end):
    data = {}
    for name, ticker in tickers.items():
        df = yf.download(ticker, start=start, end=end)
        df["Name"] = name
        data[name] = df
    return data

with st.spinner("데이터를 불러오는 중입니다..."):
    stock_data = get_stock_data(top10_tickers, start_date, end_date)

# Plotly 그래프 생성
fig = go.Figure()

for name, df in stock_data.items():
    fig.add_trace(go.Scatter(
        x=df.index,
        y=df["Adj Close"],
        mode="lines",
        name=name
    ))

fig.update_layout(
    title="최근 1년간 글로벌 시가총액 Top 10 기업 주가 변화",
    xaxis_title="날짜",
    yaxis_title="조정 종가 (USD)",
    template="plotly_dark",
    legend_title="기업명",
    hovermode="x unified"
)

st.plotly_chart(fig, use_container_width=True)

