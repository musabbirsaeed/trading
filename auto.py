import streamlit as st
#from streamlit_autorefresh import st_autorefresh
import pandas as pd
from tradingview_ta import TA_Handler, Interval, Exchange
import plotly.express as px

st.set_page_config(layout="wide")


# Run the autorefresh about every 2000 milliseconds (2 seconds) and stop
# after it's been refreshed 100 times.
#count = st_autorefresh(interval=2000, limit=100, key="fizzbuzzcounter")

# The function returns a counter for number of refreshes. This allows the
# ability to make special requests at different intervals based on the count
symbls = [
'AAL',
'AAPL',
'ABMD',
'ABNB',
'ADBE',
'ADI',
'ADP',
'ADSK',
'AEP',
'AKAM',
'ALGN',
'ALNY',
'AMAT',
'AMD',
'AMGN',
'AMZN',
'ANSS',
'APA',
'APP',
'ATVI',
'AVGO',
'BIIB',
'BKNG',
'BKR',
'BMRN',
'CDNS',
'CDW',
'CEG',
'CERN',
'CG',
'CHK',
'CHRW',
'CHTR',
'CINF',
'CMCSA',
'CME',
'COIN',
'COST',
'CPRT',
'CRWD',
'CSCO',
'CSGP',
'CSX',
'CTAS',
'CTSH',
'CTXS',
'CZR',
'DDOG',
'DISH',
'DLTR',
'DOCU',
'DXCM',
'EA',
'EBAY',
'ENPH',
'ENTG',
'EQIX',
'ETSY',
'EWBC',
'EXC',
'EXPD',
'EXPE',
'FANG',
'FAST',
'FB',
'FCNCA',
'FFIV',
'FISV',
'FITB',
'FOX',
'FOXA',
'FTNT',
'FWONA',
'FWONK',
'GFS',
'GILD',
'GLPI',
'GOOG',
'GOOGL',
'HAS',
'HBAN',
'HOLX',
'HON',
'HSIC',
'HST',
'IDXX',
'IEP',
'ILMN',
'INCY',
'INTC',
'INTU',
'ISRG',
'JBHT',
'JKHY',
'KDP',
'KHC',
'KLAC',
'LAMR',
'LBRDA',
'LBRDK',
'LCID',
'LKQ',
'LNT',
'LPLA',
'LRCX',
'LSXMA',
'LSXMB',
'LSXMK',
'MAR',
'MCHP',
'MDB',
'MDLZ',
'MKTX',
'MNST',
'MORN',
'MPWR',
'MRNA',
'MSFT',
'MTCH',
'MU',
'NDAQ',
'NDSN',
'NFLX',
'NLOK',
'NTAP',
'NTRS',
'NVDA',
'NWS',
'NWSA',
'ODFL',
'OKTA',
'OLPX',
'ON',
'ORLY',
'PANW',
'PARA',
'PARAA',
'PAYX',
'PCAR',
'PEP',
'PFG',
'PLUG',
'PODD',
'POOL',
'PTC',
'PYPL',
'QCOM',
'QRVO',
'REG',
'REGN',
'RIVN',
'ROKU',
'ROST',
'RPRX',
'SBAC',
'SBNY',
'SBUX',
'SGEN',
'SIRI',
'SIVB',
'SNPS',
'SPLK',
'SSNC',
'STLD',
'SWKS',
'TECH',
'TER',
'TMUS',
'TRMB',
'TROW',
'TSCO',
'TSLA',
'TTD',
'TTWO',
'TW',
'TXN',
'UAL',
'ULTA',
'UTHR',
'VRSK',
'VRSN',
'VRTX',
'VTRS',
'WBA',
'WBD',
'WDAY',
'WDC',
'WMG',
'XEL',
'Z',
'ZBRA',
'ZG',
'ZI',
'ZM',
'ZS']

def get_data():

    d = {}
    for symbl in symbls:
        try:
            output = TA_Handler(
            symbol=symbl,
            screener="america",
            exchange="NASDAQ",
            interval=Interval.INTERVAL_1_DAY)
            d[symbl] = output.get_analysis().summary
            
        except Exception:
            pass
    return d

data = get_data()
df = pd.DataFrame(data).T
df = df.reset_index()

st.write("This recommendation based on 26 indexes based on tradingview-ta")

st.dataframe(df)



fig1 = px.histogram(df, x="index", y=['BUY', 'SELL', 'NEUTRAL'], title="Buy, Sell, Neutral")

st.plotly_chart(fig1, use_container_width=True)

fig2 = px.scatter(df, x="index", y='RECOMMENDATION', title="Which Stock to buy and which stock to sell")
st.plotly_chart(fig2, use_container_width=True)


# ---- HIDE STREAMLIT STYLE ----
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

