from bs4 import BeautifulSoup
import requests

tickers = ('D05.SI', 'C31.SI', 'C6L.SI', 'C09.SI')

url = 'https://sg.finance.yahoo.com/quote/{}/key-statistics?p={}'

for ticker in tickers:
    html_doc = requests.get(url.format(ticker,ticker))
#print(html_doc.text)
    soup = BeautifulSoup(html_doc.text, 'html.parser')

    roe = soup.body.find_all('span', text='Return on equity')[0].find_parent('td').find_next_sibling().text
    print(f'{ticker} roe = {roe}')

# fp = open("contents.txt","w", encoding='utf-8')
# fp.write(soup.prettify())
# fp.close()



# import yfinance as yf

# dbs = yf.Ticker("MSFT")
# print(dbs.info)
# #print(dbs.actions)
# #   print(dbs.dividends)
# print('financials')
# print(dbs.balance_sheet)

# from yahoofinancials.yahoofinancials import YahooFinancials

# ticker = 'AAPL'
# yahoo_financials = YahooFinancials(ticker)
# print(yahoo_financials.get_financial_stmts('annual', 'balance'))
