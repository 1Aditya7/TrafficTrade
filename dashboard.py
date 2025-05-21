import os
import pandas as pd
import streamlit as st
import alpaca_trade_api as tradeapi

from dotenv import load_dotenv
load_dotenv()


# Alpaca Setup
API_KEY = os.getenv("APCA_API_KEY_ID")
API_SECRET = os.getenv("APCA_API_SECRET_KEY")
BASE_URL = "https://paper-api.alpaca.markets"
api = tradeapi.REST(API_KEY, API_SECRET, BASE_URL)

# Layout config
st.set_page_config(page_title="🚦 TrafficTrade Dashboard", layout="wide")
st.title("🚦 TrafficTrade Live Dashboard")

col1, col2 = st.columns(2)

# 📊 Show recent congestion scores
with col1:
    st.subheader("📈 Congestion Score History")
    score_file = "data/traffic_scores.csv"
    if os.path.exists(score_file):
        df = pd.read_csv(score_file)
        st.line_chart(df.set_index("timestamp")["score"])
        st.dataframe(df.tail(10))
    else:
        st.warning("No congestion score data found.")

# 📄 Show trade log
with col2:
    st.subheader("🪙 Trade Log")
    trade_log_path = "data/trade_log.csv"
    if os.path.exists(trade_log_path):
        trades = pd.read_csv(trade_log_path)
        st.dataframe(trades.tail(10))
    else:
        st.warning("No trades recorded yet.")

# 💼 Alpaca Position & Portfolio
st.subheader("📊 Portfolio Status")

try:
    account = api.get_account()
    st.metric(label="Cash Balance", value=f"${account.cash}")
    st.metric(label="Portfolio Value", value=f"${account.portfolio_value}")

    positions = api.list_positions()
    if positions:
        pos_data = [{
            "Symbol": p.symbol,
            "Qty": p.qty,
            "Side": p.side,
            "Market Value": p.market_value,
            "Unrealized PnL": p.unrealized_pl
        } for p in positions]
        st.table(pd.DataFrame(pos_data))
    else:
        st.info("No open positions.")
except Exception as e:
    st.error(f"Failed to load Alpaca data: {e}")
