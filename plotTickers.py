

from yahoo_fin.stock_info import get_data, get_day_gainers, tickers_sp500, get_live_price
from datetime import datetime, timedelta
import matplotlib.pyplot as plt

def plot_tickers(tickers, start_date=None, end_date=None):
    for ticker in tickers:
        df = get_data(ticker, index_as_date = False, start_date=start_date, end_date=end_date)
        plt.plot(df['date'], df['adjclose'], label=ticker)
    plt.xlabel('Date')
    plt.ylabel('Close Adjusted Price')
    plt.title('Ticker Prices')
    plt.legend()
    plt.show()

def get_top_gainer_tickers(num_tickers):
    top_gainers = get_day_gainers()
    tickers = top_gainers['Symbol'][:num_tickers].tolist()
    names = top_gainers['Name'][:num_tickers].tolist()
    ticker_to_name = {tickers[i]: names[i] for i in range(len(tickers))}
    print(ticker_to_name)
    return tickers

def get_tech_tickers():
    return ['msft', 'amzn', 'aapl', 'tsla', 'nvda', 'fb', 'googl', 'uber', 'lyft', 'adbe', 'baba', 'amd']

def main():
    tickers = get_tech_tickers()
    current_date = datetime.now()
    starting_date = current_date - timedelta(days=365)
    plot_tickers(tickers, start_date=starting_date.strftime('%m/%d/%Y'), end_date=current_date.strftime('%m/%d/%Y'))

if __name__ == "__main__":
    main()